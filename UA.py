import sys,platform
Configured = False
if platform.system() != "Windows":
    print("This Script is written for Windows only..")
    if sys.version_info[0] == 2: Terminate = raw_input("Please Press Enter to Exit..")
    if sys.version_info[0] >= 3: Terminate = input("Please Press Enter to Exit..")   
    exit()
if sys.version_info[0] == 2:
    print("Python3 must be installed for this script to work!!")
    Terminate = raw_input("Please Press Enter to Exit..")
    exit()
if Configured == False:
    print("Please Configure the script first!!")
    Terminate = input("Please Press Enter to Exit..")
    exit()

from pynput import keyboard
from win32api import GetKeyState 
from win32con import * 
import winreg,os,subprocess,winsound,socket,datetime,threading,yagmail

delay_ok_t1_PASSWORD_LISTNER ="0"
auth=""
capson = 0
shiftpressed = 0
controlpressed = 0
altpressed = 0
scriptname =  os.path.basename(sys.argv[0])
Notification_Timer_on = False

def Register():
    global scriptname
    scriptfullpath = sys.argv[0]
    for i in range (len(scriptname)-1,-1,-1):
        if scriptname[i]==".":
            extension=scriptname[i:len(scriptname)]
            break
    RUN_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"
    keyCURRENTRUN = winreg.CreateKey(winreg.HKEY_CURRENT_USER, RUN_PATH)
    keyCURRENTRUN = winreg.OpenKey(winreg.HKEY_CURRENT_USER, RUN_PATH, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(keyCURRENTRUN, scriptname, 0, winreg.REG_SZ, scriptfullpath)
    winreg.CloseKey(keyCURRENTRUN)

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def GET_TIME_FORMATTED(timestamp):
    timeformatted = ""
    for x in range(0,len(timestamp)):
        if timestamp[x] == " ":
            timeformatted += "--"
        elif timestamp[x] == ":":
            timeformatted += "."
        else:
            timeformatted += timestamp[x]
    return timeformatted

def SendNotification():
    TimeStamp = str(datetime.datetime.now())
    TimeStampFormatted = GET_TIME_FORMATTED(TimeStamp)
    machinename = os.environ['COMPUTERNAME']
    Log = open(machinename +"Log.txt", "a")
    Log.write("Unauthorized Access on " + TimeStamp + chr(10))
    Log.close()
    try:
        if os.path.isfile("CommandCam.exe"):
            subprocess.call("CommandCam.exe /filename " + TimeStampFormatted + ".jpg",shell=True)
    except:
        pass
    online = is_connected()
    if online:
        try:
            if not os.path.isfile("CommandCam.exe"):
                subprocess.call("powershell (new-object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/minamagdyshehata/UnauthorizedAccess/master/CommandCam.exe','CommandCam.exe')",shell=True)
                subprocess.call("CommandCam.exe /filename " + TimeStampFormatted + ".jpg",shell=True)
        except:
            pass
        try:
            email = "SENDFROMEMAIL"
            password = "FROMPASSWORD"
            send_to_email = "SENDTOEMAIL"
            message = "There was an unauthorized access on one of your machines with the name '" + machinename + "'"
            subject = "Unauthorized Access"
            yag=yagmail.SMTP(email,password)
            if os.path.isfile(TimeStampFormatted + ".jpg"):
                attach = TimeStampFormatted + ".jpg"
                yag.send(to=send_to_email,subject=subject,contents=message,attachments=attach,)
            else:
                yag.send(to=send_to_email,subject=subject,contents=message,)
        except:
            pass
    subprocess.call("rundll32.exe user32.dll,LockWorkStation",shell=True)
    Terminate()

def delay_happened_t1_PASSWORD_LISTNER (arg):
    if arg=="1":
        global delay_ok_t1_PASSWORD_LISTNER
        global auth
        auth=""
        delay_ok_t1_PASSWORD_LISTNER="0"
t1_PASSWORD_LISTNER = threading.Timer(3,delay_happened_t1_PASSWORD_LISTNER,[delay_ok_t1_PASSWORD_LISTNER])

def start_delay_t1_PASSWORD_LISTNER():
    global delay_ok_t1_PASSWORD_LISTNER
    global t1_PASSWORD_LISTNER
    delay_ok_t1_PASSWORD_LISTNER= "1"
    t1_PASSWORD_LISTNER = threading.Timer(3,delay_happened_t1_PASSWORD_LISTNER,[delay_ok_t1_PASSWORD_LISTNER]) 
    t1_PASSWORD_LISTNER.start()

def on_press(key):
    global delay_ok_t1_PASSWORD_LISTNER
    global t1_PASSWORD_LISTNER
    global auth
    global shiftpressed
    global controlpressed 
    global altpressed
    global Notification_Timer_on
    global Notification_Timer_on_Lock
    shiftpressed = (GetKeyState(VK_LSHIFT) + GetKeyState(VK_RSHIFT))/2
    controlpressed = (GetKeyState(VK_LCONTROL) + GetKeyState(VK_RCONTROL))/2
    altpressed = (GetKeyState(VK_LMENU)+ GetKeyState(VK_RMENU))/2
    if delay_ok_t1_PASSWORD_LISTNER=="1":
            t1_PASSWORD_LISTNER.cancel()
    if len(str(key))==3:
        auth+=str(key)[1]
        if auth == "12345" and Notification_Timer_on:
            t2_SENDING_NOTIFICATION.cancel()
            Notification_Timer_on = False
            winsound.Beep(300,100)
            winsound.Beep(300,100)
            Terminate()
        start_delay_t1_PASSWORD_LISTNER()
    elif len(str(key))>3 and str(key)[:3]=="Key":
            pressedkey = (str(key))[4:len(str(key))]
            if pressedkey=="space":
                auth+=" "
                start_delay_t1_PASSWORD_LISTNER()    
            elif pressedkey=="enter":
                auth=""

def on_release(key):
    global capson
    global shiftpressed
    global controlpressed 
    global altpressed
    capson = GetKeyState(VK_CAPITAL)
    shiftpressed=(GetKeyState(VK_LSHIFT)+GetKeyState(VK_RSHIFT))/2
    controlpressed=(GetKeyState(VK_LCONTROL)+GetKeyState(VK_RCONTROL))/2
    altpressed=(GetKeyState(VK_LMENU)+GetKeyState(VK_RMENU))/2

def Terminate():
    scriptname = os.path.basename(sys.argv[0])
    if scriptname.endswith(".pyw"):
        subprocess.call("taskkill /F /IM pyw.exe",shell=True)
    elif scriptname.endswith(".py"):
        subprocess.call("taskkill /F /IM py.exe",shell=True)
    else:
        subprocess.call("taskkill /F /IM " + scriptname,shell=True)

t2_SENDING_NOTIFICATION = threading.Timer(90,SendNotification)
t2_SENDING_NOTIFICATION.start()
Notification_Timer_on = True
winsound.Beep(300,100)
Register()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
