import telnetlib
import time
import getpass
#you must run script in terminal because pycharm is not able to run getpass
#issue with running in cmd

router1 = {'host': '10.1.1.10', 'user': 'u1'}
router2 = {'host': '10.1.1.20', 'user': 'u2'}
router3 = {'host': '10.1.1.30', 'user': 'u3'}

routers = [router1, router2, router3]

for router in routers:
    print(f'Connecting to {router["host"]}')
    password = getpass.getpass('Enter Password:')

    tn = telnetlib.Telnet(host=router['host'])

    tn.read_until(b'Username: ')
    tn.write(router['user'].encode() + b'\n')

    tn.read_until(b'Password: ')
    tn.write(password.encode() + b'\n')

    tn.write(b'terminal length 0\n')
    tn.write(password.encode() + b'\n')
    tn.write(b'cisco\n')  # this is enable password
    tn.write(b'conf t\n')
    tn. write(b'ip route 0.0.0.0 0.0.0.0 e0/0 10.1.1.2\n')
    tn.write(b'end\n')
    tn.write(b'show ip route\n')
    tn.write(b'exit\n')
    time.sleep(1)

    output = tn.read_all()
    print(type(output))
    output = output.decode()
    print(output)
    print('#'*50)