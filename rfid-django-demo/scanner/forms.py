from django import forms

from .models import ScanRecord


class ScanForm(forms.ModelForm):
    class Meta:
        model = ScanRecord
        fields = ["card_uid", "employee_id", "employee_name", "department"]
        widgets = {
            "card_uid": forms.TextInput(attrs={"placeholder": "Scan card here"}),
            "employee_id": forms.TextInput(attrs={"placeholder": "Employee ID"}),
            "employee_name": forms.TextInput(attrs={"placeholder": "Employee name"}),
            "department": forms.TextInput(attrs={"placeholder": "Department"}),
        }

    def clean_card_uid(self):
        card_uid = (self.cleaned_data.get("card_uid") or "").strip()
        if not card_uid:
            raise forms.ValidationError("Card UID is required.")
        return card_uid
