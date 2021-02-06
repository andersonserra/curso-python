import paramiko

username = 'your-user-here'
password = 'your-password-here'

address = open("address-list.txt")

for ip in address:
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=ip, username=username, password=password)
	stdin, stdout, stderr =  ssh_client.exec_command('df -h')
	stdin.close()
	print("Information disk from server: "+ip)
	ler_commandos = stdout.readlines()
	for line in ler_commandos:
		print(line.replace('\n',''))
	ssh_client.close()
