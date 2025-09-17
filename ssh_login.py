#pip install fabric ou le paquet python-fabric (dans les dépots AUR sur Arch) / python3-fabric (Debian)
from fabric import Connection

def choix_serveur():
    choix=0
    resp=["1","2","3"]
    ip=["192.168.157.136","192.168.157.138",""]
    while choix not in resp :
        choix=str(input("Quel est le serveur de destination (1-> FTP, 2-> Web, 3-> SQL)"))
    return ip[choix-1]
