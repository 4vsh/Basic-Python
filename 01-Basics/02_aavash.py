#hi im Aavash
#i like to code
#i like to read
#i like to write
#i like to play games


#just a intro

print("Welcom to my social links")

while True:
    print("1. X (FORMERLY KNOWN AS TWITTER)")
    print("2. INSTAGRAM")
    print("4. YOUTUBE")
    print("5. DISCORD")
    print("6. SPOTIFY")

    choice = input("Enter the number of the social link you want to visit: ")

    if choice == "1":
        print("https://x.com/AvshPy")
    elif choice == "2":
        print("https://www.instagram.com/avsh.exe")
    elif choice == "3":
        print("Not available yet")
        print("https://www.youtube.com/")
    elif choice == "4":
        print("https://discord.gg/sphinxgm")

    elif choice == "5":
        print("https://open.spotify.com/user/
        ")

    else:
        print("Invalid choice")

    if choice == "6":
        break

    print("Do you want to visit another social link? (y/n)")
    if input() == "n":
        break
    elif input() == "y":
        continue
    else:
        print("Invalid choice")
        break


print("Thank you for visiting my social links!")

