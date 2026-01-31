import re

def extract_basic_fields(text: str) -> dict:
    fields = {}

    inv_no = re.search(r"Invoice Number:\s*(.+)", text)
    if inv_no:
        fields["invoice_number"] = inv_no.group(1).strip()

    inv_date = re.search(r"Invoice Date:\s*(.+)", text)
    if inv_date:
        fields["invoice_date"] = inv_date.group(1).strip()

    po_ref = re.search(r"PO Reference:\s*(.+)", text)
    if po_ref:
        fields["po_reference"] = po_ref.group(1).strip()

    # Supplier is usually first line
    fields["supplier"] = text.split("\n")[0].strip()

    return fields
