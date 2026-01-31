import re

def extract_line_items(text: str):
    items = []

    pattern = re.compile(
        r"""
        (?P<code>[A-Z]{2,5}-\d{3})\s+          # Item code (API-001)
        (?P<desc>[A-Za-z0-9\s]+?)\s+           # Description
        (?P<qty>\d+)\s+kg\s+                   # Quantity
        £(?P<unit>[\d,]+\.\d{2})\s+            # Unit price
        £(?P<total>[\d,]+\.\d{2})               # Total
        """,
        re.VERBOSE
    )

    for match in pattern.finditer(text):
        items.append({
            "item_code": match.group("code"),
            "description": match.group("desc").strip(),
            "quantity": int(match.group("qty")),
            "unit_price": float(match.group("unit").replace(",", "")),
            "total": float(match.group("total").replace(",", "")),
        })

    return items