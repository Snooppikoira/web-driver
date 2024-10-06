from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from colorama import Fore, Style, init

init(autoreset=True)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    while True:
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Entering website: https://github.com/Snooppikoira")
        
        driver.get("https://github.com/Snooppikoira")
        time.sleep(1)
        
        print(f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}] Refreshing page...")
        
        driver.refresh()
        time.sleep(1)
finally:
    print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Closing program & thread...")
    driver.quit()
