import json
from urllib.parse import quote_plus

from .email_osint import analyze_email
from .name_osint import name_searches
from .social import social_searches
from .ipinfo import lookup_ip
from .harvester import passive_domain_recon


BANNER = r"""
===========================================================
                 CYBEREDU OSINT TOOLKIT
       Educational • Passive • Public Information
===========================================================
"""


def print_json(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))


def run():
    print(BANNER)
    while True:
        print("\nChoose a module:")
        print("1. Email analysis")
        print("2. Name OSINT")
        print("3. Social-account search")
        print("4. IP information")
        print("5. Passive domain recon (theHarvester-style)")
        print("0. Exit")

        choice = input("\ncyberedu> ").strip()

        try:
            if choice == "1":
                email = input("Email: ").strip()
                print_json(analyze_email(email))

            elif choice == "2":
                name = input("Name: ").strip()
                for item in name_searches(name):
                    print(f"- {item['label']}: {item['url']}")

            elif choice == "3":
                email = input("Email or username: ").strip()
                for item in social_searches(email):
                    print(f"- {item['platform']}: {item['url']}")
                print("\nThese are public search links only; manually verify results.")

            elif choice == "4":
                ip = input("Public IP address: ").strip()
                print("Looking up IP information...")
                print_json(lookup_ip(ip))

            elif choice == "5":
                domain = input("Domain you own/are authorized to assess: ").strip()
                print("Running passive DNS/CT lookups...")
                print_json(passive_domain_recon(domain))

            elif choice == "0":
                print("Bye.")
                break

            else:
                print("Invalid choice.")

        except KeyboardInterrupt:
            print("\nCancelled.")
        except Exception as exc:
            print(f"Error: {exc}")
