"""Detect likely RFID/HID readers connected to this machine."""

import hid

KEYWORDS = ("rfid", "prox", "nfc", "reader", "card")


def detect_possible_readers():
    devices = hid.enumerate()
    matches = []

    for d in devices:
        product = (d.get("product_string") or "").lower()
        manufacturer = (d.get("manufacturer_string") or "").lower()
        joined_text = f"{manufacturer} {product}"
        if any(k in joined_text for k in KEYWORDS):
            matches.append(d)

    return matches


def main():
    matches = detect_possible_readers()
    if not matches:
        print("No obvious RFID reader detected.")
        print("Tip: many readers still work as keyboard wedge even if not listed by keywords.")
        return

    print("Possible RFID reader devices:")
    for item in matches:
        vendor_id = item.get("vendor_id", 0)
        product_id = item.get("product_id", 0)
        manufacturer = item.get("manufacturer_string") or "UnknownManufacturer"
        product = item.get("product_string") or "UnknownProduct"
        print(
            f"- VID:{vendor_id:04x} PID:{product_id:04x} "
            f"Manufacturer:{manufacturer} Product:{product}"
        )


if __name__ == "__main__":
    main()
