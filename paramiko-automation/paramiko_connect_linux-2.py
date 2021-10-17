
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

stdin, stdout, stderr = ssh_client.exec_command('ifconfig\n')
output = stdout.read()
output = output.decode()
print(output)

stdin, stdout, stderr = ssh_client.exec_command('whodsadsa\n')
time.sleep(0.5)
output = stdout.read()
output = output.decode()
print(output)

print(stderr.read().decode())

print(ssh_client.get_transport().is_active())
#sending commands
if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()