import time
print("\n" * 100)

print(f"{tcolors.HEADER}Welcome to McCMD, {name}!{tcolors.ENDC}")
print(NM)

print(f"{tcolors.OKCYAN}")

if NM.lower() == "dev":
    print(f"{tcolors.WARNING}You are in developer mode, you now have access to debug features normal users do not have. To disable,\ngo into NMdebug.py and change NM to user.\nTo get started, use the command //help [DEV]")

menu = input(f"Enter a {tcolors.UNDERLINE}System Command{tcolors.RESET}{tcolors.OKCYAN}, or choose from the list below:\n\n1. Import File [//Import [About/Select/[NONE]]\n2. Free Code [//Free [About/Select/[NONE]]\n3. Contact [//Contact] \n4. Documentation/Getting Started [//Documentation]\n5. Exit [//Exit]\n\nYour Choice: ")

if menu == "2":
    exec(open("freecode.py").read())
elif menu.lower() == "//free":
    exec(open("freecode.py").read())
elif menu.lower() == "//free select":
    exec(open("freecode.py").read())
elif menu.lower() == "//free about":
    print("\n" * 100)
    desc = input(freedesc)
    exec(open("menu.py").read())
elif menu.lower() == "//contact":
    print("\n" * 100)
    print("https://pythoncommandblock.pages.dev/contact")
    print("\n")
    input("Press enter to return to the menu")
    exec(open("menu.py").read())
elif menu.lower() == "//exit":
    sys.exit("User chosen to exit the program. You may ignore this error. Thank you for using McCMD!")
else:
    print("\n" * 100)
    print(f"{tcolors.FAIL}Uh oh! McCMD has encountered an error! Invalid Command! \n\nDev Reason: User has entered an invalid command that does not exist in the menu, this is likely caused by a typo or the user not knowing the correct command.")
    print("We are currently attempting to recover, please wait...")
    time.sleep(3)
    if ver == "y":
        print("Recovery Successful! Returning to menu...")
        time.sleep(3)
        exec(open("menu.py").read())