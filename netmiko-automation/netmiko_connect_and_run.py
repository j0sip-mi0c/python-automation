#below in comment is a first option to connect to device
#from netmiko import Netmiko
#connection = Netmiko(host='10.1.1.10', port='22', username='u1', password='cisco', device_type='cisco_ios')
from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.10',
    'username': 'u1',
    'password': 'cisco',
    'port': 22,   #optional, default 22
    'secret': 'cisco',  #optional, default ''
    'verbose': True     #optional, default False
}
connection = ConnectHandler(**cisco_device)

print('Running commands...')
output = connection.send_command('show ip interface brief')
print(output)

print('Closing connection')
connection.disconnect()