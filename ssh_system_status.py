from fabric import Connection
import mysql.connector
from datetime import datetime

SSH_key='PSMM' #Nom de la clé privé pour se connecté, cela peut être un chemin aussi.
ip='192.168.157.140' #IP du serveur SQL

def connection_serveur_ssh(key,ip):
    c = Connection(
        host=ip,
        user="monitor",
        connect_kwargs={
            "key_filename": key
        }
    )
    return c

def connection_serveur_sql():
    c = mysql.connector.connect(
        host="192.168.157.140",
        user="",
        password="",
        database="error_access"
    )
    return c

def connection_close_sql(connection):
    connection.commit()
    connection.close()
    return 1

def collect_stats(c):
    ram_result = c.run("free -m | awk 'NR==2{print $3,$2}'", hide=True)
    ram_line = ram_result.stdout.strip()
    used_ram, total_ram = map(int, ram_line.split())
    print(used_ram)

    cpu_line = c.run('top -bn1 | grep "Cpu(s)"', hide=True).stdout
    cpu_usage = float(cpu_line.split()[1].replace(',', '.'))
    print(cpu_usage)

    disk_line = c.run("df --total -h | grep 'total'", hide=True).stdout.split()
    disk_used = disk_line[2]
    disk_total = disk_line[1]

    return used_ram, total_ram, cpu_usage, disk_used, disk_total

def main():
    server_ssh=connection_serveur_ssh(SSH_key,ip)
    print(collect_stats(server_ssh))

if __name__ == "__main__":
    main()