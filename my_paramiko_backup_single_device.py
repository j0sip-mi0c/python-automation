import my_paramiko
import time

router = {'server_ip': '10.1.1.30', 'server_port': '22', 'user': 'u2', 'passwd': 'cisco'}
client = my_paramiko.connect(**router)
shell = my_paramiko.get_shell(client)


#my_paramiko.send_command(shell, 'show ip interface brief\n')
#time.sleep(1)
my_paramiko.send_command(shell, 'enable\n')
my_paramiko.send_command(shell, 'cisco')
my_paramiko.send_command(shell, 'show run\n')



output = my_paramiko.show(shell)
print(output)

output_list = output.splitlines()
output_list = output_list[11:-1]

output = '\n'.join(output_list)

from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

file_name = f'{router["server_ip"]}_{year}_{month}_{day}.txt'
print(file_name)

with open(file_name, 'w') as f:
    f.write(output)

my_paramiko.close(client)