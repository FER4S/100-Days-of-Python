import requests
import datetime as dt

USERNAME = 'feras'
TOKEN = 'xdxdxd696969'
GRAPH_ID = 'graph1'
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': '100 Days Of Python',
    'unit': 'hour',
    'type': 'float',
    'color': 'kuro',
}

headers = {
    'X-USER-TOKEN': TOKEN,
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f'{graph_endpoint}/{GRAPH_ID}'

today = dt.datetime.today().strftime('%Y%m%d')

pixel_config = {
    'date': today,
    'quantity': '150.5',
}

# response = requests.post(pixel_endpoint, headers=headers, json=pixel_config)
# print(response.text)

pixel_update_endpoint = f'{pixel_endpoint}/20210720'

pixel_update_config = {
    'quantity': '2',
}
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

response = requests.delete(pixel_update_endpoint, headers=headers)
print(response.text)
