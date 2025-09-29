import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import mysql.connector

def get_yesterday_date(date):
    return str(date[0:8]+str(int(date[8:10])-1))
today_date=str(datetime.now())
yesterday_date=get_yesterday_date(today_date)

def send_mail(mail):
    port=587 #TLS
    smtp_server = "smtp.gmail.com" #SMTP Gmail, Mot de passe d'application obligatoire
    login = "" #Adresse mail Gmail
    password = "" #Votre mot de passe d'application
    
    sender_email= "" #Mail
    receiver_email= "" #Mail de l'administrateur
    message=MIMEText(mail,"plain")
    message["Subject"] = f"Tentative d'intrusion du {yesterday_date}"
    message["From"] = sender_email
    message["To"] = receiver_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def create_mail(log_ftp,log_web,log_sql):
    mail=f"Voici les logs d'hier"
    if log_ftp and log_web and log_sql:
        #Il y a des logs présent pour un des trois
        if log_ftp:
            mail=mail+f"Il y a eux {len(log_ftp)} tentatives d'intrusion sur le serveur FTP\n"
            for log in log_ftp:
                mail=mail+f"{log} \n"
        if log_web:
            mail=mail+f"Il y a eux {len(log_web)} tentatives d'intrusion sur le serveur WEB\n"
            for log in log_web:
                mail=mail+f"{log} \n"
        if log_sql:
            mail=mail+f"Il y a eux {len(log_sql)} tentatives d'instrusion sur le serveur SQL\n"
            for log in log_sql:
                mail=mail+f"{log} \n"
    else:
        return "Il n'y a eu aucune tentative d'intrusion hier sur les machines FTP,WEB et SQL"

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

def get_log(type_srv,date,connection):
    cursor = connection.cursor()
    if type_srv == "ftp":
        cursor.execute("SELECT * FROM error_ftp WHERE date = %s", (date,))
    elif type_srv == "sql":
        cursor.execute("SELECT * FROM error_sql WHERE date = %s", (date,))
    elif type_srv == "web":
        cursor.execute("SELECT * FROM error_web WHERE date = %s", (date,))
    result=cursor.fetchall()
    cursor.close()
    return result

















def main():
    print("TODO")





if __name__ == "__main__":
    main()