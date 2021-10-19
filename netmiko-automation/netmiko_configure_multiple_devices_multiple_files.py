from netmiko import ConnectHandler
with open('devices.txt') as f:
    devices = f.read().splitlines()

devices_list = list()

for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'u1',
        'password': 'cisco',
        'port': 22,   #optional, default 22
        'secret': 'cisco',  #optional, default ''
        'verbose': True     #optional, default False
    }

    devices_list.append(cisco_device)

print(devices_list)

for device in devices_list:
    connection = ConnectHandler(**device)

    print("Entering the enable mode...")
    connection.enable()

    file = input(f"Enter a configuration file (use valid path) for {device['host']}: ")
    output = connection.send_config_from_file(file)  #sending commands from file
    print(output)

    print(f"Closing connection to {cisco_device['host']}")
    connection.disconnect()

    print('#' * 30)