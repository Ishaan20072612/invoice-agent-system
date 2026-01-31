from utils.pdf_utils import extract_text_from_pdf
from utils.ocr import ocr_image
from utils.basic_field_parser import extract_basic_fields
from utils.line_item_parser import extract_line_items


def document_agent(state: dict) -> dict:
    invoice_path = state["invoice_path"]

    text = extract_text_from_pdf(invoice_path)

    used_ocr = False
    confidence = 0.95

    if not text or len(text.strip()) < 50:
        text = ocr_image(invoice_path)
        used_ocr = True
        confidence = 0.80

    fields = extract_basic_fields(text)
    line_items = extract_line_items(text)

    state["document"] = {
        "raw_text": text[:1200],
        "fields": fields,
        "line_items": line_items,
        "used_ocr": used_ocr,
        "extraction_confidence": confidence,
    }

    return state

