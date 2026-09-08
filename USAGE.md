# Usage Guide

## 1. Email

Enter an email address. The tool checks:
- basic syntax
- domain
- MX records

It does not attempt mailbox verification and does not search breach databases.

## 2. Name

The tool creates exact-name search queries. Search engines decide which public pages are returned.

## 3. Social accounts

The tool creates `site:` searches for common public platforms. A search hit is only a lead, not proof of identity.

## 4. IP information

Enter a public IP address. The module returns basic geolocation/network metadata from the public API.

Do not use the result to infer a person's exact physical location.

## 5. Passive domain recon

Use only a domain you own or are authorized to investigate. The module reads public certificate-transparency data and does not perform port scans or exploitation.
