#pip install fabric ou le paquet fabric sous Arch (dépot extra) / python3-fabric (Debian)
from fabric import Connection

SSH_key='PSMM' #Nom de la clé privé pour se connecté, cela peut être un chemin aussi.
#Choix du serveur cible:
def choix_serveur():
    choix=0
    resp=["1","2","3"]
    ip=["192.168.157.136","192.168.157.138","192.168.157.140"] #Liste d'ip à adapter a votre situation
    while choix not in resp :
        choix=str(input("Quel est le serveur de destination (1-> FTP, 2-> Web, 3-> SQL)"))
    return ip[int(choix)-1]

#Initialisation de la connection SSH
def connection_serveur(key,ip):
    c = Connection(
        host=ip,
        user="monitor",
        connect_kwargs={
            "key_filename": key
        }
    )
    return c
#Execution de commande SSH
def exec_command(srv,command):
    return srv.run(command, hide=True).stdout

#Main
def main():
    ok=True
    while ok==True:
        ip_connect=choix_serveur()
        srv_connect=connection_serveur(SSH_key,ip_connect)
        command_srv=str(input("Quel commande souhaitez-vous exectuer ?\n"))
        command_srv="sudo "+command_srv
        print(exec_command(srv_connect,command_srv))
        again=int(input("Souhaitez-vous relancer une connection ? 1--> Oui 2 --> Non"))
        if again==2:
            ok=False
    print("Au revoir")

if __name__ == "__main__":
    main()