import requests, json

baseURI = "https://petstore.swagger.io/v2/pet/"
petID = "151"

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
    assert data['id'] == 151








