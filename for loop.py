#for loops in python
#for loops used to make limited loops in python
#lets get into it

import time


print("This is countdown in python !")
ur_time = int(input("Please enter countdown time : "))

for i in range(ur_time, 0,-1):
    print(i)
    time.sleep(1)

print("Happy New Year! :)")

