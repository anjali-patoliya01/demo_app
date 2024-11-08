def event_has_permission(doc, user=None, permission_type=None):
    # when reading a document allow if event is Public
    if permission_type == "read" and doc.event_type == "Public":
        return True

    # when writing a document allow if event owned by user
    if permission_type == "write" and doc.owner == user:
        return True

    return False


