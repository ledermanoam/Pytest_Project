import requests, json

baseURI = "https://petstore.swagger.io/v2/pet/"
petID = "191"

# test valid response or response is not empty
def test_getPetByID_response():
    url = baseURI + petID
    header = {"content-type" : "application/json"}
    print("RequestedURL:",url)
    response = requests.get(url,verify=False,headers=header)
    data = response.json()
    print(json.dumps(data, indent=3))
    assert len(data) > 0, "empty response"

# Testing response body for "ID" key
def test_getPetById_id():
    url = baseURI + petID
    header = {"content-type": "application/json"}
    print("RequestedURL:", url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    assert data['id'] == 191

# create Post req
def test_add_newPet():
    url = baseURI
    header = {"content-type": "application/json"}
    payload = {'id':192,'name':'cutie','status':'available'}
    response = requests.post(url,verify=False,json=payload, headers=header)
    data = response.json()
    assert data['id'] == 192
    assert len(data) > 0
    print(data)






