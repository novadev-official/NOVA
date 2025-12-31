import argparse
from banner import show_banner
from modules.username import username_osint
from modules.ip_lookup import ip_lookup
from modules.domain import domain_osint

def main():
    show_banner()

    parser = argparse.ArgumentParser(description="NOVAI OSINT Tool")
    parser.add_argument("-u", "--username", help="Username OSINT")
    parser.add_argument("-i", "--ip", help="IP address OSINT")
    parser.add_argument("-d", "--domain", help="Domain OSINT")

    args = parser.parse_args()

    if args.username:
        username_osint(args.username)
    elif args.ip:
        ip_lookup(args.ip)
    elif args.domain:
        domain_osint(args.domain)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
