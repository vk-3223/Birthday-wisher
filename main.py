from datetime import datetime
import pandas
import random
import smtplib

my_email = "YOUR_EMAIL"
password = "YOUR_PASSWORD"

today = datetime.now()
today_tuple = (today.month,today.date)
print(today_tuple)

data = pandas.read_csv("HERE_YOUR_CSV_BIRTHDAY_LIST_WITH_EMAIL")


birthdays_dict = {(data_row["month"],data_row["day"]):data_row for(index,data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],msg=f"Subject\n\n{contents}")
        print(f"you contents:{contents}")   