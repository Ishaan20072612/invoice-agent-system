def resolution_agent(state):
    discrepancies = state.get("discrepancies", [])

    if discrepancies:
        state["decision"] = "manual_review"
    else:
        state["decision"] = "auto_approve"

    return state

