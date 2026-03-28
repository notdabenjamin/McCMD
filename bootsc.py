import sys
import time

def boot():
    print("Reminder: If you recieve an error saying 'name ver is not defined' it means you have launched McCMD from the boot.sc\nfile instead of main.py and you need to reboot the program.")
    time.sleep(2)
    print("Verification will start shortly.. Please wait...")
    time.sleep(2)
    print("Verification has started!")
    time.sleep(1)
    print(f"Debug: ver = {ver}")
    time.sleep(1)
    if ver == "y":
        print("1SV has completed!")
        time.sleep(.5)
        print("Checking for SMs...")
        time.sleep(1)
        if sm == "y":
            print("System: SMs are enabled!")
        if sm != "y":
            print("SMs (System Messages are disabled)! This will also disable the Command Prompt on the menu and is NOT reccomended.")
            smcon = input("Continue? [y/n]")
            if smcon == "y":
                sys.exit(
                    "Uh oh! McCMD has encountered an error! \n\nDev Reason: Disabling SMs is not allowed in Version 1.1, please restart the program with SMs enabled.")
    else:
        sys.exit("Uh oh! McCMD has encountered an error! Invalid Variable! \n\nDev Reason: Head into Main.py and set ver to y.")
    exec(open("sel.py").read())
def DBboot():
    print("WARNING: IF YOU REALLY DID LAUNCH THE APP FROM BOOTSC.PY WE HIGHLY RECCOMMEND ENDING AND RERUNNING THE PROGRAM, AS VERIFICATION WILL BE SKIPPING CAUSING MULTIPLE ERRORS. YOU ARE ABLE TO SAFELY CONTINUE IF YOU WOULD LIKE, BUT IT IS RECOMMENDED YOU KNOW WHAT YOU ARE DOING.")
    DB = input("Are you sure you want to continue? [y/n]")
    if DB == "y":
        print("Continuing without Verification... Please wait...")
        time.sleep(2)
        exec(open("sel.py").read())
    if DB != "n":
        sys.exit("User had chosen to end the program. You may ignore this error.")
print("Testing... Testing...")
time.sleep(1) # Preventing the error to occur without anything happening.
tst = "Hello World"
if tst != "Hello World":
    sys.exit(
        "Uh oh! McCMD has encountered an error! We were unable to launch bootsc.py {DO NOT ATTEMPT TO LAUNCH IT MANUALLY} \n\nDev Reason: bootsc.py test has failed, the tst var check was unable to work, this was likely caused by change of code.")
print(tst)
time.sleep(1)
print("Test Completed Successfully! Welcome, User!")
multichoice = input("McCMD Boot Wizard:\n\n1. Boot Sel.py (The App)\n2. Skip Verification (Lauched from Bootsc.py)\n\nYour Choice: ")
if multichoice == "1":
    print("McCMD will boot shortly, please wait...")
    time.sleep(3)
    print("Preparing to start Verification and Boot...")
    time.sleep(1)
    print("Booting... Please stand-by!")
    time.sleep(1)
    boot()
if multichoice == "2":
    DBboot()

exec(open("sel.py").read())