from fabric import Connection
from datetime import datetime
import os

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

def main():
    remote=connection_serveur_ssh(SSH_key,ip):
    dump_name = f"dump_{datetime.now().strftime('%d-%m-%Y_%H-%M')}.sql"
    remote_path = f"/tmp/{dump_name}"
    local_dir = os.path.expanduser("~/backup")
    local_path = os.path.join(local_dir, dump_name)
    os.makedirs(local_dir, exist_ok=True)
    remote.run(f"mysqldump -u bilou -p'mdp' error_access > {remote_path}")
    remote.get(remote_path, local=local_path)
    remote.run(f"rm {remote_path}")
    print("Dump bien sauvegardé sous :", local_path)

if __name__ == "__main__":
    main()