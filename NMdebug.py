# NMdebug will change the mode you run McCMD inside of, giving you access to features a normal user does not have.
# NM WILL LOCK YOUR NAME AT YOUR MODE
import sys

# - = OR
# NM List -
# dev-developer

# NM EARLY List -
# error

# Default = User
NM = "user"

if NM == "user" or NM == "dev" or NM == "developer":
    print(f'Setting Debug Mode: {NM}')
    exec(open("bootsc.py").read())
else:
    sys.exit("Uh oh! McCMD has encountered an error! We were unable to launch bootsc.py {DO NOT ATTEMPT TO LAUNCH IT MANUALLY} \n\nDev Reason: NMdebug is set to an invalid string, head into NMdebug.py and set NM to 'user'.")