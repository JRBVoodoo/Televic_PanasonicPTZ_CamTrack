import requests

api_url = "http://192.168.0.150:8890/CoCon/Connect"
response = requests.get(api_url)
response.json()
print(response.json())
apiID = response.json()[22:58]
api_url = "http://192.168.0.150:8890/CoCon/Notification/id=" + apiID
print(api_url)