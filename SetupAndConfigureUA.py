import sys,platform
if platform.system() != "Windows":
    print("This Script is written for Windows only..")
    if sys.version_info[0] == 2: Terminate = raw_input("Please Press Enter to Exit..")
    if sys.version_info[0] >= 3: Terminate = input("Please Press Enter to Exit..")   
    exit()
if sys.version_info[0] == 2:
    print("Python3 must be installed for this script to work!!")
    Terminate = raw_input("Please Press Enter to Exit..")
    exit()
    
import os,socket,datetime

red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def GET_TIME_FORMATTED():
    time = str(datetime.datetime.now())
    timeformatted = ""
    for x in range(0,len(time)):
        if time[x] == " ":
            timeformatted += "--"
        elif time[x] == ":":
            timeformatted += "."
        else:
            timeformatted += time[x]
    return timeformatted

online = is_connected()
if online == True:
    os.system("python -m pip install --upgrade pip")
    os.system("pip install pynput")
    os.system("pip install pypiwin32")
    os.system("pip install yagmail")
    os.system("pip install pyinstaller")
    if not os.path.isfile("UA.py"):
        os.system("powershell (new-object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/minamagdyshehata/UnauthorizedAccess/master/UA.py','UA.py')")
    else:
        lines = open("UA.py").readlines()
        if len(lines)== 186:
            print(green(chr(10) + "The correct UA.py file was found" + chr(10)))
        else:
            print (red(chr(10) + "Corrupted UA.py file was found. The correct file will be downloaded.." + chr(10)))
            time_now = GET_TIME_FORMATTED()
            os.rename("UA.py",time_now + "CorruptedUA.py")
            os.system("powershell (new-object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/minamagdyshehata/UnauthorizedAccess/master/UA.py','UA.py')")
else:
    print("Please check your Internet Connection then run this script again!")
    Terminate = input("Please Press Enter to Exit..")
    exit()
if not os.path.isfile("UA.py"):
    print("Failed to download a fresh copy of UA.py!")
    print("Please download UA.py manualy from:")
    print("https://github.com/minamagdyshehata/UnauthorizedAccess")
    print("Then run this script again!")
    Terminate = input("Please Press Enter to Exit..")
    exit()
        
print(red(chr(10) + "ALL DATA YOU ARE ABOUT TO ENTER WONT BE CHECKED FOR MISTAKES..."))
print(red("PLEASE BE CARFUL..." + chr(10)))
print(green("Incase of any mistakes, just restart SetupAndConfigureUA.py" + chr(10)))
      
GMAIL_LSA = input(green("Please enter your Gmail (configured to allow Less secure app access): "))
if GMAIL_LSA == "": print(red("KEPT UNCONFIGURED!!"))
GMAIL_LSA_PASS = input(green("Please enter your Gmail password: "))
if GMAIL_LSA_PASS == "": print(red("KEPT UNCONFIGURED!!"))
NOFITY_EMAIL = input (green("Please enter the Email address where notifications will be sent to: "))
if NOFITY_EMAIL == "": print(red("KEPT UNCONFIGURED!!"))
TERMINATION_PASS = input(green("Please enter your termination password (case sensitive): "))
if TERMINATION_PASS == "": print(red("KEPT UNCONFIGURED!!  ") + green("Default: 12345"))
MODES_SOUND = ["1","2",""]
MODE = input(green("[1]-Protection Mode , [2]-Monitor Mode: "))
while MODE not in MODES_SOUND:
    MODE = input(green("[1]-Protection Mode , [2]-Monitor Mode: "))
if MODE == "":
    MODE = "1"
    print(red("KEPT UNCONFIGURED!!  ") + green("Default: [1]-Protection Mode"))
SOUND = input(green("Sound Notifications: [1]-ON , [2]-OFF: "))
while SOUND not in MODES_SOUND:
    SOUND = input(green("Sound Notifications: [1]-ON , [2]-OFF: "))
if SOUND == "":
    SOUND = "1"
    print(red("KEPT UNCONFIGURED!!  ") + green("Default: Sound Notifications: [1]-ON"))
    
RAWUA = open("UA.py").readlines()
RAWUA[1] = "Configured = True ##Configuration {"
if MODE == "1": RAWUA[1] += "Mode: Protection, "
if MODE == "2": RAWUA[1] += "Mode: Monitor, "
if SOUND == "1": RAWUA[1] += "Sound: ON}"
if SOUND == "2": RAWUA[1] += "Sound: OFF}"
RAWUA[1] += "\n"
if GMAIL_LSA != "": RAWUA[84] = "            email = "+ chr(34) + GMAIL_LSA + chr(34) + "\n"
if GMAIL_LSA_PASS != "": RAWUA[85] = "            password = "+ chr(34) + GMAIL_LSA_PASS + chr(34 )+ "\n"
if NOFITY_EMAIL != "": RAWUA[86] = "            send_to_email = "+ chr(34) + NOFITY_EMAIL + chr(34) + "\n"
if TERMINATION_PASS != "": RAWUA[131] = "        if auth == "+ chr(34) + TERMINATION_PASS + chr(34) + " and Notification_Timer_on:" + "\n"
if MODE == "2":
    RAWUA[97] ="\n"
if SOUND == "2":
    RAWUA[134] ="\n"
    RAWUA[135] ="\n"
    RAWUA[168] ="\n"

Configured_UA=open("ConfiguredUA.pyw","w")
for x in range(0,len(RAWUA)):
    Configured_UA.write(RAWUA[x])
Configured_UA.close()
print(chr(10) + "UA.py is successfully configured as " + green("ConfiguredUA.pyw"))
Terminate = input(red(chr(10) + "Please Press Enter to Exit.."))
exit()
