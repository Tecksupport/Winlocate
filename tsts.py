#!/usr/bin/python
# Teck
import urllib2
import re
import sys
import os
import linecache
import ctypes
import time
import socket
from socket import *
from threading import *
import subprocess
import random
import time












# most crdit goes to http://www.unix.com/shell-programming-scripting/136055-using-python-grab-data-website.html
#user name  Momo.reina
# and also http://stackoverflow.com/questions/2081836/reading-specific-lines-only-python
# although added a few things for it, so it can complie correclty 

#get the file
""" http://stackoverflow.com/users/37020/orip """
# Constants from the Windows API 
STD_OUTPUT_HANDLE = -11 
FOREGROUND_RED = 0x0007 # text color contains red.
FOREGROUND_Fai = 0x0004
FOREGROUND_YEL = 0x0006
FOREGROUND_GRN = 0x0002
FOREGROUND_BlU = 0x0003
FOREGROUND_PPL = 0x0005
FOREGROUND_LIB = 0x0009 # Light Blue
FOREGROUND_LIG = 0x000A # Light Green
FOREGROUND_LIA = 0x000B # Light aqua
FOREGROUND_LIP = 0x000D # Light Purp
FOREGROUND_LIY = 0x000E # light yel
FOREGROUND_LIW = 0x000F # Bright White
FOREGROUND_LIR = 0x000C # Light RED



