import my_paramiko

router = {'server_ip': '10.1.1.20','server_port': '22', 'user': 'u2', 'passwd': 'cisco'}
client = my_paramiko.connect(**router)
shell = my_paramiko.get_shell(client)


my_paramiko.send_command(shell, 'terminal length 0')
my_paramiko.send_command(shell, 'enable')
my_paramiko.send_command(shell, 'cisco')
my_paramiko.send_command(shell, 'show run')



output = my_paramiko.show(shell)
print(output)

my_paramiko.close(client)