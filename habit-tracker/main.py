import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

"""
This is a guide on how to get started using the pixela api for tracking.
"""

GRAPH_ID = "graph1"
username = os.getenv("PIXELA_USERNAME")
token = os.getenv("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}
header = {
    "X-USER-TOKEN": token,
}
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

today = datetime.now()
today_date = today.strftime("%Y%m%d")
update_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
update_graph_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8",
}
# response = requests.post(url=update_endpoint, json=update_graph_config, headers=header)
# print(response.text)

put_update_config = {
    "quantity": "6",
}

put_endpoint = f"{update_endpoint}/{today_date}"
# response = requests.put(url=put_endpoint, json=put_update_config, headers=header)
# print(response.text)

delete_endpoint = f"{update_endpoint}/{today_date}"
response = requests.delete(url=put_endpoint, headers=header)
print(response.text)
