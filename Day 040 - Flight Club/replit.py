import os
import requests

endpoint = os.environ['SHEETY_POST_ENDPOINT']

print('Welcome to the club!')
print('We find the best flight deals and email you! ✈')
fn = input('What is your first name?\n').title()
ln = input('What is your last name?\n').title()
email = input('Enter your email please: \n').lower()
email_v = input('Enter your email again please: \n').lower()

sheety_config = {
    'user': {
        'firstName': fn,
        'lastName': ln,
        'email': email
    }
}

if email == email_v:
    response = requests.post(endpoint, json=sheety_config)
    response.raise_for_status()
    print("You're in the club!")
else:
    print('Invalid input!')
