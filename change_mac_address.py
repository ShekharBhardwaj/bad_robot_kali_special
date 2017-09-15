import os


def change():
    try:
        wln = input('Enter your monitor:')
        cmd_1 = 'ifconfig {} down'.format(wln)
        cmd_2 = 'macchanger -r {}'.format(wln)
        cmd_3 = 'ifconfig {} up'.format(wln)
        os.system(cmd_1)
        os.system(cmd_2)
        os.system(cmd_3)
    finally:
        print('Your MAC address has been randomized')
        print('BadRobot over and out..')

if __name__ == '__main__':
    change()