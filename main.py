#####################################################
#     author   :-  SHAIK AFRID                      #
#    github   :-  https://github.con/afridanon      #
#    twitter  :-  @afridanon                        #
#    purpose  :-  educational purpose only          #
#     @--- DONT TRY TO STEEL MY CODE Bitch ---@     #
#####################################################

import os
import os.path
import time
import sys
import requests
def pubg():
    print("You Selected Pubg")
    time.sleep(4)
    print("This Is Under Maintence")
    print("Try After Some Days !")
    time.sleep(6)
    sys.exit()
def FaceBook():
    print("You Selected FaceBook")
    time.sleep(4)
    print("Use Only For Good purpose !")
    print("Wait A While  ..... ")
    time.sleep(5)
    os.system("python FaceBook.py")
def InstaGram():
    print("You Selected InstaGram")
    time.sleep(4)
    print("Use Only For Good purpose !")
    print("Wait A While  ..... ")
    time.sleep(5)
    os.system("python InstaGram.py")


#####################################################
#     author   :-  SHAIK AFRID                      #
#    github   :-  https://github.con/afridanon      #
#    twitter  :-  @afridanon                        #
#    purpose  :-  educational purpose only          #
#     @--- DONT TRY TO STEEL MY CODE Bitch ---@     #
#####################################################

print("1 == Facebook")
print("2 == InstaGram")
print("3 == Github")
print("4 == FreeFire")
print("5 == Pubg!")

while(True):
    User_Value = int(input("Please Enter Which You Want Hack  :- "))
    if(User_Value == 1):
        FaceBook()
    elif(User_Value == 2):
        InstaGram()
    elif(User_Value == 3):
        print("You Selected Github")
    elif(User_Value == 4):
        print("You Selected FreeFire")
    elif(User_Value == 5):
        pubg()
    else:
        print("Plese Enter A Valid Value :(")
