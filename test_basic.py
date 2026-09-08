from cyberedu.email_osint import analyze_email
from cyberedu.name_osint import name_searches
from cyberedu.social import social_searches


def test_email():
    result = analyze_email("student@example.com")
    assert result["valid_syntax"] is True
    assert result["domain"] == "example.com"


def test_name_links():
    results = name_searches("Ada Lovelace")
    assert len(results) >= 3
    assert all(item["url"].startswith("https://") for item in results)


def test_social_links():
    results = social_searches("student@example.com")
    assert len(results) >= 5
    assert all("url" in item for item in results)
