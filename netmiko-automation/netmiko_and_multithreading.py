from netmiko import ConnectHandler
from datetime import datetime
import time
import threading

start = time.time()  #just to measure the time of thread

def backup(device):
    connection = ConnectHandler(**device)
    print("Entering the enable mode...")
    connection.enable()

    output = connection.send_command('show run')
    # print(output)
    prompt = connection.find_prompt()
    # print(prompt)
    hostname = prompt[0:-1]
    # print(hostname)

    from datetime import datetime

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    filename = f'{hostname}_{year}_{month}_{day}.txt'
    with open(filename, 'w') as backup:
        backup.write(output)
        print(f'Backup of {hostname} completed successfully')
        print('#' * 30)

    print(f"Closing connection")
    connection.disconnect()


with open('devices.txt') as f:
    devices = f.read().splitlines()

threads = list()
for ip in devices:
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'u1',
        'password': 'cisco',
        'port': 22,   #optional, default 22
        'secret': 'cisco',  #optional, default ''
        'verbose': True     #optional, default False
    }

    th = threading.Thread(target=backup, args=(device,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

end = time.time()
print(f"Total execution time:{end-start}")
