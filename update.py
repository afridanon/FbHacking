#####################################################
#     author   :-  SHAIK AFRID                      #
#    github   :-  https://github.con/afridanon      #
#    twitter  :-  @afridanon                        #
#    purpose  :-  educational purpose only          #
#     @--- DONT TRY TO STEEL MY CODE Bitch ---@     #
#####################################################


import os
import shutil
import sys
import time

def open():
    
    from colorama import Fore
    if shutil.which('git'):
        
        print(Fore.YELLOW +" -->>   UPDATING THE SCRIPT   <<--")
        time.sleep(5)
        os.system('git checkout . && git pull')
        print(Fore.YELLOW + " ->  UPDATED SUCCESSFULLY RUNNING THE TOOL AGAIN  <-")
        time.sleep(4)
        os.system("python main.py")
    else:
        
        print("Please ReClone CracKing Again")
        sys.exit()
def dep():
    os.system("pip install colorama")


if __name__ == "__main__":
    dep()
    open()