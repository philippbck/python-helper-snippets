import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://web-url.com/api/"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': "Basic username:password"
    }

response = requests.get(url, headers=headers, verify=False)

print(response.text)