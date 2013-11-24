#!/usr/bin/env python
import sys
import os
import time

def update():
    print "[!]Note please delete the orginal directory first" 
    print "[!]Note if you dont have Git installed this will not work"
    do = (raw_input("Is Git installed(Y/N)"))
    if do == "Y":
        pass
    else:
        print "You need to install it then"
        os.system("start iexplore.exe https://msysgit.googlecode.com/files/Git-1.8.4-preview20130916.exe")
        wa = (raw_input("Press Enter to continue"))
        ins = (raw_input("It should now be installed"))
        pass
    print "Your current directory is", os.getcwd()
    print "Changing directoies"
    time.sleep(0.1)
    instalpath = (raw_input("Please enter the path\n\nthat git was installed at "))
    os.chdir("C:/Program Files/Git/bin")
    time.sleep(0.1)
    os.system("git clone git://github.com/Tecksupport/Winlocate" )
    time.sleep(0.1)
    wait = (raw_input("Done!"))
    print "change dir"
    time.sleep(0.1)
    print os.getcwd()
    print "moving your files"
    path = (raw_input("Please enter the path you would me to move to"))
    os.system("mv Winlocate " , path)
    print "Done!! Bitches!!!!\n\nEnjoy your new script"
    
         

update()

#EOF
