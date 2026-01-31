def discrepancy_agent(state):
    discrepancies = []

    invoice_items = state["document"].get("line_items", [])
    po_items = state["matching"].get("po_items", [])

    po_map = {item["item_code"]: item for item in po_items}

    for inv in invoice_items:
        code = inv["item_code"]

        if code not in po_map:
            discrepancies.append({
                "type": "ITEM_NOT_IN_PO",
                "item_code": code
            })
            continue

        po = po_map[code]

        if abs(inv["unit_price"] - po["unit_price"]) > 0.01:
            discrepancies.append({
                "type": "PRICE_MISMATCH",
                "item_code": code,
                "invoice_price": inv["unit_price"],
                "po_price": po["unit_price"]
            })

        if inv["quantity"] != po["quantity"]:
            discrepancies.append({
                "type": "QUANTITY_MISMATCH",
                "item_code": code
            })

    state["discrepancies"] = discrepancies
    return state

