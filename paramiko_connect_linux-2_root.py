
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

stdin, stdout, stderr = ssh_client.exec_command('sudo useradd u2\n', get_pty=True)
stdin.write('x\n')
time.sleep(2)

stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n')
print(stdout.read().decode())
time.sleep(1)

print(stderr.read().decode())

print(ssh_client.get_transport().is_active())
#sending commands
if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()