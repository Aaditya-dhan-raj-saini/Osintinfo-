import re
import requests


DOMAIN_RE = re.compile(
    r"^(?=.{1,253}$)([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[A-Za-z]{2,63}$"
)


def passive_domain_recon(domain: str) -> dict:
    domain = domain.strip().lower().rstrip(".")
    if not DOMAIN_RE.match(domain):
        raise ValueError("Enter a valid domain such as example.com")

    result = {
        "domain": domain,
        "mode": "passive",
        "subdomains_from_certificate_transparency": [],
        "notes": [
            "This is a learning-oriented, passive alternative to active scanning.",
            "Certificate transparency results can include historical or unrelated entries."
        ]
    }

    # Public Certificate Transparency endpoint.
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    response = requests.get(
        url,
        timeout=15,
        headers={"User-Agent": "CyberEdu-OSINT/1.0"}
    )
    response.raise_for_status()

    names = set()
    for row in response.json():
        for name in str(row.get("name_value", "")).splitlines():
            name = name.strip().lower().lstrip("*.")
            if name == domain or name.endswith("." + domain):
                names.add(name)

    result["subdomains_from_certificate_transparency"] = sorted(names)
    return result
