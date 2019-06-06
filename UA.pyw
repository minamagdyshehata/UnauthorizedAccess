from pynput import keyboard
import winreg, os, sys, subprocess,winsound,socket,smtplib,datetime
from win32api import GetKeyState 
from win32con import *
import threading

delay_ok_t1_PASSWORD_LISTNER ="0"
auth=""
capson = 0
shiftpressed = 0
controlpressed = 0
altpressed = 0
scriptname =  os.path.basename(sys.argv[0])

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

def SendNotification():
    global windrive
    machinename = os.environ['COMPUTERNAME']
    Log = open(machinename +"Log.txt", "a")
    Log.write("Unauthorized Access on " + str(datetime.datetime.now()) + chr(10))
    Log.close()
    online = is_connected()
    while online == False:
        online = is_connected()
    email = "SENDFROMEMAIL"
    password = "FROMPASSWORD"
    send_to_email = "SENDTOEMAIL"
    message = "Subject: Unauthorized Access \nThere was an unauthorized access on one of your machines with the name '" + machinename + "'\n "
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, send_to_email , message)
    server.quit()
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
    shiftpressed = (GetKeyState(VK_LSHIFT) + GetKeyState(VK_RSHIFT))/2
    controlpressed = (GetKeyState(VK_LCONTROL) + GetKeyState(VK_RCONTROL))/2
    altpressed = (GetKeyState(VK_LMENU)+ GetKeyState(VK_RMENU))/2 
    if delay_ok_t1_PASSWORD_LISTNER=="1":
            t1_PASSWORD_LISTNER.cancel()
    if len(str(key))==3:
        auth+=str(key)[1]
        if auth=="TERMINATIONPASSWORD":
            winsound.Beep(2000,100)
            winsound.Beep(2000,100)
            t2_SENDING_NOTIFICATION.cancel()
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
    global scriptname
    if scriptname.endswith(".pyw"):
        subprocess.call("taskkill /F /IM pyw.exe",shell=True)
    elif scriptname.endswith(".py"):
        subprocess.call("taskkill /F /IM py.exe",shell=True)
    else:
        subprocess.call("taskkill /F /IM " + scriptname,shell=True)

t2_SENDING_NOTIFICATION = threading.Timer(120,SendNotification)
t2_SENDING_NOTIFICATION.start()
Register()


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
