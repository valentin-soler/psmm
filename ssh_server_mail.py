import smtplib
from email.mime.text import MIMEText
from datetime import datetime

today_date=str(datetime.now())
yesterday_date=str(today_date[0:8]+str(int(today_date[8:10])-1))

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
            mail=mail+f"Il y a eux {len(log_ftp)} tentatives d'intrustion sur le serveur FTP\n"
            for log in log_ftp:
                mail=mail+f"{log} \n"
        if log_web:
            mail=mail+f"Il y a eux {len(log_web)} tentatives d'intrusion sur le serveur WEB\n"
    else:
        return "Il n'y a eu aucune tentative d'intrusion hier sur les machines FTP,WEB et SQL"





















def main():
    print("TODO")





if __name__ == "__main__":
    main()