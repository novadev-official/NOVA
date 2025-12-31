import socket
from urllib.parse import urlparse
from colorama import Fore

def domain_osint(domain):
    print(Fore.CYAN + f"\n[+] Domain OSINT for: {domain}\n")

    # allow passing full URLs (with scheme/path) or plain hostnames
    parsed = urlparse(domain if '://' in domain else '//' + domain)
    host = parsed.hostname if parsed.hostname else domain

    if not host:
        print(Fore.RED + "Invalid domain/URL")
        return

    try:
        # try to get canonical name and alias list
        try:
            cname, aliases, ip_list = socket.gethostbyname_ex(host)
        except Exception:
            cname, aliases, ip_list = host, [], []

        if cname:
            print(Fore.GREEN + f"Hostname: {cname}")
        if aliases:
            print(f"Aliases : {', '.join(aliases)}")

        # collect all addresses via getaddrinfo (handles IPv4/IPv6)
        addrs = set()
        try:
            for res in socket.getaddrinfo(host, None):
                addr = res[4][0]
                addrs.add(addr)
        except Exception:
            pass

        if addrs:
            print(Fore.GREEN + "IP Addresses:")
            for a in sorted(addrs):
                print(f"  - {a}")
        elif ip_list:
            print(Fore.GREEN + "IP Addresses:")
            for a in ip_list:
                print(f"  - {a}")
        else:
            print(Fore.RED + "No IP addresses found")
    except Exception:
        print(Fore.RED + "Unable to resolve domain")
