from netmiko import ConnectHandler

linux = {
    'device_type': 'linux',
    'host': '192.168.1.111',
    'username': 'x',
    'password': 'x',
    'port': 22,   #optional, default 22
    'secret': 'x',  #optional, default ''
    'verbose': True     #optional, default False
}
connection = ConnectHandler(**linux)

connection.enable()  #sudo su
output = connection.send_command('apt install -y apache2')
print(output)

print(f"Closing connection")
connection.disconnect()