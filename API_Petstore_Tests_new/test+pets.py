from utils.myUtills import getAPIData

baseURI = "https://petstore.swagger.io/v2/pet/"
petID = "191"

def test_getPetByID_response():
    url = baseURI + petID
    data = getAPIData(url)
    assert data['id'] == int(petID)