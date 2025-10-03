from fabric import Connection
import mysql.connector
from datetime import datetime

SSH_key='PSMM' #Nom de la clé privé pour se connecté, cela peut être un chemin aussi.

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
        host="192.168.157.128", #IP du serveur SQL PC Fixe
#         host="192.168.157.140", #IP du serveur SQL PC Portable
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

def add_to_DB(machine,date,heure,cpu,ram,disk,c):
    cursor = c.cursor()
    cursor.execute("INSERT IGNORE INTO etat_sys (machine, date, heure, cpu, ram, disk) VALUES (%s, %s, %s, %s, %s, %s)",
    (machine,date,heure,cpu,ram,disk))
    cursor.close()

def script_machine(ip,type_vm):
    server_ssh=connection_serveur_ssh(SSH_key,ip)
    result=collect_stats(server_ssh)
    server_sql=connection_serveur_sql()
    result_ram=f"{result[0]}M of {result[1]}M"
    result_cpu_usage=result[2]
    result_disk=f"{result[3]} of {result[4]}"
    add_to_DB(type_vm,datetime.now.date(),datetime.now.time(),result_cpu_usage,result_ram,result_disk)
    connection_close_sql(server_sql)
    
def main():
    #Server SQL
    script_machine("192.168.157.128","SQL")
    #Server FTP
    script_machine("192.168.157.130","FTP")
    #Server WEB
    script_machine("192.168.157.129","WEB")

if __name__ == "__main__":
    main()