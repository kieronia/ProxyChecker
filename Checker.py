
import time , requests , threading , os
from colorama import init, Fore, Back, Style

init(convert=True)

filepath = 'proxies.txt'

invalid = int(0)
valid = int(0)




def my_function(line):
    global valid
    global invalid
    try:
        print(f"{Fore.WHITE}[{Fore.CYAN}!{Fore.WHITE}] {Fore.CYAN}Checking {line.strip()}")
        proxy = line
        proxies = {'https': 'https://%s' % (proxy)}
        requests.get(site, proxies = proxies)
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}{proxy.strip()} - Valid")
        f = open("valid.txt", 'a')
        f.write(f"{proxy.strip()} \n")
        f.close()
        valid = valid + 1
        os.system(f"title Checking Proxies - [Valid : {valid}] [Invalid {invalid}]")
    except:
        print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] {Fore.RED}{proxy.strip()} - Invalid")
        invalid = invalid + 1
        os.system(f"title Checking Proxies - [Valid : {valid}] [Invalid {invalid}]")

os.system(f"title Checking Proxies - [Valid : {valid}] [Invalid {invalid}]")


site = input(f"{Fore.WHITE}[{Fore.CYAN}!{Fore.WHITE}] {Fore.CYAN}URL To Validate Proxies On?\n{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] {Fore.GREEN}")
with open(filepath, 'r') as f:
    for line in f.readlines():
        threading.Thread(target = my_function, args = (line,)).start()
        time.sleep(0.05)
    input()
        

        
