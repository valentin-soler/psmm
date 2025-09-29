#Voir README pour l'installation de la dépendance
from fabric import Connection
import mysql.connector
import re
from datetime import datetime

SSH_key='PSMM' #Nom de la clé privé pour se connecté, cela peut être un chemin aussi.
ip='192.168.157.136' #IP du serveur SQL

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

def add_to_DB(user,ip,date,time,connection):
    cursor = connection.cursor()
    cursor.execute(
    "INSERT IGNORE INTO error_ftp (user, date, time, ip) VALUES (%s, %s, %s, %s)",
    (user, date, time, ip))
    cursor.close()

def exec_command(srv,command):
    return srv.run(command, hide=True).stdout

def convert_time(date):
    dt=datetime.strptime(date, "%a %b %d %Y")
    return dt.strftime("%Y-%m-%d")

def extract_log(logs):
    result=[]
    pattern = re.compile(r'^(?P<date>\w{3} \w{3} \d{1,2}) (?P<heure>\d{2}:\d{2}:\d{2}) (?P<annee>\d{4}) \[pid \d+\] \[(?P<user>.*?)\].*Client "(?P<ip>[\d\.]+)", "530 Login incorrect\."')
    logs_lines=logs.splitlines()
    for log in logs_lines:
        m = pattern.search(log)
        if m:
            date=convert_time(f"{m.group("date")} {m.group("annee")}")
            result.append({
                "date": date,
                "heure": m.group("heure"),
                "user": m.group("user"),
                "ip": m.group("ip")
            })
    return result

def main():
    command_log=f"sudo cat /var/log/vsftpd/vsftpd.log"
    srv_ssh=connection_serveur_ssh(SSH_key,ip)
    logfile=exec_command(srv_ssh,command_log)
    result=extract_log(logfile)
    srv_sql=connection_serveur_sql()
    for r in result:
        print(r["user"],r["ip"],r["date"],r["heure"])
        add_to_DB(r["user"],r["ip"],r["date"],r["heure"],srv_sql)
    connection_close_sql(srv_sql)

if __name__ == "__main__":
    main()