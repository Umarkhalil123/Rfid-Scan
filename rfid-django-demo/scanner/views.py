from django.contrib import messages
from django.db import DatabaseError, IntegrityError, OperationalError, transaction
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import ScanForm
from .models import CardOwner, ScanRecord


def scan_page(request):
    owners_by_uid = {}
    try:
        owners_by_uid = {
            owner.card_uid: {
                "employee_id": owner.employee_id,
                "employee_name": owner.employee_name,
                "department": owner.department,
            }
            for owner in CardOwner.objects.all()
        }
    except OperationalError:
        messages.error(
            request,
            "Database tables are not ready. Run migrations and reload this page.",
        )

    # POST saves one scan record, GET shows a blank form.
    if request.method == "POST":
        form = ScanForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            card_uid = form_data["card_uid"]
            try:
                with transaction.atomic():
                    owner = CardOwner.objects.filter(card_uid=card_uid).first()
                    if owner is None:
                        # New card requires basic employee details before first save.
                        if not all(
                            [
                                form_data.get("employee_id"),
                                form_data.get("employee_name"),
                                form_data.get("department"),
                            ]
                        ):
                            form.add_error(
                                None,
                                "Unknown card: fill Employee ID, Name, and Department, then save.",
                            )
                            raise ValueError("Missing fields for new card mapping.")
                        owner = CardOwner.objects.create(
                            card_uid=card_uid,
                            employee_id=form_data.get("employee_id", ""),
                            employee_name=form_data.get("employee_name", ""),
                            department=form_data.get("department", ""),
                        )
                        messages.success(request, "New card owner created successfully.")
                    else:
                        # Keep owner details up to date if user edited any fields.
                        owner.employee_id = form_data.get("employee_id", owner.employee_id)
                        owner.employee_name = form_data.get("employee_name", owner.employee_name)
                        owner.department = form_data.get("department", owner.department)
                        owner.save()

                    now = timezone.now()
                    open_record = (
                        ScanRecord.objects.filter(card_uid=card_uid, time_out__isnull=True)
                        .order_by("-time_in")
                        .first()
                    )
                    if open_record:
                        # Second scan closes attendance window as time-out.
                        open_record.time_out = now
                        open_record.employee_id = owner.employee_id
                        open_record.employee_name = owner.employee_name
                        open_record.department = owner.department
                        open_record.save()
                        messages.success(request, "Attendance saved: Time Out marked.")
                    else:
                        # First scan starts attendance window as time-in.
                        ScanRecord.objects.create(
                            card_uid=card_uid,
                            employee_id=owner.employee_id,
                            employee_name=owner.employee_name,
                            department=owner.department,
                            time_in=now,
                        )
                        messages.success(request, "Attendance saved: Time In marked.")
                if not form.errors:
                    return redirect("scan-page")
            except ValueError:
                # Validation-style flow: form errors are already attached above.
                pass
            except IntegrityError:
                form.add_error(None, "Duplicate card or conflicting data. Please verify inputs.")
            except DatabaseError:
                form.add_error(None, "Database error occurred while saving attendance.")
    else:
        form = ScanForm()

    # Keep the page lightweight by rendering only recent entries.
    recent_scans = []
    try:
        recent_scans = ScanRecord.objects.order_by("-time_in")[:10]
    except OperationalError:
        messages.error(
            request,
            "Could not load recent scans because database tables are missing.",
        )
    return render(
        request,
        "scanner/scan_form.html",
        {"form": form, "recent_scans": recent_scans, "owners_by_uid": owners_by_uid},
    )
