import sys
import os

print(os.getcwd()+"\log_parser")
with open("sfbios.log") as f1:
    for line in f1:
        if "SFBAppDelegate" in line:
            print("this is present")