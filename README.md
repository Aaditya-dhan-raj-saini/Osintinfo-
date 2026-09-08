# CyberEdu OSINT Toolkit

A beginner-friendly, **educational and defensive OSINT toolkit** for learning how public information can be investigated responsibly.

## Features

1. **theHarvester-style passive domain recon**
   - Looks up public DNS records.
   - Queries public certificate-transparency data (crt.sh).
   - Does not exploit systems or bypass access controls.
2. **Email analysis**
   - Syntax validation.
   - Domain extraction.
   - DNS MX lookup.
   - Generates public search links for learning.
3. **Name OSINT**
   - Generates public search-engine queries for a name.
   - No private-data lookup or authentication bypass.
4. **Social-account discovery**
   - Generates public search links for common platforms.
   - It does **not** claim an account exists unless a public result is manually verified.
5. **IP information**
   - Looks up a user-supplied public IP using a public IP information API.
   - Never scans ports or attacks the IP.

## Safety boundary

Use this project only with information you are authorized to investigate. It is intentionally limited to **passive, publicly available information**. It does not include password attacks, credential theft, malware, exploitation, port scanning, private-account access, or data-broker/breach searches.

## Requirements

- Python 3.10+
- Internet connection for DNS, crt.sh, search links, and IP information.

Install:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

Run:

```bash
python main.py
```

## Examples

```text
1. Email analysis
2. Name OSINT
3. Social-account search
4. IP information
5. Passive domain recon
```

### Important limitation

Search links are intentionally provided instead of automated social-media scraping. Public search results can be incomplete, stale, or misleading. Always verify information manually.

## GitHub

Create a repository named `cyberedu-osint`, then:

```bash
git init
git add .
git commit -m "Initial educational OSINT toolkit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/cyberedu-osint.git
git push -u origin main
```

Do not commit API keys, passwords, cookies, private datasets, or personal investigation data.

## License

MIT License. See `LICENSE`.
