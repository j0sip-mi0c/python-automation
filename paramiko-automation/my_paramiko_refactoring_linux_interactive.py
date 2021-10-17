import my_paramiko
import getpass


username = input('Username:')
password = getpass.getpass()

ssh_client = my_paramiko.connect('192.168.1.112', 22, username, password)
remote_connection = my_paramiko.get_shell(ssh_client)

new_user = input('Enter the user you want to create: ')
command = 'sudo useradd -m -d /home/' + new_user + ' -s /bin/bash ' + new_user
my_paramiko.send_command(remote_connection, command)
my_paramiko.send_command(remote_connection, password)
print('A new user has been created')

answer = input('Display the users? (y/n) ')
if answer == "y":
    users = my_paramiko.send_command(remote_connection, 'cat /etc/passwd\n')
    print(users.decode())  #not working for some reason


my_paramiko.close(ssh_client)