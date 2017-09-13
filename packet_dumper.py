import os

try:
	os.system('clear')
	print('Caution: this script is for educational purposes only.')
	bsid = input('Enter Target bssid:')
	chnl = input('Enter Target channel:')
	fil = input('Enter file name for packet dump:')
	wl = input('Enter monitoring adapter:')
	print('suggestion: *.cap file will be used in wireshark')
	cmd = 'airodump-ng --bssid {} --channel {} --write {} {}'.format(bsid, chnl, fil, wl)
	os.system(cmd) 
finally:
	os.system('clear')
	print('BadRobot over and out...')
	print('you are on your own now :D')



