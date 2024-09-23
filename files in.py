#file detection in python


import os


path = "C:\\Users\\A v S H\\NeverGonnaStop" #use your own path its different on your device

if os.path.exists(path):
    print("yes that location exist")
    if os.path.isfile(path):
        print("this is a file")


    elif os.path.isdir(path):
        print("This is a directory")

else:
    print("No it does not exist")


