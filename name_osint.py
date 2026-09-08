from urllib.parse import quote_plus


def name_searches(name: str):
    q = quote_plus(f'"{name.strip()}"')
    return [
        {"label": "Google exact-name search", "url": f"https://www.google.com/search?q={q}"},
        {"label": "Bing exact-name search", "url": f"https://www.bing.com/search?q={q}"},
        {"label": "DuckDuckGo exact-name search", "url": f"https://duckduckgo.com/?q={q}"},
    ]
