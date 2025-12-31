from colorama import Fore, Style

def show_banner():
    print(Fore.CYAN + """
███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ ██╗
████╗  ██║██╔═══██╗██║   ██║██╔══██╗██║
██╔██╗ ██║██║   ██║██║   ██║███████║██║
██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║██║
██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║██
╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═
    """ + Style.RESET_ALL)
    print(Fore.YELLOW + "NOVAI - Open Source Intelligence Tool")
    print(Fore.GREEN + "Author: NOVA Developments\n" + Style.RESET_ALL)
