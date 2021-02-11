#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Arbab Ali Memon
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)
#Dev:Arbab-Memon
##### LOGO #####
logo = """
\033[1;91m╭━━━┳╮╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╭━━━╮╱╭╮╱╱╱╱╭╮
\033[1;91m┃╭━╮┃┃╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱┃╭━╮┃╱┃┃╱╱╱╱┃┃
\033[1;95m┃╰━━┫╰━┳━━┫╰━┳━━━┳━━┳━╯┣━━╮╱╱┃┃╱┃┣━┫╰━┳━━┫╰━╮
\033[1;95m╰━━╮┃╭╮┃╭╮┃╭╮┣━━┃┃╭╮┃╭╮┃╭╮┣━━┫╰━╯┃╭┫╭╮┃╭╮┃╭╮┃
\033[1;92m┃╰━╯┃┃┃┃╭╮┃┃┃┃┃━━┫╭╮┃╰╯┃╭╮┣━━┫╭━╮┃┃┃╰╯┃╭╮┃╰╯┃
\033[1;92m╰━━━┻╯╰┻╯╰┻╯╰┻━━━┻╯╰┻━━┻╯╰╯╱╱╰╯╱╰┻╯╰━━┻╯╰┻━━╯
\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•\033[1;93m-Arbab-Memon-\033[1;92m•◈•╬╬╬╬╬╬╬╬╬╬╬╬╬╬•◈•

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")

##### logo  
\033[1;91m ______     ______     ______     ______     ______    
           /\  __ \   /\  == \   /\  == \   /\  __ \   /\  == \   
           \ \  __ \  \ \  __<   \ \  __<   \ \  __ \  \ \  __<   
            \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_____\ 
             \/_/\/_/   \/_/ /_/   \/_____/   \/_/\/_/   \/_____/ 
                                                      
    ____  __    _____  __      ____  ______  __
   / __ \/ /   /   \ \/ /     / __ )/ __ \ \/ /
  / /_/ / /   / /| |\  /_____/ __  / / / /\  / 
 / ____/ /___/ ___ |/ /_____/ /_/ / /_/ / / /  
/_/   /_____/_/  |_/_/     /_____/\____/ /_/   
                                             
jalan("\033[1;92m   YOUR MOBILE SPEED IS 1.0002 SD/M .....ACTIVATED")
jalan('\033[1;93m   .....10%......30%.........50%......70%..........100%')
jalan('\033[1;93m   SOME VIRUS HAS FOUND..GOING TO DELETE....DONE100000000%')
jalan("\033[1;93m   NOW SYSTEM IS GOING TO CONNECT WITH CYBER HACKING GALAXY")
jalan("\033[1;93m   ©CYBER PLAYER RIGHT HANDED ® MR ARBAB ALI MEMON 0.01286✓✓✓")
print "\033[1;92m•◈•MR -X •◈•\033[1;91mLogin Arbab-Memon\033[1;92m•◈•Mr -X•◈•"
 ___                           ___                              
(   )                         (   )                             
 | | .-.     .---.    .--.     | |   ___     .--.    ___ .-.    
 | |/   \   / .-, \  /    \    | |  (   )   /    \  (   )   \   
 |  .-. .  (__) ; | |  .-. ;   | |  ' /    |  .-. ;  | ' .-. ;  
 | |  | |    .'`  | |  |(___)  | |,' /     |  | | |  |  / (___) 
 | |  | |   / .'| | |  |       | .  '.     |  |/  |  | |        
 | |  | |  | /  | | |  | ___   | | `. \    |  ' _.'  | |        
 | |  | |  ; |  ; | |  '(   )  | |   \ \   |  .'.-.  | |        
 | |  | |  ' `-'  | '  `-' |   | |    \ .  '  `-' /  | |        
(___)(___) `.__.'_.  `.__,'   (___ ) (___)  `.__.'  (___)       
                                                                
                                                                
CorrectUsername = "Hacker"
CorrectPassword = "Arbab"
