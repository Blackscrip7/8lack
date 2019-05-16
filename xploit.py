#!/usr/bin/env python2.7
#coding=utf-8
#Coded By Black Script
#Love to TeaM_CC
#Learn to code, not to copy :)
#Salam to all muslim brothers :)
#  ____  _            _      ____            _       _
# | __ )| | __ _  ___| | __ / ___|  ___ _ __(_)_ __ | |_
# |  _ \| |/ _` |/ __| |/ / \___ \ / __| '__| | '_ \| __|
# | |_) | | (_| | (__|   <   ___) | (__| |  | | |_) | |_
# |____/|_|\__,_|\___|_|\_\ |____/ \___|_|  |_| .__/ \__|

import urllib,requests,sys, os , re, socket # pip install requests
from platform import system
from time import time as timer
def clearscrn() :
  if system() == 'Linux':
    os.system('clear' )
  if system() == 'Windows':
    os.system('cls')
clearscrn()
def bannner() :
    print """\033[0m

 ____  _            _      ____            _       _   By 8l@ck Scr!p7
| __ )| | __ _  ___| | __ / ___|  ___ _ __(_)_ __ | |_ 
|  _ \| |/ _` |/ __| |/ / \___ \ / __| '__| | '_ \| __|
| |_) | | (_| | (__|   <   ___) | (__| |  | | |_) | |_ 
|____/|_|\__,_|\___|_|\_\ |____/ \___|_|  |_| .__/ \__|
                                            |_|
\033[91m"""

def menu():
    clearscrn()
    bannner()
    print ( """\033[1m
  [!] https://github.com/Blackscrip7 [!] 
 -----------------------------------------------------------------------
\033[0m
   [1] - Get Ip From site            
   [2] - Reverseiplookup             
   [3] - Your IP and Location                                  
   [4] - Exit              
 """)
    choice = raw_input("   BlackScript:~$ ")
    try :
        if choice == '1':
            clearscrn()
            bannner()
            getip()
        elif choice == '2':
            clearscrn()
            bannner()
            grab()
        elif choice == '3':
            clearscrn()
            bannner()
            myinfo()
        
    except (EOFError,KeyboardInterrupt):
        pass
def getip():
    print("==============================")
    print("[+] Get Ip From sites [+]")
    print("==============================")
    try :
        Files = open(raw_input('Enter Site List ~# '), 'r')
        for i in Files.readlines():
            site = i.strip()
            try:
                if 'http://' not in site:
                    IP1 = socket.gethostbyname(site)
                    print "[-]#IP:" + IP1
                    open('ips.txt', 'a').write(IP1 + '\n')
                elif 'http://' in site:
                    url = site.replace('http://', '').replace('https://', '').replace('/', '')
                    IP2 = socket.gethostbyname(url)
                    print "[-]#IP:" + IP2
                    open('ips.txt', 'a').write(IP2 + '\n')
                elif 'https://' in site:
                    url = site.replace('http://', '').replace('https://', '').replace('/', '')
                    IP2 = socket.gethostbyname(url)
                    print "[-]#IP:" + IP3
                    open('ips.txt', 'a').write(IP3 + '\n')

            except:
                pass
    except (EOFError, KeyboardInterrupt):
        pass




def grab():
    print("==============================")
    print("[+] Reverseiplookup From ip [+]")
    print("==============================")
    try :
        nam = raw_input('Enter ip List ~#  ')
        with open(nam) as f:
            for i in f:
                try:
                    ch = requests.get('http://api.hackertarget.com/reverseiplookup/?q=' + i)
                    if '.' in ch.content:
                        print ' [+] Grabbing done IP ->> ', i
                        open('mass.txt', 'a').write(ch.content)
                        time.sleep(5)

                    else:
                        print "[!] => " + i + '  Problem '
                except:
                    pass
    except (EOFError, KeyboardInterrupt):
        pass


def myinfo():
    print("==============================")
    print("[+] Your IP and Location [+]")
    print("==============================")
    if system() == 'Linux':
        os.system('curl ipinfo.io')
    if system() == 'Windows':
        os.system('curl ipinfo.io')




menu() #excute Script
