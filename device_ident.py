import os


def identfy_target():
	try:
		bsid = input('Enter Target bssid:')
		chnl = input('Enter Target channle:')
		wln = input('Enter your monitoring adapter:')
		cmd = 'airodump-ng --bssid {} --channel {} {}'.format(bsid, chnl, wln)
		os.system(cmd)
	finally:
		print('BadRobot over and out...')
		caution = '''This is illegal, if you are doing this to an unsuspected victim,
			I would highly recommend that you take permission before this attack.
			'''
		print(caution)

if __name__ == '__main__':
	identfy_target()
