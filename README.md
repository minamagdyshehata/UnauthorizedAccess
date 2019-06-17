# UnauthorizedAccess
# **Get notified when an unauthorized person tries to access your computer behind your back!**

**NOTE: {This Script is written for Windows machines!}**


*Disclaimer:*

   *-It's illegal to monitor others' computers.*
   *-Any misuse of this project is completely prohibited*
    *and will result in legal consequences to the identified user.*
   *-To be used under your own responsibility.*

This script will run everytime you start your computer and wait for a termination password for 90 seconds (No prompt for the password, just type it on your keyboard!!). If the the correct password is provided, your will hear 2 beeps indicating that and the script will terminate.

If the password is not provided :

    -- A Log file will be created with a timestamp of the unauthorized access.
    -- If a webcam exist a snapshot will be taken.
       {Special Thanks to: https://github.com/tedburke/CommandCam, for making this possible.}
        ** Both the Log file and the snapshot will be saved in the same directory of the script.
    -- If there is an Internet Connection a Notification Email will be sent with the name
       of the machine and the snapshot taken.
    

How to Configure the script:

    01- Make sure Pathon3 is installed on your machine. 
        If not please go to https://www.python.org/, download and install.
    02- Right Click on "This PC" ===> "Properties" ===> "Advanced System Settings" ===> "Environment Variables".
    03- In User Variables (Top part), Double click on "Path".
    04- Make sure the following 2 paths are there, if not click on "New" and add them:
            %USERPROFILE%\AppData\Local\Programs\Python\Python37\
            %USERPROFILE%\AppData\Local\Programs\Python\Python37\Scripts\
    05- Download the project zipped folder and unzip it from:
            https://github.com/minamagdyshehata/UnauthorizedAccess/archive/master.zip
    06- Creat a new GMAIL email and configure it to allow less secured apps by setting this option to "ON" from:
            https://myaccount.google.com/lesssecureapps?utm_source=google-account&utm_medium=web
    07- Go to the Unzipped project directory and run "SetupAndConfigureUA.py" and enter the following:
            a. Your GMAIL (the one configured to allow less secured apps).
            b. Your GMAIL password.
            c. The EMAIL where you want to recieve your Notifications.
            d. Choose Mode:
                    + Protection Mode: Will force Shutdown the machine after sending the Notification Email.
                    + Monitor Mode: You will just get the Notification Email.
            e. Choose to let the script notify you with 1 beep everytime it starts or not.
    08- "ConfiguredUA.pyw" will be created. Run "CreatEXE.bat" to creat the .exe file. when the batch file terminates, 
        you will find your "ConfiguredUA.exe" in "dist" folder.
        You must delete "ConfiguredUA.pyw" as your password is written inside in plain text!
    09- Hide "ConfiguredUA.exe" anywhere in your machine and rename it.
    10- Double click on the renamed .exe file, give it few seconds to download "CommandCam.exe".
        Then type your termination password (you will hear 2 beeps when correct password is entered).
        Now the script will run everytime your machine is turned on.
    11- If you want the script to run also everytime you unlock your machine follow the instructions on:
            https://superuser.com/questions/615114/how-to-make-a-window-task-run-everytime-i-enter-my-password-unlock-the-computer
    12- Notes: 
                    ** If a wrong key is pressed while entering the password you can wait 3 seconds 
                       then start entering the termination password from the begining 
                       OR 
                       press "ENTER" then start typing the password again.
                    ** For the first time you recieve a Notification Email you might need 
                       to check your Spam or Junk E-mail and configure your email that this is 
                       not spam so that you can recieve it in your inbox.
                    ** For the first time a Notification Email is sent from a certain machine, 
                       GMAIL will send you an email asking if that was you on that computer.
                       You must confirm that it is you.
                    ** If you want to remove the script do the following:
                            1. Delete the Task Scheduler entry of the .exe if exist.
                            2. Delete the .exe file and all the files it created (CommandCam.exe,Log.txt,snapshots).
                            3. Press "Start+R", type "regedit" and press "ENTER".
                            5. Navigate to "Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run",
                               then delete the entry for your renamed .exe file.
                               
                               
