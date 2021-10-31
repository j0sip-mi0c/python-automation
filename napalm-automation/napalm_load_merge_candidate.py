from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is the enable password
ios = driver('10.10.10.1', 'u1', 'cisco', optional_args=optional_args)
ios.open()
#start your code

ios.load_merge_candidate('acl.txt')

diff = ios.compare_config()
print(diff)

#end your code
ios.close()