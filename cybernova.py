import os
import sys
import time

# Colors for the terminal
class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def banner():
    print(r"""
███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ ██╗
████╗  ██║██╔═══██╗██║   ██║██╔══██╗██║
██╔██╗ ██║██║   ██║██║   ██║███████║██║
██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║██║
██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║██║
╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝
""")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        banner()
        print(f"{Colors.YELLOW}[1]{Colors.END} {Colors.BOLD}INTELLIGENCE & ANALYSIS{Colors.END}")
        print(f"{Colors.YELLOW}[2]{Colors.END} {Colors.BOLD}VULNERABILITY TESTING{Colors.END}")
        print(f"{Colors.YELLOW}[3]{Colors.END} {Colors.BOLD}RED TEAM ARSENAL{Colors.END}")
        print(f"{Colors.YELLOW}[4]{Colors.END} {Colors.BOLD}EMAIL SECURITY SUITE{Colors.END}")
        print(f"{Colors.YELLOW}[5]{Colors.END} {Colors.BOLD}SYSTEM TOOLS & SETTINGS{Colors.END}")
        print(f"{Colors.YELLOW}[0]{Colors.END} {Colors.RED}EXIT{Colors.END}")
        print("\n" + "="*60)
        
        choice = input(f"\n{Colors.GREEN}CYBERNOVA > {Colors.END}")
        
        if choice == '1':
            intelligence_menu()
        elif choice == '2':
            vulnerability_menu()
        elif choice == '3':
            red_team_menu()
        elif choice == '4':
            email_security_menu()
        elif choice == '5':
            print(f"\n{Colors.BLUE}[*] System Tools coming soon...{Colors.END}")
            time.sleep(1)
        elif choice == '0':
            print(f"\n{Colors.RED}[!] Shutting down CYBERNOVA...{Colors.END}")
            sys.exit()
        else:
            print(f"\n{Colors.RED}[!] Invalid Choice{Colors.END}")
            time.sleep(1)

from tools import intel, vuln

def intelligence_menu():
    while True:
        clear_screen()
        banner()
        print(f"{Colors.CYAN}--- INTELLIGENCE & ANALYSIS ---{Colors.END}\n")
        print(f"{Colors.YELLOW}[1]{Colors.END} IP Address Location Finder")
        print(f"{Colors.YELLOW}[2]{Colors.END} Advanced Data Analysis")
        print(f"{Colors.YELLOW}[3]{Colors.END} Email Validator")
        print(f"{Colors.YELLOW}[0]{Colors.END} BACK")
        
        choice = input(f"\n{Colors.GREEN}CYBERNOVA/INTEL > {Colors.END}")
        if choice == '1':
            ip = input(f"{Colors.BLUE}[?] Enter IP to trace: {Colors.END}")
            result = intel.get_ip_location(ip)
            print(f"{Colors.GREEN}[+] Result: {result}{Colors.END}")
            input("\nPress Enter to continue...")
        elif choice == '3':
            email = input(f"{Colors.BLUE}[?] Enter Email to validate: {Colors.END}")
            valid = intel.validate_email(email)
            if valid:
                print(f"{Colors.GREEN}[+] Email looks valid.{Colors.END}")
            else:
                print(f"{Colors.RED}[-] Invalid email format.{Colors.END}")
            input("\nPress Enter to continue...")
        elif choice == '0': break
        else: 
            print(f"\n{Colors.BLUE}[*] Module starting... (Stub){Colors.END}")
            time.sleep(1)

def vulnerability_menu():
    while True:
        clear_screen()
        banner()
        print(f"{Colors.CYAN}--- VULNERABILITY TESTING ---{Colors.END}\n")
        print(f"{Colors.YELLOW}[1]{Colors.END} SQL Injection Scanner")
        print(f"{Colors.YELLOW}[2]{Colors.END} XSS Scanner")
        print(f"{Colors.YELLOW}[3]{Colors.END} LFI/RFI Scanner")
        print(f"{Colors.YELLOW}[4]{Colors.END} OS Command Injection Detector")
        print(f"{Colors.YELLOW}[0]{Colors.END} BACK")
        
        choice = input(f"\n{Colors.GREEN}CYBERNOVA/VULN > {Colors.END}")
        if choice == '1':
            url = input(f"{Colors.BLUE}[?] Enter URL to scan for SQLi: {Colors.END}")
            vuln.scan_sqli(url)
            input("\nPress Enter to continue...")
        elif choice == '2':
            url = input(f"{Colors.BLUE}[?] Enter URL to scan for XSS: {Colors.END}")
            vuln.scan_xss(url)
            input("\nPress Enter to continue...")
        elif choice == '0': break
        else: 
            print(f"\n{Colors.BLUE}[*] Module starting... (Stub){Colors.END}")
            time.sleep(1)

def red_team_menu():
    while True:
        clear_screen()
        banner()
        print(f"{Colors.CYAN}--- RED TEAM ARSENAL ---{Colors.END}\n")
        print(f"{Colors.YELLOW}[1]{Colors.END} Advanced SQL Injection Tester")
        print(f"{Colors.YELLOW}[2]{Colors.END} Intelligent XSS Scanner")
        print(f"{Colors.YELLOW}[3]{Colors.END} Custom Payload Generator")
        print(f"{Colors.YELLOW}[4]{Colors.END} Advanced Port Scanner")
        print(f"{Colors.YELLOW}[0]{Colors.END} BACK")
        
        choice = input(f"\n{Colors.GREEN}CYBERNOVA/REDTEAM > {Colors.END}")
        if choice == '1':
            url = input(f"{Colors.BLUE}[?] Enter URL to test for advanced SQLi: {Colors.END}")
            vuln.advanced_sqli_tester(url)
            input("\nPress Enter to continue...")
        elif choice == '2':
            url = input(f"{Colors.BLUE}[?] Enter URL to scan for intelligent XSS: {Colors.END}")
            vuln.intelligent_xss_scanner(url)
            input("\nPress Enter to continue...")
        elif choice == '3':
            vuln.custom_payload_generator()
            input("\nPress Enter to continue...")
        elif choice == '4':
            target = input(f"{Colors.BLUE}[?] Enter target IP/domain for port scan: {Colors.END}")
            vuln.advanced_port_scanner(target)
            input("\nPress Enter to continue...")
        elif choice == '0': break
        else: 
            print(f"\n{Colors.BLUE}[*] Invalid option.{Colors.END}")
            time.sleep(1)

def email_security_menu():
    while True:
        clear_screen()
        banner()
        print(f"{Colors.CYAN}--- EMAIL SECURITY SUITE ---{Colors.END}\n")
        print(f"{Colors.YELLOW}[1]{Colors.END} Mail Configuration Analyzer")
        print(f"{Colors.YELLOW}[2]{Colors.END} SPF Checker")
        print(f"{Colors.YELLOW}[3]{Colors.END} DKIM Validator")
        print(f"{Colors.YELLOW}[4]{Colors.END} DMARC Analyzer")
        print(f"{Colors.YELLOW}[0]{Colors.END} BACK")
        
        choice = input(f"\n{Colors.GREEN}CYBERNOVA/EMAIL > {Colors.END}")
        if choice == '0': break
        else: 
            print(f"\n{Colors.BLUE}[*] Module starting... (Stub){Colors.END}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[!] Exit requested by user.{Colors.END}")
        sys.exit()
