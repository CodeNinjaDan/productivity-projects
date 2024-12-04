import datetime as dt
import random
import pandas
import smtplib
import os

from dotenv import load_dotenv

load_dotenv()

# Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_month = now.month
current_day = now.day

birthdays_df = pandas.read_csv('birthdays.csv')
for index, row in birthdays_df.iterrows():
    if row['month'] == current_month and row['day'] == current_day:

        # 3. If step 2 is true, pick a random letter from letter templates
        # and replace the [NAME] with the person's actual name from birthdays.csv

        #Specify the path to the subdirectory containing the .txt files
        txt_directory = '../birthday_wisher_app/letter_templates'
        #List all .txt files in the directory
        txt_files = [file for file in os.listdir(txt_directory) if file.endswith('.txt')]
        #Randomly select one of the files
        selected_file = random.choice(txt_files)
        #Join the subdirectory path to the file name to get the full path
        selected_file_path = os.path.join(txt_directory, selected_file)

        # Read the content of the selected file
        with open(selected_file_path, 'r') as file:
            content = file.read()

        new_content = content.replace('[NAME]', row['name'])

        # 4. Send the letter generated in step 3 to that person's email address.
        my_email = os.getenv("MY_EMAIL")
        password = os.getenv("PASSWORD")
        receiver_email = row['email']

        if not my_email or not password:
            raise ValueError("Email or password environment variables are not set.")

        subject = "Happy Birthday!"
        body = new_content
        msg = f"Subject:{subject}\n\n{body}"
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()  # Makes the connection secure
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=receiver_email, msg=msg)

        except smtplib.SMTPAuthenticationError:
            print("Failed to login, check your email and password.")

        except Exception as e:
            print(f"An error occurred: {e}")
