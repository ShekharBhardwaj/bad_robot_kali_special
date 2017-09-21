import os


def scan():
	try:
		userchoice = input('''
		1 for 2.4Ghz(Default)
		2 for 5Ghz :''')
		print('CAUTION: This script is for educational purposes only')
		print('starting monitoring on wlan0')
		os.system('airmon-ng start wlan0')
		print('If you are not seeing any output make sure your wifi adapter is in place and working')
		if userchoice == '1':
			os.system('airodump-ng wlan0mon')
		else:
			os.system('airodump-ng wlan0mon --band a')

	except ValueError as e:
		print('Script failed due to ----> {}'.format(e))
	finally:
		print('BadRobot over and out...')


if __name__ == '__main__':
	scan()
