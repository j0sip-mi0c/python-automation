import paramiko


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router1 = {'hostname': '10.1.1.10','port': '22', 'username': 'u1', 'password': 'cisco'}
router2 = {'hostname': '10.1.1.20','port': '22', 'username': 'u1', 'password': 'cisco'}
router3 = {'hostname': '10.1.1.30','port': '22', 'username': 'u1', 'password': 'cisco'}

routers = [router1, router2, router3]

for router in routers:
    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    shell = ssh_client.invoke_shell()

    shell.send('end\r\n')
    #shell.send('show ip int brief\r\n')
    #shell.send(f'enable\r\n')
    #shell.send(f'cisco\r\n') #this is the enable password
    shell.send(f'conf t\r\n')
    shell.send(f'router ospf 1\r\n')
    shell.send(f'net 0.0.0.0 0.0.0.0 area 0\n')
    shell.send(f'end\n')
    shell.send(f'terminal length 0\n')
    shell.send(f'show ip protocols\n')
    time.sleep(2)

    output = shell.recv(10000).decode()
    print(output)

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()