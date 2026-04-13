print("\n" * 100)

print(f"{tcolors.HEADER}Welcome to McCMD, {name}!{tcolors.ENDC}")
print(NM)

print(f"{tcolors.OKCYAN}")

if NM.lower() == "dev":
    print(f"{tcolors.WARNING}You are in developer mode, you now have access to debug features normal users do not have. To disable,\ngo into NMdebug.py and change NM to user.\nTo get started, use the command //help [DEV]")

menu = input(f"Enter a {tcolors.UNDERLINE}System Command{tcolors.RESET}{tcolors.OKCYAN}, or choose from the list below:\n\n1. Import File [//Import [About/Select/[NONE]]\n2. Free Code [//Free [About/Select/[NONE]]\n3. Discord [//Discord] \n4. Documentation/Getting Started [//Documentation]\n")

if menu == "2":
    exec(open("freecode.py").read())
if menu.lower() == "//free":
    exec(open("freecode.py").read())
if menu.lower() == "//free select":
    exec(open("freecode.py").read())
if menu.lower() == "//free about":
    desc = input(freedesc)
    exec(open("menu.py").read())
