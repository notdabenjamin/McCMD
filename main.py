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

ver = "y"
sm = "y"

yn = input("WARNING: McCMD is NOT optimized to run on every software, the entire software was made on VS Code and PyCharm and was also\nslightly tested on Windows Command Prompt. We recommend running it on PyCharm or CMD, as VS Code has large amounts\nof bugs. It is reccommended that you use a Non-Web based python compiler, as Web based often have low access to python\nlibraries, which McCMD heavily relies on. We have tried our best to make it compatible with every single software, but it seems like it is impossible.\n\nMcCMD is a joke project meant to test how good python is at creating a coding language inside a coding language.\n\nMcCMD is owned by NotDaBenjamin.\nCredit is not required, but appreciated.\n\nLearn how to use McCMD on the Official GitHub Page\nPress Y to agree\n\n")
if yn == "Y":
    time.sleep(.5)
    print("An error has occurred, we will attempt to fix it now. If you see this message for longer than 10 seconds, restart the program")
    print("\n" * 100)
    print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟩🟫🟩🟩🟫🟩🟫🟫🟫🟫🟫🟩🟩🟩\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟩🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫")
    print('Entering BootScreen... Please wait...')
    time.sleep(1)
    exec(open("NMdebug.py").read())
else:
    print("\n" * 100)
    sys.exit("Uh oh! McCMD has encountered an error! We were unable to launch bootsc.py {DO NOT ATTEMPT TO LAUNCH IT MANUALLY}"
             "\n\nDev Reason: During the import process, when you were asked to agree, you entered an invalid string that would not allow you to verify during boot, which would cause many errors and make the program unusable until it is restarted. Please ReRun the program and agree to continue to the application.")