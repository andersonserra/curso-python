#!/usr/bin/python3 -d
import os
import paramiko

#if range network /24
#iprange = list(range(1,254)) #then use object iprange like parameter loop for.

#routers < file in same folder with address informations, suggestion... store values in many lines. In this case filename is "enderecos"
routers = open("enderecos")


#Username and Password
user = "type-user-here"
passw = "type-password-here"


for ip in routers:
   print("Verify ICMP Status IP: "+ip+"...")
   resposta = os.system("ping -c 5 " + ip + "> /dev/null")
   if resposta == 0:
      print(ip+" - Status ICMP OK")
      print("Running backup process - "+ip)
      ssh_client = paramiko.SSHClient()
      ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      ssh_client.connect(hostname=ip,port=2222,username=user,password=passw)
      stdin,stdout,stderr = ssh_client.exec_command("export terse")
      list = stdout.readlines()
      output = [line.rstrip() for line in list]
      #print (''.join(output))
      #This part is very essential to file format and prevent memory trush...
      file = open('backup-{}'.format(ip.strip()), '+w')
      file.write('\n'.join(output))
      file.close()

else:
   print(ip+" - Status ICMP PROBLEM")


