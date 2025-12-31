import requests
from colorama import Fore

def ip_lookup(ip):
    print(Fore.CYAN + f"\n[+] IP OSINT for: {ip}\n")

    url = f"http://ip-api.com/json/{ip}"
    try:
        data = requests.get(url, timeout=6).json()
    except Exception:
        print(Fore.RED + "Error querying IP API")
        return

    if data.get("status") == "success":
        print(Fore.GREEN + f"Country : {data.get('country')}")
        print(f"City    : {data.get('city')}")
        print(f"ISP     : {data.get('isp')}")
        print(f"Org     : {data.get('org')}")
        print(f"ASN     : {data.get('as')}")
    else:
        print(Fore.RED + "Invalid IP or API error")
