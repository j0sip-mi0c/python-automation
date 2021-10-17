
import paramiko
import time

ssh_client = paramiko.SSHClient()
#print(type(ssh_client))
#print('Connecting to 10.1.1.10')
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',
#                   look_for_keys=False, allow_agent=False)


linux = {'hostname': '192.168.1.110','port': '22', 'username': 'x', 'password': 'x'}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('cat /etc/passwd\n')
time.sleep(1)
print('Looking for shadow...')
#shell.send('sudo cat /etc/shadow\n')
#shell.send('x\n')
shell.send('ifconfig\n')
time.sleep(1)

output = shell.recv(10000)
#print(type(output))
output = output.decode('utf-8')
print(output)

print(ssh_client.get_transport().is_active())

#sending commands
if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()