import smtplib
import pandas
import datetime as dt
import random

MY_EMAIL = "metodiganev207@gmail.com"
MY_PASSWORD = "zfse mzhi qdkr gwrc"
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for index, data_row in data.iterrows()}
if today_tuple in birthday_dict.keys():
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        new_content = content.replace("[NAME]", birthday_person["name"])

    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    #     connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Happy Birthday\n\n{new_content}")

    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=new_content)
    connection.close()
# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
