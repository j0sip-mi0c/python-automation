from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is enable password
ios = driver('10.1.1.10', 'u1', 'cisco', optional_args=optional_args)
ios.open()
#start your code

print(dir(ios))

#end your code
ios.close()