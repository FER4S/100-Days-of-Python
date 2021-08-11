import requests


class DataManager:
    def __init__(self):
        self.get_endpoint = 'https://api.sheety.co/0d234755873eac7527f49c78ace54c64/flightDeals/prices'
        self.put_endpoint = 'https://api.sheety.co/0d234755873eac7527f49c78ace54c64/flightDeals/prices/'

    def get_sheet(self):
        response = requests.get(self.get_endpoint)
        response.raise_for_status()
        return response.json()['prices']

    def put_sheet(self, obj):
        id = obj['id']
        obj_config = {
            'price': {
                'city': obj['city'],
                'iataCode': obj['iataCode'],
                'lowestPrice': obj['lowestPrice'],
                'id': obj['id']
            }
        }
        response = requests.put(f'{self.put_endpoint}{id}', json=obj_config)
        response.raise_for_status()
