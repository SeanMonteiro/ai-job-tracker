def parse_raw_job_text(text:str):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    data = {
        "title": lines[0] if len(lines) > 0 else "Unknown",
        "company" : lines[1] if len(lines) > 0 else "Unknown",
        "description": "\n".join(lines[2:]) if len(lines) > 2 else ""
    }
    return data

# raw_text = (
#     "Software Engineer\n"
#     "Lifelabs\n"
#     "2+ years of software engineering industry experience building and shipping production applications. "
#     "Strong coding skills in Python and/or C#, with solid backend engineering fundamentals. "
#     "Experience with modern web development using JavaScript/TypeScript, and ideally React or similar frameworks. "
#     "Experience building or integrating API-driven systems and working across application layers. "
#     "Practical familiarity with LLMs, AI developer tools, or AI-powered product features. "
#     "Ability to turn ambiguous product or engineering requirements into structured implementation plans. "
#     "Good judgment around when AI should be used for generation, reasoning, or assistance, and when traditional software logic should drive behavior. "
#     "Strong problem-solving skills, attention to quality, and a builder mindset. "
#     "Attention to quality, a builder mindset, and comfort with code reviews, testing, and continuous improvement. "
#     "Clear written and verbal communication. "
#     "Nice to Have: Has used AI coding tools to meaningfully change how they build software, not just experimented with them. "
#     "Familiarity with Docker, Kubernetes, or Azure. "
#     "Experience shipping AI-powered product features in enterprise software. "
#     "Interest in cybersecurity, automation, or workflow-heavy systems. "
#     "Exposure to evaluation, prompt iteration, or reliability practices for LLM applications."
# )

# print(parse_raw_job_text(raw_text))