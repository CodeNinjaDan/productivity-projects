import smtplib
import datetime as dt
import random
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")

now = dt.datetime.now()
day_of_week = now.weekday()
# set_own_date = dt.datetime(year=, month=, day=)

if day_of_week == 2:
    with open('quotes.txt', 'r') as file:
        quotes_list = file.readlines()
    # Remove any trailing newline characters
    quotes_list = [quote.strip() for quote in quotes_list]

    random_quote = random.choice(quotes_list)

    # Create the email message
    subject = "Daily Monday"
    body = random_quote
    msg = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls() #Makes the connection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=receiver_email, msg=msg)
