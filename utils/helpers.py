def fix_objectid(doc: dict) -> dict:
    """Convert ObjectId -> str for JSON"""
    doc["_id"] = str(doc["_id"])
    return doc
