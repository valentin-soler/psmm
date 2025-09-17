import mysql.connector


conn = mysql.connector.connect(
    host="192.168.157.140",
    user="bilou",
    password="", #A changé avec votre mdp
    database="test"
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

print("Tables dans la base MariaDB :")
for table in tables:
    print(table[0])

cursor.close()
conn.close()