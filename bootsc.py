import sys
import time
def finalstageboot():
    print("SMs Verified!")
    name = input(f"{tcolors.OKGREEN}Welcome, {NM}! What is your name?\n")
    print(f"{tcolors.OKGREEN}Hello there, {name}!")
    time.sleep(1)
    print("Booting... Please Wait...")
    exec(open("menu.py").read())


def boot():
    print(f"{tcolors.WARNING}Reminder: If you recieve an error saying 'name ver is not defined' it means you have launched McCMD from the bootsc.py\nfile instead of main.py and you need to reboot the program.")
    time.sleep(2)
    print(f"{tcolors.OKBLUE}Verification will start shortly.. Please wait...")
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
            finalstageboot()
        if sm != "y":
            print(f"{tcolors.FAIL}SMs (System Messages) are disabled! This will also disable the Command Prompt.")
            smcon = input("Continue? [y/n]")
            if smcon == "y":
                sys.exit(
                    "Uh oh! McCMD has encountered an error! \n\nDev Reason: Disabling SMs is not allowed in Version 1.1, please restart the program with SMs enabled.")
            else:
                sys.exit(
                    "User had chosen to end the program. You may ignore this error.")
    else:
        sys.exit("Uh oh! McCMD has encountered an error! Invalid Variable! \n\nDev Reason: Head into Main.py and set ver to y.")
    exec(open("menu.py").read())
def DBboot():
    print("WARNING: IF YOU REALLY DID LAUNCH THE APP FROM BOOTSC.PY WE HIGHLY RECCOMMEND ENDING AND RERUNNING THE\nPROGRAM, AS VERIFICATION WILL BE SKIPPING CAUSING MULTIPLE ERRORS.YOU ARE ABLE TO SAFELY CONTINUE IF YOU WOULD LIKE, BUT IT IS RECOMMENDED YOU KNOW WHAT YOU ARE DOING.")
    DB = input("Are you sure you want to continue? [y/n]")
    if DB == "y":
        print("Continuing without Verification... Please wait...")
        time.sleep(2)
        finalstageboot()
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
multichoice = input(f"{tcolors.OKBLUE}McCMD Boot Wizard:\n\n1. Boot menu.py (The App)\n2. Skip Verification (Lauched from Bootsc.py)\n\nYour Choice: ")
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
else:
    sys.exit("Uh oh! McCMD has encountered an error! McCMD Boot Wizard could not interpret the provided variable correctly. \n\nDev Reason: An invalid prase was given in the McCMD Boot Wizard, likely an invalid choice when told to select a way to boot.")
