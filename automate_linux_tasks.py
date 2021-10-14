import my_paramiko

client = my_paramiko.connect('192.168.1.110', '22', 'x', 'x')
shell = my_paramiko.get_shell(client)
my_paramiko.send_command(shell, 'uname -a')

cmd = 'sudo groupadd developers'
my_paramiko.send_command(shell, cmd)
my_paramiko.send_command(shell, 'x', 2)
#my_paramiko.show(shell) #to see only next in row ouptut
my_paramiko.send_command(shell, 'tail -n 1 /etc/group')

output = my_paramiko.show(shell)
print(output)

my_paramiko.close(client)