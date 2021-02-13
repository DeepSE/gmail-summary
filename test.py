import requests

payload = {'txt': "Hello"}
r = requests.post('http://localhost:3000', json=payload)
print(r.content)
