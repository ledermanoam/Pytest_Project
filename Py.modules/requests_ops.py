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
print('******************************************')
###################################################

url = 'https://httpbin.org/get'
myparams = {'key1':'noam','key2':'lederman','key3':'054797885'}
r = requests.get(url,params=myparams)
print(r.url)



for key, value in r.json().items():
    print(key,":",value)
print(r.json()["headers"]["Host"])


