from utils.myUtills import getAPIData

baseURI = "https://petstore.swagger.io/v2/pet/"
petID = "193"

def test_getPetByID_response1():
    url = baseURI + petID
    data = getAPIData(url)
    assert data[id] == int(petID)