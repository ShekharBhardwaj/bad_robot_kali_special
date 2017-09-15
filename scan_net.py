import os


def scan():
	try:
		print('CAUTION: This script is for educational purposes only')
		print('starting monitoring on wlan0')
		os.system('airmon-ng start wlan0')
		print('If you are seeing any output make sure your wifi adapter is in place and working')
		os.system('airodump-ng wlan0mon')
	finally:
		print('BadRobot over and out...')


if __name__ == '__main__':
	scan()