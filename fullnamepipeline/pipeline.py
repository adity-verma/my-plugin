def add_full_name(strategy, details, backend, user = None, *args, **kwargs):
    """
    Social-auth pipeline step: ensure details['fullname'] is 'First Last'.
    """
    first = (details.get("first_name") or "").strip()
    last = (details.get("last_name") or "").strip()
    full = f"{first} {last}".strip()

    if not full:
        full = "Fullname"

    # Only set fullname if we actually built something
    if full:
        # Either mutate in place or return an update dict; both are acceptable.
        details["fullname"] = full
        return {"details": details}
    return None

