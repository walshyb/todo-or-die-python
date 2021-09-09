def generate_message(message: str, date: str = "") -> str:
    date_text = f" by {date}" if date else ""
    return f"TODO, '{message}', was not completed{date_text}. Get on this!"