import paramiko
from scp import SCPClient

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.1.112', port=22, username='x', password='x', allow_agent=False, look_for_keys=False)

scp = SCPClient(ssh_client.get_transport())
#copy a single file
scp.put('configure_ssh_cisco.txt', '/tmp/cisco.txt')
#copy a directory
#scp.put('directory', recursive=True, remote_path='/tmp') #it will copy whole directory into tmp folder
#get files from other machine
scp.get('/etc/passwd', 'passwd') #it will copy file to this directory

scp.close()