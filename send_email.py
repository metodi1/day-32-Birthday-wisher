import smtplib

MY_EMAIL = "metodiganev207@gmail.com"
MY_PASSWORD = "vxem caov wxae ztmq"

connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=MY_EMAIL, password=MY_PASSWORD)
connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="ssss")
connection.close()
