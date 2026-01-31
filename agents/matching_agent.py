def matching_agent(state: dict) -> dict:
    state["matching"] = {
        "matched_po": "PO-TEST",
        "confidence": 0.95
    }
    return state