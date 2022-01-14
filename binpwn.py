#!/usr/bin/python3

import os
import sys
import requests
from googlesearch import search


R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m' # white

version = '1.0'

def banner():
	os.system('clear')
	banner = r'''
                            ,--.,-.----.                            
    ,---,.    ,---,       ,--.'|\    /  \                           
  ,'  .'  \,`--.' |   ,--,:  : ||   :    \                          
,---.' .' ||   :  :,`--.'`|  ' :|   |  .\ :       .---.      ,---,  
|   |  |: |:   |  '|   :  :  | |.   :  |: |      /. ./|  ,-+-. /  | 
:   :  :  /|   :  |:   |   \ | :|   |   \ :   .-'-. ' | ,--.'|'   | 
:   |    ; '   '  ;|   : '  '; ||   : .   /  /___/ \: ||   |  ,"' | 
|   :     \|   |  |'   ' ;.    ;;   | |`-'.-'.. '   ' .|   | /  | | 
|   |   . |'   :  ;|   | | \   ||   | ;  /___/ \:     '|   | |  | | 
'   :  '; ||   |  ''   : |  ; .':   ' |  .   \  ' .\   |   | |  |/  
|   |  | ; '   :  ||   | '`--'  :   : :   \   \   ' \ ||   | |--'   
|   :   /  ;   |.' '   : |      |   | :    \   \  |--" |   |/       
|   | ,'   '---'   ;   |.'      `---'.|     \   \ |    '---'        
`----'             '---'          `---`      '---"                 '''
	print(G + banner + W + '\n')
	print(G + '[>] ' + R + 'Created by : ' + W + 'Hacker Destination | Modded by :' + G + ' Denis Sossich')
	print(G + '[>] ' + R + 'Version : ' + W + version)

def cardpwn():
	urls = []
	qlist = []
	total_url = []
	paste_sites = ['cl1p.net', 'dpaste', 'dumpz.org', 'hastebin', 'ideone', 'pastebin', 'pw.fabian-fingerle.de','gist.github.com','https://www.heypasteit.com/','ivpaste.com','mysticpaste.com','paste.org.ru','paste2.org','sebsauvage.net/paste/','slexy.org','squadedit.com','wklej.se','textsnip.com','throwbin.io','ghostbin.com','justpaste.it', 'termbin.com']
	card = input(G + '[+] ' + R +'Enter BIN No. Max 6 numbers -> ' + W)
	try:
		val = int(card)
		if len(str(val)) >= 1 and len(str(val)) < 7:
			for site in paste_sites:
				query = '{} {}'.format(site, card)
				qlist.append(query)
			for entry in qlist:
				for url in search(entry, pause=15, stop=200, user_agent='Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'):
					urls.append(url)

			print('\n' + G + '[>]' + R + ' Getting Dumps...' + W + '\n')
			for item in urls:
				for site in paste_sites:
					if '{}'.format(site) in item:
						print(G + '[+] ' + C + item + W)
						total_url.append(item)

		else:
			print('\n' + R + '[!] ' + G + 'Invaild BIN Number' + W + '\n')
			return cardpwn()
		total = len(total_url)
		if total == 0:
			print (R + '[-] No Open Leaks for this BIN Number Found.' + W + '\n')
		else:
			print('\n' + G + '[+]' + R + ' Total Dumps Found : ' + W + str(total) + '\n')

	except ValueError:
		print('\n' + R + '[!] Invaild BIN Number Entered...' + W + '\n')


def network():
	try:
		requests.get('https://github.com/', timeout = 5)
		print ('\n' + G + '[+]' + R + ' Checking Internet Connection...' + W, end = '')
		print (G + ' Working' + W + '\n')
	except requests.ConnectionError:
		print (R + '[!]' + R + ' You are Not Connected to the Internet...Quiting...' + W)
		sys.exit()
def brain():
		print ('\n' + G + '[+]' + R + ' Checking Brain Connection...' + W, end = '')
		print (G + ' Not Working' + W + '\n')
		
try:
	banner()
	brain()
	network()
	cardpwn()
except KeyboardInterrupt:
	print ('\n' + R + '[!]' + R + ' Keyboard Interrupt.' + W)
	exit()
