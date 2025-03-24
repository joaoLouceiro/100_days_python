import datetime

import requests
# create user

USERNAME = "jjtesttestjj2"
TOKEN = "ijwqer1243jgf4"

pixela_url = "https://pixe.la/"
pixela_user_endpoint = "v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# req = requests.post(url=pixela_url+pixela_create_user_endpoint, json=user_params)

pixela_graph_endpoint = f"{pixela_url}/v1/users/{USERNAME}/graphs"

graph_id ="graph1"

graph_params = {
    "id": graph_id,
    "name": "Programming Time Graph",
    "unit": "Hours",
    "type": "int",
    "color": "shibafu"
}

headers={"X-USER-TOKEN": TOKEN}

# req = requests.post(url=pixela_graph_endpoint, headers={"X-USER-TOKEN": TOKEN}, json=graph_params)

date = datetime.date.today().strftime("%Y%m%d")
print(date)
pixel_params = {
    "date": date,
    "quantity": str(1)
}

url=f"{pixela_url}{pixela_user_endpoint}/{USERNAME}/graphs/{graph_id}"
print(url)

req = requests.post(url, json=pixel_params, headers=headers)
print(req.text)

