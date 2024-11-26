import requests, sys, os
from colorama import Fore, init
from multiprocessing.dummy import Pool as ThreadPool

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

init(autoreset=True)

try:
    os.mkdir("cms")
except:
    pass

class CheckCMS:
    def __init__(self, domain):
        self.domain = domain
        self.url = "https://" + domain
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }
        self.timeout = 15
    
    def Logs(self, args):
        sys.stdout.write(f"\n{args}")
    
    def Scan(self):
        try:
            cek = requests.get(self.url, timeout=self.timeout, headers=self.headers, verify=False).text
            
            # Joomla
            if 'content="Joomla!' in cek or 'Joomla' in cek or 'index.php?option=com_' in cek or '/media/system/js/' in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Joomla{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/joomla.txt", "a").write(self.domain + "\n")
            # WordPress
            elif 'wp-content' in cek or 'WordPress' in cek or 'wp-includes' in cek or '?ver=' in cek or 'wp-json' in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}WordPress{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/wordpress.txt", "a").write(self.domain + "\n")
            
            # SilverStripe
            elif 'SilverStripe' in cek or 'Security/login' in cek or 'cms/' in cek or 'framework/' in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}SilverStripe{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/silverstripe.txt", "a").write(self.domain + "\n")
            
            # Drupal
            elif 'Drupal' in cek or 'X-Generator' in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Drupal{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/drupal.txt", "a").write(self.domain + "\n")
            
            # Typo3
            elif 'typo3' in cek.lower():
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Typo3{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/typo3.txt", "a").write(self.domain + "\n")
            
            # AEM
            elif 'AEM' in cek or 'Adobe Experience Manager' in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}AEM{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/aem.txt", "a").write(self.domain + "\n")
            
            # vBulletin
            elif 'vBulletin' in cek or 'vBSEO' in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}vBulletin{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/vBulletin.txt", "a").write(self.domain + "\n")
            
            # Moodle
            elif 'Moodle' in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}MOodle{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/moodle.txt", "a").write(self.domain + "\n")
            
            # osEcommerce
            elif 'osCommerce' in cek or 'oscommerce' in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}osEcommerce{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/osEcommerce.txt", "a").write(self.domain + "\n")
            
            # ColdFusion
            elif 'ColdFusion' in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}ColdFusion{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/coldfusion.txt", "a").write(self.domain + "\n")
            
            # JBoss
            elif "JBoss" in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}JBoss{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/jboss.txt", "a").write(self.domain + "\n")
            
            # Oracle E-Business
            elif 'Oracle E-Business' in cek or 'Oracle' in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Oracle{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/oracle.txt", "a").write(self.domain + "\n")
            
            # phpBB
            elif "phpBB" in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}phpBB{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/phpBB.txt", "a").write(self.domain + "\n")
            
            # php-nuke
            elif 'PHP-Nuke' in cek or 'phpnuke' in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Php-Nuke{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/php-nuke.txt", "a").write(self.domain + "\n")
            
            # DotNetNuke
            elif "DotNetNuke" in cek or "DNN" in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}DotNetNuke{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/dotnetnuke.txt", "a").write(self.domain + "\n")
            
            # Umbraco
            elif "Umbraco" in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Umbraco{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/umbraco.txt", "a").write(self.domain + "\n")
            
            # PrestaShop
            elif "PrestaShop" in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}PrestaShop{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/prestashop.txt", "a").write(self.domain + "\n")
            
            # OpenCart
            elif "OpenCart" in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}OpenCart{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/opencart.txt", "a").write(self.domain + "\n")
            
            # Magento
            elif "Magento" in cek:
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Magento{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
                open("cms/magento.txt", "a").write(self.domain + "\n")
            else:
                open("cms/unknown.txt", "a").write(self.domain + "\n")
                self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}UNKNOWN{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")
        except:
            self.Logs(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}ERROR{Fore.LIGHTCYAN_EX}] {Fore.WHITE}-- {self.domain}")

def Runner(domain):
    try:
        CheckCMS(domain).Scan()
    except:
        pass

def Banner():
    os.system("cls" if os.name == "nt" else "clear")
    __banner__ = f"""  {Fore.LIGHTRED_EX}┏┓┏┓      ┏┓┳┳┓┏┓
   ┃┃   ━━  ┃ ┃┃┃┗┓
  ┗┛┗┛      ┗┛┛ ┗┗┛ {Fore.WHITE}CMS - Scanner
"""
    print(__banner__)

if __name__ == "__main__":
    Banner()
    input_list = [j.strip("\r\n") for j in open(input(f"{Fore.WHITE} Domain List : "), "r", encoding="ISO-8859-1").readlines()]
    Thread = input(f"{Fore.WHITE} Thread : ")
    pool = ThreadPool(int(Thread))
    pool.map(Runner, input_list)
    pool.close()
    pool.join()
