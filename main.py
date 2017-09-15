import change_mac_address as cma
import device_ident as di
import kill_switch as ks
import packet_dumper as pd
import scan_net as sn
import os


class Main:

    @property
    def welcome(self):
        welxome = '''
                Enter 1 for Scanning the networks.
                Enter 2 for Scanning the router.
                Enter 3 for Phishing the packets.
                Enter 4 for Changing the MAC address.
                Enter KILL for disrupting the service.
                Enter q for exiting the app.
                Enter H for help.
                '''
        return welxome

    @property
    def start(self):
        print('Welcome script kiddie:')
        print(self.welcome)

    def selection_action(self):
        self.start
        while True:
            os.system('clear')
            str_u = input('Enter your choice: ')
            if str_u == '1':
                sn.scan()
            elif str_u == '2':
                di.identfy_target()
            elif str_u == '3':
                pd.dump()
            elif str_u == '4':
                cma.change()
            elif str_u == 'KILL':
                ks.kill()
            elif str_u == 'q':
                os.system('clear')
                break
            elif str_u == 'H':
                os.system('clear')
                print('HELP:')
                print(self.welcome)
        else:
            print('BadRobot left the terminal..')


if __name__ == '__main__':
    run = True
    m = Main()
    selection = m.start
    m.selection_action(selection)

