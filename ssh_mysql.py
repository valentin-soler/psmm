#Voir README pour l'installation de la dépendance
import mysql.connector

#Création de la connection
conn = mysql.connector.connect(
    host="192.168.157.128",
    user="bilou",
    password="", #A changé avec votre mdp
    database="test"
)
#Connection
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
#On affiches les tables
print("Tables dans la base MariaDB :")
for table in tables:
    print(table[0])
#On ferme la connection
cursor.close()
conn.close()