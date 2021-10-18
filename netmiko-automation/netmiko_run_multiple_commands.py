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
prompt = connection.find_prompt()  #find if you are in privileged or basic mode
print(prompt)
print("Entering enable mode")
if '>' in prompt:
    connection.enable()
#connection.enable()  #entering enable privileged mode

#commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret cisco']  #creating a new user
#output = connection.send_config_set(commands)  #two lines in comments are first option to run commands

#cmd = 'ip ssh version 2;access-list 1 permit any;ip domain-name network-automation.io'
#output = connection.send_config_set(cmd.split(';'))    #this is second version of sending commands

cmd = '''ip ssh version 2
access-list 1 permit any
ip domain-name net-auto.io
'''
output = connection.send_config_set(cmd.split('\n'))

print(output)
print(connection.find_prompt())

connection.send_command('write memory')

print("Closing connection")
connection.disconnect()