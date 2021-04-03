import bs4
import requests
from mercurial.util import cookielib

logo='''
\033[1;33;40m.---.               .    `.---                 
\___  . , , ,-. ,-. |-    |__  ,-. ,-. ,-. ,-. 
    \ |/|/  |-' |-' |    ,|    |   |   | | |   
`---' ' '   `-' `-' `'   `^--- '   '   `-' ' 
\t\t \033[1;33;40mAn Error is a Sweet Taste
\033[1;32;40m\n▌│█║▌║▌║ \033[1;31;40m█▓▒░░ \033[1;34;40mMubeen Ahmad \033[1;31;40m░░▒▓█\033[1;32;40m ║▌║▌║█│▌\n\t-: Contact me on Facebook :-\n     \033[1;36;40mhttps://m.facebook.com/sweeterror404\033[1;32;40m\n\t-: my Github Account :- \n     \033[1;36;40mhttps://github.com/Sweeterror404\n\t\033[1;32;40m-: Join Facebook Group :-\n  \033[1;36;40mhttps://m.facebook.com/groups/sweeterror404
'''
print(logo)
print("\033[1;32;40mPlease Add facebook Cookies ")
print("\033[1;32;40mWarning Don't Log out from Browser")
def cookies():
    c_user = input("\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Enter c_user value :- ")
    datr = input("\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Enter datr value :- ")
    fr = input("\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Enter fr value :- ")
    sb = input("\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Enter sb :- ")
    xs = input("\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Enter xs :- ")

    cookies = f'''# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.facebook.com	TRUE	/	TRUE	1644072814	c_user	{c_user}
.facebook.com	TRUE	/	TRUE	1675608817	datr	{datr}
.facebook.com	TRUE	/	TRUE	1620312811	fr	{fr}
.facebook.com	TRUE	/	TRUE	1675608817	sb	{sb}
.facebook.com	TRUE	/	TRUE	1644072814	xs	{xs}
'''
    with open("cookies.txt", "w") as w:
        w.write(cookies)

# Load cookies
cj = cookielib.MozillaCookieJar("cookies.txt")
cj.load()
print("\033[1;32;40mPlease Wait\n")
# searcher function
def searcher(link):
    header = {
        "Accept-Language": "en-US,en;q=0.5",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'}
    data = requests.get(link, cookies=cj, headers=header)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    return soup

# extract links
confirm = []
delete = []

def Extract_LINKS():
    url = ["https://mbasic.facebook.com/friends/center/requests/#friends_center_main"]
    for links in url:
        for i in searcher(links).find_all('a'):
            lk = str(i.get("href"))
            if lk.find("/friends/center/requests/?") != -1:
                url.append("https://mbasic.facebook.com/"+lk)

    # extract friends
    for extract_links in url:
        for i in searcher(extract_links).find_all("a"):
            lk = str(i.get("href"))
            # confirm
            if lk.find("/a/notifications.php?confirm=") != -1:
                confirm.append("https://mbasic.facebook.com/"+lk)

            # delete
            if lk.find("/a/notifications.php?delete=") != -1:
                delete.append("https://mbasic.facebook.com/"+lk)

Extract_LINKS()
print(f"\nTotal {len(confirm)} Friends")
while True:
    user_input = input("\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Press C for Confirm\n\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Press D for Delete ").lower()
    if user_input == "c":
        count = len(confirm)
        for pos,i in enumerate(confirm):
            searcher(i)
            print(f"\n\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Confirm {pos+1}\n\t{count-1} are left")
            count -= 1
        if count == 0:
            print("All Friends Requests are Accpeted Sucessfully ")
            break

    elif user_input == "d":
        count = len(confirm)
        for pos,i in enumerate(confirm):
            searcher(i)
            print(f"\n\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Deleted {pos+1}\n\t{count - 1} are left")
            count -= 1
        if count == 0:
            print("All Friends Requests are Deleted Sucessfully ")
        break

    elif user_input != "c" or user_input != "d":
        print("\033[1;32;40mWrong input !")