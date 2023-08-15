import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sender(konu, icerik, kullanici, alici, sifre):
    em = MIMEMultipart()
    em["From"] = kullanici 
    em["To"] = alici
    em["Subject"] = konu
    body = icerik
    em.attach(MIMEText(body, "plain"))
    
    server = smtplib.SMTP("smtp.yandex.com", 587)
    server.starttls()
    server.login(kullanici, sifre)
    text = em.as_string()
    server.sendmail(kullanici, alici, text)
    server.quit()

if __name__ == "__main__":
    try:
        file = open("config.json", encoding="utf-8")
        config = json.load(file)
        file.close()

        sender_mail = config["sender_email"]
        sender_pwd = config["sender_pwd"]

        sender("Test email", "merhabaaalar", sender_mail, "gönderceğiniz kişinin epostası", sender_pwd)
    except Exception as e:
        print("Hata:", e)
        raise e



    








