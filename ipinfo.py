import ipaddress
import requests


def lookup_ip(ip: str) -> dict:
    ip = ip.strip()
    parsed = ipaddress.ip_address(ip)

    if parsed.is_private or parsed.is_loopback or parsed.is_reserved:
        return {
            "ip": ip,
            "status": "local_or_reserved",
            "message": "This module is intended for public IP information."
        }

    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url, timeout=10, headers={"User-Agent": "CyberEdu-OSINT/1.0"})
    response.raise_for_status()
    data = response.json()

    # Keep the educational output focused; do not expose unnecessary fields.
    allowed = [
        "ip", "version", "city", "region", "country_name", "country_code",
        "latitude", "longitude", "postal", "timezone", "utc_offset",
        "asn", "org"
    ]
    return {k: data.get(k) for k in allowed if k in data}
