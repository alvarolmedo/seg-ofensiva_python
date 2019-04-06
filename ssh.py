import paramiko

IP = '35.204.250.42'
USER = 'pruebaURJC'
PASSWORD = 'TallerURJC123'

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, port=22, username=USER, password=PASSWORD)
    sftp = ssh.open_sftp()
    sftp.get('./Clases.py','Clases.py')
    sftp.get('./__init__.py','__init__.py')
    sftp.close()
    ssh.close()
except KeyboardInterrupt:
    print('Fallo')