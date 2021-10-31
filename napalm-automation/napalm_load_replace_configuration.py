from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is the enable password
ios = driver('10.1.1.10', 'u1', 'cisco', optional_args=optional_args)
ios.open()
#start your code

ios.load_replace_candidate(filename='config.txt')

diff = ios.compare_config()
print(diff)

#end your code
ios.close()