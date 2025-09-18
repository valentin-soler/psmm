#Voir README pour l'installation de la dépendance
from fabric import Connection
import mysql.connector

SSH_key='PSMM' #Nom de la clé privé pour se connecté, cela peut être un chemin aussi.
ip='192.168.157.140' #IP du serveur SQL

def connection_serveu_ssh(key,ip):
    c = Connection(
        host=ip,
        user="monitor",
        connect_kwargs={
            "key_filename": key
        }
    )
    return c
def connection_serveur_sql(ip,username,passwd,tb):
    c = mysql.connector.connect(
        host=ip,
        user=username,
        password=passwd,
        table=tb
    )
    return c

def connection_close_sql(connection):
    connection.close()
    return 1

def add_to_DB(user,ip,date,time,connection):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO error (user, date, time, ip) VALUES ({user}, {date}, {time}, {ip})")
    cursor.close()

def exec_command(srv,command):
    return srv.run(command, hide=True).stdout














if __name__ == "__main__":
    main()