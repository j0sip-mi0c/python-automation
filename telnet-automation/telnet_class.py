import time

class Device:
    def __init__(self, host, username, password, tn=None):  #constructor
        self.host = host
        self.username = username
        self.password = password
        self.tn = tn

    def connect(self):
        import telnetlib
        self.tn = telnetlib.Telnet(self.host)

    def authenticate(self):
        self.tn.read_until(b'Username: ')
        self.tn.write(self.username.encode() + b'\n')

        self.tn.read_until(b'Password: ')
        self.tn.write(self.password.encode() + b'\n')

    def send(self, command, timeout=0.5):
        print(f'Sending command: {command}')
        self.tn.write(command.encode() +b'\n')
        time.sleep(timeout)

    def show(self):
        output = self.tn.read_all().decode('utf-8')
        return output

router1 = Device(host='10.1.1.10', username='u1', password='cisco')
router1.connect()
router1.authenticate()
router1.send('enable')
router1.send('cisco')
router1.send('conf t')
router1.send('interface loopback 0')
router1.send('ip address 1.1.1.1 255.255.255.255')
router1.send('exit')
router1.send('router ospf 1')
router1.send('net 0.0.0.0 0.0.0.0 area 0')
router1.send('end')
router1.send('terminal length 0')
router1.send('show ip protocols')
router1.send('exit')
output = router1.show()
print(output)