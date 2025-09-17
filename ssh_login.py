#pip install fabric ou le paquet python-fabric (dans les dépots AUR sur Arch) / python3-fabric (Debian)
from fabric import Connection

SSH_key=''
def choix_serveur():
    choix=0
    resp=["1","2","3"]
    ip=["192.168.157.136","192.168.157.138","192.168.157.140"]
    while choix not in resp :
        choix=str(input("Quel est le serveur de destination (1-> FTP, 2-> Web, 3-> SQL)"))
    return ip[choix-1]

def connection_serveur(key,ip):
    c = Connection(
        host=ip
        user="monitor"
        connect_kwargs={
            "key_filename": key
        }
    )
    return c