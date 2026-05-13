def parse_raw_job_text(text:str):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    data = {
        "title": lines[0] if len(lines) > 0 else "Unknown",
        "company" : lines[1] if len(lines) > 0 else "Unknown",
        "description": "\n".join(lines[2:]) if len(lines) > 2 else ""
    }
    return data