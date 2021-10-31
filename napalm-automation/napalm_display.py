from napalm import get_network_driver
import json #optional

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is the enable password
ios = driver('10.1.1.10', 'u1', 'cisco', optional_args=optional_args)
ios.open()
#start your code

output = ios.get_arp_table()
for item in output:
    print(item)

dump = json.dumps(output, sort_keys=True, indent=4) #sort_keys and indent to sort it
#print(dump)  #optional dump to save in json

with open('arp.txt', 'w') as f:
    f.write(dump)  #save dump in file

#end your code
ios.close()