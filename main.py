# When booting McCMD please make sure you boot this file (Main.py) before anything else,
# this file is used to import the necessary libraries and verify that everything is working
# correctly.

# McCMD is a joke project meant to test how good python is at creating a coding language
# inside a coding language.

# McCMD is owned by NotDaBenjamin.
# Credit is not required, but appreciated.

# Learn how to use McCMD on the Official GitHub Page

import os
import sys
import time
print("\n" * 100)

# Settings
ver = "y"
sm = "y"
Test = "Yes"

class tcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'  # Resets color and style

freedesc = "\n\nWelcome to Free Code!\nFree Code allows you to write and run code all inside of the file! You can Copy & Paste code you already\nhave instead of needing a text file like in //import, giving new users a way to learn the language!\n\nSettings:\nSMs: Enabled\nAttempted Error Desc: Enabled\nImporting: Disabled\nRecommended: For new users\n\nMcCMDFreeCodev Beta 1.0\nPress enter to head back to the menu:\n"

# Version and Test ID, these are used to identify the version of the program and if the user is running a test, this is used for debugging purposes and to help users know if they are running a test or not. The Test ID is a unique identifier for each test, allowing developers to track and manage different tests effectively.
Version = "BETAv1.0.1"
TestID = "5"

if Test == "Yes":
    print("YOU ARE CURRENTLY RUNNING A TEST, YOUR TEST ID IS: " + TestID + " Stable Version: " + Version)
else:
    print(Version)
yn = input(f"{tcolors.WARNING}WARNING: McCMD is NOT optimized to run on every software, the entire software was made on VS Code and PyCharm and was also\nslightly tested on Windows Command Prompt. We recommend running it on PyCharm or CMD, as VS Code has large amounts\nof bugs. It is reccommended that you use a Non-Web based python compiler, as Web based often have low access to python\nlibraries, which McCMD heavily relies on. We have tried our best to make it compatible with every single software, but it seems like it is impossible.\n\n{tcolors.RESET}McCMD is a joke project meant to test how good python is at creating a coding language inside a coding language.\n\nMcCMD is owned by NotDaBenjamin.\nCredit is not required, but appreciated.\n\nLearn how to use McCMD by going to https://pythoncommandblock.pages.dev/ or on the Official GitHub Page.\nPress Y to agree\n\n")
ynl = yn.lower()
if ynl == "y":
    time.sleep(.5)
    print("An error has occurred, we will attempt to fix it now. If you see this message for longer than 10 seconds, restart the program")
    print("\n" * 100)
    print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟫🟩🟩🟫🟩🟫🟫🟫🟫🟫🟩🟩🟩\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟩🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫")
    print(f'{tcolors.OKGREEN}Entering BootScreen... Please wait...')
    time.sleep(1)
    exec(open("NMdebug.py").read())
else:
    sys.exit("Uh oh! McCMD has encountered an error! We were unable to launch bootsc.py {DO NOT ATTEMPT TO LAUNCH IT MANUALLY}"
             "\n\nDev Reason: During the import process, when you were asked to agree, you entered an invalid string that would not allow you to verify during boot, which would cause many errors and make the program unusable until it is restarted. Please ReRun the program and agree to continue to the application.")
