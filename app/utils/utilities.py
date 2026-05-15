from app.exceptions import AppException

#parse_raw_job_text
MAX_TITLE_LENGHT = 80
MAX_COMPANY_LENTH = 100

# description length validator
MAX_JOB_DESCRIPTION_TEXT_LENGTH = 5000

def validate_description(text: str):
    if(len(text)) > MAX_JOB_DESCRIPTION_TEXT_LENGTH:
        raise AppException("Raw job description too long", 413)

def parse_raw_job_text(text:str):
    if not text or not text.strip():
        raise ValueError("Empty job description")
    
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    
    line1 = lines[0] if len(lines) > 0 else None
    # print(f"Lines [0]: {lines[0]}\n")
    
    line2 = lines[1] if len(lines) > 1 else "Unknown"
    # print(f"Lines [1]: {lines[1]}\n")
    
    description_lines = lines[2:]

    # for index, line in enumerate(lines[2:], start=2):
    #     print(f"Line [{index}]: {line}")

    # Reconstructing original description

    ## Validate if truly company name or just another description text
    company = line2 if len(line2) <= MAX_COMPANY_LENTH else "Unknown"
    # description_lines.insert(0, company)
    if company =="Unknown":
        description_lines.insert(0,line2)

    # # Validate if try title name or just another description text
    title = line1 if len(line1) <= MAX_TITLE_LENGHT else "Unknown"
    # description_lines.insert(0, title)
    if title == "Unknown":
        description_lines.insert(0,line1)

    description = "\n".join(description_lines)

    # print("#### --------- PRINTING OBJECT ------------ ####")
    return {
        "title": title,
        "company" : company,
        "description": description
    }