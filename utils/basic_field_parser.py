import re

def extract_basic_fields(text: str) -> dict:
    fields = {}

    invoice_no = re.search(r"Invoice Number:\s*(.+)", text)
    date = re.search(r"Invoice Date:\s*(.+)", text)
    po = re.search(r"PO Reference:\s*(.+)", text)
    supplier = re.search(r"^(.*)\nINVOICE", text)

    if invoice_no:
        fields["invoice_number"] = invoice_no.group(1).strip()
    if date:
        fields["invoice_date"] = date.group(1).strip()
    if po:
        fields["po_reference"] = po.group(1).strip()
    if supplier:
        fields["supplier"] = supplier.group(1).strip()

    return fields
