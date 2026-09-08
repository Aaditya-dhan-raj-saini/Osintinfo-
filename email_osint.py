import re
import socket

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def analyze_email(email: str) -> dict:
    email = email.strip()
    result = {
        "email": email,
        "valid_syntax": bool(EMAIL_RE.match(email)),
        "domain": None,
        "mx_records": [],
        "notes": [
            "Syntax and DNS data do not prove that a mailbox exists.",
            "No breach databases or private-account data are queried."
        ],
    }

    if not result["valid_syntax"]:
        return result

    domain = email.rsplit("@", 1)[1].lower()
    result["domain"] = domain

    try:
        import dns.resolver
        answers = dns.resolver.resolve(domain, "MX")
        result["mx_records"] = sorted(
            [{"priority": r.preference, "host": str(r.exchange).rstrip(".")} for r in answers],
            key=lambda x: x["priority"]
        )
    except Exception as exc:
        result["mx_lookup_error"] = str(exc)

    return result
