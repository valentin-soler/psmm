# psmm
Les scripts ont été tester sous Debian 13 & Manjaro.

### Dépendense Python:
Fabric (apt install python3-fabric | pacman -S fabric) --> Client SSH
mysql-connector-python (Pour debian 13, utilisé le paquet dans "paquet manquant" et installer python3-protobuf | pacman -S python-mysql-connector) --> Client SQL

### Script :
ssh_login.py -> Connection en SSH et execution d'une commande
ssh_login_sudo.py -> Connection en SSH et execution d'une commande en sudo (sudo configurer sans demande de mot de passe)
ssh_mysql.py --> Connection au serveur SQL et liste les tables dans une base de donnée définie dans les script avec les id donnée dans le script
ssh_mysql_error.py --> Connection au serveur SQL et récupération des logs pour les mettres dans une BDD
ssh_ftp_error.py --> Connection au serveur FTP via SSH pour récupération des log, et stockages des tentative de connection infructueuse dans la bdd