while True:
    



    def util():
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIR)
        print "*" * 10
        print "1 ->> nslookup"
        print "2 ->> ping"
        print "3 ->> finger" 
        print "4 ->> dig"
        print "5 ->> whois"
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
        op =  input("Enter choice: ")
        if op == 1:
            nslook()
            options()
        if op == 2:
            ping()
            options()
        if op == 3:
            finger() 
            options()
        if op == 4:
            time.sleep(0.1)
            print "Not for windows"
            #dig()
            options()
        if op == 5:
            time.sleep(0.1)
            print "Not for windows"
            #whois()
            options()
        if op == "clear":
            clear()
            options()


    def dig():
        print "Choice of dig"
        targ = (raw_input("Enter host to dig: "))
        os.system("dig " + targ)
        time.sleep(0.04)
        options()        

    def menu():
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIR)
        print "How would you like perform this scan"
        print "=" * 10 
        print "1) -->  Common port scan"
        print "2) -->  Specifiyed range scan "
        print "3) -->  Single port scan"
        print "=" * 10
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)



    def clear():
        os.system("cls")
    
    

    def portmenu():
        print "Would like to port scan the host(Y/N)"
        a = (raw_input("Choice: "))
        if a == 'Y' or a == 'y':
            menu()
            y = input("Choice: ")
            if y == 1:
                portscan()
                return portmenu()
            elif y == 2:
                 portrange()
                 return portmenu()
            elif y == 3:
                singleport()
                return portmenu()
            elif y == "clear":
                clear()
                options
            else:
                time.sleep(0.3)
                print "Invalid choice"
                return portmenu()
   
    def nslook():
        print "NSlookup"
        n = (raw_input("Would you like to do a nslookup?(Y/N)"))
        if n == "Y" or n == "y":
              print "[OK]"
              trg = (raw_input("Plaese enter the host name: "))
              os.system("nslookup  " + trg )
              pass 
        if n == "N" or n == "n":
              print "Moving on"
              pass
        if n == "Skip portscan":
              print "Skipping"
              portmenu()


    

    def local():
        try:
            print"local ip information"
            ch = (raw_input("Is this a local look up?(Y/N): "))
            if ch == "Y" or ch == "y":
                locallook()
            elif ch == "n" or ch == "N":
                os.system("cls")
                print "[+]Going back to main"
                time.sleep(0.3)
                options()
            elif ch == "":
                time.sleep(0.1)
                print"[!]You left the question blank"
                os.system("cls")
                return local()
            elif ch == "Goto portscan":
                print "Skipping to portscan"    
                portmenu()
            else:
                time.sleep(0.3)
                print "[*]Invalid option"
                os.system("cls")
                return local()
           
        except KeyboardInterrupt:
            print "\n\n"+"quitting"
            raise SystemExit


    def dig():
        print "Choice of dig"
        targ = (raw_input("Enter host to dig: "))
        os.system("dig " + targ)
        time.sleep(0.04)
        options()
 
     
    def finger():
       print "This can be done with a finger command"+'\n'+"would you like me to run the finger commnd"+'\n'+"1 for Yes 2 for No"
       fi = input()
       if fi == 1:
              print "using the finger command"
              os.system("finger -l")
              pass
       elif fi == 2:
                print "going foward then"
                pass   
     


    def locallook():
        print "Looking up the local IP address"
        ff = urllib2.urlopen("http://showmemyip.com")
        s = str(ff.read())
        ff.close()
        pattern = r'(<.*?>)'
        ff = open('local.txt','w')
        ff.write(re.sub(pattern,'',s))
        ff.close()     
        locall = open("local.txt").readlines()[28],
        for lines in locall:
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIR)
            print (lines)
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
            time.sleep(0.3)
            ip = (lines)
            os.system("cls")
            print " Now add the ip below   " +ip
            outside()
    
    def outside():
        try:
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIW)
            f = "Enter First Octant: "
            s = "Enter second Octant:"
            t = "Enter Third Octant: "
            fo ="Enter fourth Octant: "
            fail = "You entered this blank"
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
            wait = "Continue?(Y/N)"
            
            f = (raw_input(f))
            if f == "":
                print fail
                f = (raw_input("Enter first Octant: "))
            s = (raw_input(s))
            if s == "":
                print fail
                s = (raw_input("Enter second Octant: "))
            t = (raw_input(t))
            if t == "":
                print fail
                t = (raw_input("Enter third Octant: "))
            fo = (raw_input(fo))
            if f  == "":
                print fail
                fo = (raw_input("Enter fourth Octant: "))
        except KeyboardInterrupt:
            print '\n'+"Quitting"
            raise SystemExit
        print  "specifyed  ip address "+f+'.'+s+'.'+t+'.'+fo 
        time.sleep(0.1)            
 
        try:
            ff = urllib2.urlopen("http://www.iplocationfinder.com/"+f+'.'+s+'.'+t+'.'+fo)
            print "Now fetching your infomation"
            bar()
            os.system("cls")
            s = str(ff.read())
            ff.close()
            pattern = r'(<.*?>)'
            ff = open('location.txt', 'w') 
            ff.write(re.sub(pattern,'',s))
            ff.close()
            lip = open('location.txt').readlines()[58],
            for lines in lip:
                ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIG)
                print (lines) 
            trip = open('location.txt').readlines()[66],
            for lines in trip:
                print (lines)
            rip = open('location.txt').readlines()[67],
            for lines in rip:
                print (lines)
            it = open('location.txt').readlines()[68],
            for lines in it:
                print (lines)
            of = open('location.txt').readlines()[69],
            for lines in of:
                print (lines)
            read = open('location.txt').readlines()[70],
            for lines in read:
                print (lines)
            ancor = open('location.txt').readlines()[71],
            for lines in ancor:
                print (lines)
            teck = open('location.txt').readlines()[72],
            for lines in teck:
                print (lines)
            god = open('location.txt').readlines()[73], 
            for lines in god:
                print (lines)
            ip = open('location.txt').readlines()[74],
            for lines in ip:
                print (lines)
            look = open('location.txt').readlines()[75],
            for line in look:
                print (lines)
            hack = open('location.txt').readlines()[76],
            for lines in hack:
                print (lines)
            vito = open ('location.txt').readlines()[77],
            for lines in vito:
                print (lines)
            HGB = open('location.txt').readlines()[78],
            for lines in HGB:
                print (lines)
                ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
            wait = (raw_input("Would you like to continue(Y?N)"))
            try:
                if wait == "Y" or wait == "y":
                    pass
                elif wait == "N" or wait == "n":
                    i = random.randrange(0,2)
                    if i == 0:
                        print "Thank you for using this program"
                        raise SystemExit             
                    if i == 1:
                        print "[Even though your winning it dosen't mean you've won]"
                        raise SystemExit
                    else:
                        print "Thanks for not answering the question i'll exit then"
                        raise SystemExit 
            except KeyboardInterrupt:
                print "You hit Ctl-C Exitting"
                raise SystemExit  

            
        except urllib2.HTTPError, e:
            time.sleep(0.1)
            print "This IP does not exist"+'\n'+"Exitting"
            print e
            time.sleep(0.1)
            os.system("cls")
            print "This is the last output information requested"+'\n'+"Since you ty"       


               

                

