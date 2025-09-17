# psmm
Les scripts ont été tester sous Debian 13 & Manjaro.

### Dépendense Python:
Fabric (apt install python3-fabric | pacman -S fabric) --> Client SSH
mysql-connector-python (apt install python3-mysql-connector | pacman -S python-mysql-connector) --> Client SQL

### Script :
ssh_login.py -> Connection en SSH et execution d'une commande
ssh_login_sudo.py -> Connection en SSH et execution d'une commande en sudo (sudo configurer sans demande de mot de passe)
ssh_mysql.py --> Connection au serveur SQL et liste les tables dans une base de donnée définie dans les script avec les id donnée dans le script