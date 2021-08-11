import requests
from datetime import datetime
import os

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/0d234755873eac7527f49c78ace54c64/workoutTracking/workouts'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}
nutritionix_config = {
    "query": input('Tell me which exercises you did: '),
    'gender': 'male',
    'weight_kg': 85,
    'height_cm': 180,
    'age': 20
}

response = requests.post(url=nutritionix_endpoint, headers=headers, json=nutritionix_config)

result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheety_input = {
        'workout': {
            'date': today_date,
            'time': now_time,
            'exercise': exercise["name"].title(),
            'duration': exercise["duration_min"],
            'calories': exercise['nf_calories'],
        },
    }

    sheety_response = requests.post(sheety_endpoint, json=sheety_input, auth=('feras', '100daysofpython'))
    print(response.text)
