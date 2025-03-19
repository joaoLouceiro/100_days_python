import smtplib
import datetime as dt
import pandas
import random

##################### Extra Hard Starting Project ######################

EMAIL = "***REMOVED***"
PASSWORD = "***REMOVED***"

smtp_connection = smtplib.SMTP(host="***REMOVED***", port=***REMOVED***)
smtp_connection.starttls()
smtp_connection.login(user=EMAIL, password=PASSWORD)


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_month = now.month
current_day = now.day
data = pandas.read_csv("birthdays.csv")
birthday_boy = data.loc[(data["month"] == current_month) & (data["day"] == current_day)]


for (index, row) in birthday_boy.iterrows():
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        message = letter.read().replace("[NAME]", row["name"])
        smtp_connection.sendmail(from_addr=EMAIL, to_addrs=row["email"], msg=f"Subject: Happy Birthday!\n\n{message}".encode("utf-8"))

smtp_connection.close()

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




