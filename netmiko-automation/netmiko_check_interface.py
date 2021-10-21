from netmiko import ConnectHandler

cisco_device = {
       'device_type': 'cisco_ios',
       'host': '10.1.1.10',
       'username': 'u1',
       'password': 'cisco',
       'port': 22,             # optional, default 22
       'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }
net_connect = ConnectHandler(**cisco_device)
prompter = net_connect.find_prompt()
if '>' in prompter:
    net_connect.enable()

interface = input('Enter the interface you want to enable: ')
output = net_connect.send_command('sh ip interface ' + interface)
if 'Invalid input detected' in output:
       print('You entered invalid interface')
else:
       first_line = output.splitlines()[0]
       print(first_line)
       if not 'up' in first_line:
              print('The interface is down. Enabling interface...')
              commands = ['interface '+interface, 'no shut', 'exit']
              output = net_connect.send_config_set(commands)
              print('#'*40)
              print('Interface is enabled.')
       else:
              print('Interface '+interface+' is already enabled')

print('Closing connection')
connection.disconnect()