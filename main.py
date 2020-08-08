import time
import paramiko

HOST = '192.168.0.104'
USER = 'jcflores'

from getpass import getpass

if __name__ == '__main__':
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy( paramiko.AutoAddPolicy())

    password = getpass('Ingrese su contraseña: ')
    client.connect(HOST, username=USER, password=password)

    stdin, stdout, stderr = client.exec_command('sudo sosreport --batch')

    time.sleep(2)

    result = stdout.read().decode()

    stdin, stdout, stderr = client.exec_command('sudo chmod 777 /var/tmp/sosreport*')

    time.sleep(5)
    

    #print(result)

    result1 = result.split()
    buscar = '/var/tmp/sosreport'
    res = [i for i in result1 if buscar in i] 
    file_destino = ''.join(res)
    file_origen = file_destino.replace("/var/tmp","/home/jcflores")
    print("Esto salio --> ", file_destino)
    print("Esto salio --> ", file_origen)


    sftp_client = client.open_sftp()

    sftp_client.get(
           file_destino, 
           file_origen 
            )


    client.close()
