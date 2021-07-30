import datetime as dt
import random
import smtplib
import pandas

MY_EMAIL = 'testing.for.python44@gmail.com'
MY_PASSWORD = '************'
YAHOO_MAIL = 'testing_for_python@yahoo.com'

birthdays = pandas.read_csv('birthdays.csv', index_col=0)

month = dt.datetime.now().month
day = dt.datetime.now().day

birthdays_dic = [{'name': row.name, 'email': row.email, 'month': row.month, 'day': row.day} for
                 (index, row) in birthdays.iterrows()]


for birthday in birthdays_dic:
    if birthday['month'] == month and birthday['day'] == day:
        with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as file:
            letter = file.read()
        letter = letter.replace('[NAME]', birthday['name'])
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(MY_EMAIL, YAHOO_MAIL, f'Subject:Happy Birthday!!\n\n{letter}')