## Only works for linux only 
##    def whois():
##         print "Choice of whois"
##         host = (raw_input("Enter host : "))
##         os.system("whois " + host)
##         time.sleep(0.04)
##         options()



    screenLock = Semaphore(value=1)    
    def singleport():
         try:
             host = (raw_input("Enter host: "))
             port = input("Enter port num: ")
             print "=" * 30
             print "Single port and application scanning"
             print "=" * 30
             print "Talking to host first\r\n"
             ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIG)
             os.system("ping " + host+ " -n 5")
             ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
             print "Complete\nScanning the port",port
             s = socket(AF_INET, SOCK_STREAM)
             s.connect((host, port))
             s.send('Tecks port scan\r\n')
             msg = s.recv(100)
             screenLock.acquire()
             ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIG)
             print '[!]%d/tcp open'%port
             print "[+] " + str(msg)
             ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
         except:
              screenLock.acquire()
              ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIR)
              print "[-]%d/tcp Closed"%port
              ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
              s.close()      

         finally:
            screenLock.release()
            s.close()
            print "Scanner complete for ",host
            options() 
    

            
    def bar():
        prgbar_width = 18
        sys.stdout.write("[%s]" % (" " * prgbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (prgbar_width+1))
        for i in xrange(prgbar_width):
            time.sleep(0.1)
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIA)
            sys.stdout.write("~")
            sys.stdout.flush()
            sys.stdout.write("")
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
            

    def ping():
        try:
           print "Would you like to ping to see if the host is alive"
           p = (raw_input("(Y/N)"))
           if p  == "Y" or p == "y":
                  print "Ok lets ping the host"
                  host = (raw_input("Enter the host IP: "))
                  print "pinging ==>[",host,"]"
                  ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIG)
                  os.system('ping ' + host)
                  ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
                  pass 
           elif p == "N" or p == "n":
                   print "Then ill pass on then"
                   pass
        except KeyboardInterrupt:
               time.sleep(0.1)
               print '\n'+"going back to main"
               pass 

    
    def portscan():
        try:
            host = (raw_input("host : " ))
            #strt = input("start ")
            #end = input("end ")
            print "=" * 40
            print "Now port scanning" , host
            print "=" * 40
            print "Well run a ping sweep first"
            time.sleep(0.2)
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIG)
            os.system("ping  "+ host+ " -n 5")
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset) 
            print "[*]ping sweep complete"+'\n'+"Now port scanning" 
            portlst = 21,22,23,443   
            for port in portlst:
                s = socket(AF_INET, SOCK_STREAM)
                if s.connect_ex((host,port)) == 0:
                      ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIG)
                      print "Port :",port,"[!]Open"
                      ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
             
                else:
                     ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIR)
                     print "Port :",port," Closed"
                     ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
                     s.close()
        except KeyboardInterrupt:
                print "Ctl-C caught"
                raise SystemExit  
  
        finally:
            print "scan complete for ",host
            options()    
    
    
    def portrange():
         try:
            host = (raw_input("Enter Host: ")) 
            first = input("Enter start range: ")
            last  = input("Enter end range: ") 
            print "=" * 20
            print "specified scanner"
            print "=" * 20
            print "ping sweep begin "
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIG)
            os.system("ping "+ host+ " -n 5")
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
            print "ping complete"+'\n'+"Now port scanning"
            for port in range(first, last):
                s = socket(AF_INET, SOCK_STREAM)
                #message = s.recv(1024)
                if s.connect_ex((host,port)) == 0:
                    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIG) 
                    print "Port : ",port, "Open"
                    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
                      # print "[!]"+str(message)
                else:
                    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIR)
                    print "Port : ",port, "Closed"
                    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
                    s.close()
            

         finally:
            print "Scan complete for "+ host
            options()
  

    
    def options():
        try:
            print "\n\n"
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_YEL)
            print "Choose a choice" 
            print "*" * 10 
            print "1 >> Outside Ip Lookup"
            print "2 >> Local IP Lookup"
            print "3 >> Port scanner"
            print "4 >> Utilites"
            print "5 >> Clear Screen"
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
            c = input("->>__ ") 
            if c == 1:
                outside()
            elif c == 2:
                local()
            elif c == 3:
                 portmenu()
            elif c == 4:
                util()
            elif c == 5:
                clear()
                options()
            
            else:
                time.sleep(0.2)
                print "wrong"
                return options()
        except KeyboardInterrupt:
            print "\n\nControl-C caught"
            raise SystemExit

    
    
    def get_csbi_attributes(handle): 
        # Based on IPython's winconsole.py, written by Alexander Belchenko 
        import struct 
        csbi = ctypes.create_string_buffer(22) 
        res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi) 
        assert res 
     
        (bufx, bufy, curx, cury, wattr, 
        left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw) 
        return wattr
     
     
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE) 
    reset = get_csbi_attributes(handle) 

     
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_LIA)
    os.system("cls")
    print "============================================"
    print "Infromation Parser rev 8.0"
    print "============================================"
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
    options()


    
    
  
  
       

    
   
 
    
   
    
    
   

    
  


    
    
    
    
   


    

    
        


    
            
    
    
  

##   sick = open('location.txt').readlines()[108],
##   for lines in sick:
##       print (lines)
##   find = open('location.txt').readlines()[109],
##   for lines in find:
##       print (lines)
##   snap = open('location.txt').readlines()[110],
##   for lines in snap:
##       print (lines)
##   tack = open('location.txt').readlines()[112],
##   for lines in tack:
##       print (lines)
##   help = open('location.txt').readlines()[113],
##   for lines in help:
##       print (lines)
##   sex = open('location.txt').readlines()[114],
##   for lines in sex:
##       print (lines)
##   itia = open('location.txt').readlines()[115],
##   for lines in itia:
         # Lines can be added if more is needed




    
    
   
    
    
