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
if '>' in prompt:
    connection.enable()
#connection.enable()  #entering enable privileged mode
output = connection.send_command('show run')
print(output)

if not connection.check_config_mode():  #into conf t
    connection.config_mode()
#connection.send_command('username u3 secret cisco')  #making another user in conf t

print(connection.check_config_mode())  #check if config t is enabled

connection.exit_config_mode()  #exit from conf t
print(connection.check_config_mode())


print('Closing connection')
connection.disconnect()