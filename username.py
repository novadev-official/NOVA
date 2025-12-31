import requests
from colorama import Fore

def username_osint(username):
    sites = {
        "GitHub": "https://github.com/{}",
        "Instagram": "https://www.instagram.com/{}",
        "Twitter": "https://twitter.com/{}",
        "Reddit": "https://www.reddit.com/user/{}"
    }

    print(Fore.CYAN + f"\n[+] Searching username: {username}\n")

    for site, url in sites.items():
        try:
            r = requests.get(url.format(username), timeout=5)
            if r.status_code == 200:
                print(Fore.GREEN + f"[FOUND] {site}: {url.format(username)}")
            else:
                print(Fore.RED + f"[NOT FOUND] {site}")
        except Exception:
            print(Fore.YELLOW + f"[ERROR] {site}")
