import os


path = 'aww.txt'

try:
    os.remove(path)
    #os.rmdir(dir_path) #delete directory!!

except FileExistsError:
    print("File does not exist on the given location :/ ")

except FileNotFoundError:
    print("File Does not found in given path :/")

else:
    print("Thanks my idiot the file has been deleted :)")
