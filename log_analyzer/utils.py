from datetime import datetime

def parse_iso(s: str):
    # helper to parse ISO-like dates, fallback raises ValueError
    return datetime.fromisoformat(s)
