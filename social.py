from urllib.parse import quote_plus


PLATFORMS = {
    "GitHub": "site:github.com",
    "LinkedIn": "site:linkedin.com/in",
    "Instagram": "site:instagram.com",
    "X": "site:x.com OR site:twitter.com",
    "Reddit": "site:reddit.com/u OR site:reddit.com/user",
    "YouTube": "site:youtube.com",
}


def social_searches(value: str):
    value = value.strip()
    q = quote_plus(value)
    results = []
    for platform, operator in PLATFORMS.items():
        query = quote_plus(f"{operator} {value}")
        results.append({
            "platform": platform,
            "url": f"https://www.google.com/search?q={query}",
            "input": value,
        })
    return results
