import requests
response = requests.get('https://www.google.com/')
print(response.text)
print(f'Status  {response.status_code}')


