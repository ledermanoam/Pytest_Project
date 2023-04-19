import requests

url = 'https://www.google.com/search?q=pytest'
r = requests.get(url)
#print(r.status_code)
#print(r.text)
print(r.url)

url = 'https://reqres.in/api/users'
r = requests.get(url)
print(r.status_code)
print(r.headers)
print(r.request.headers)
print(r.text)
print(r.json())
print(r.headers['Content-Type'])

