from utils.myConfigParser import *
from utils.myUtills import getAPIData

baseURI = getPetAPIURL()
petID = "193"

def test_getPetByID_response1():
    url = baseURI + petID
    data = getAPIData(url)
    assert data[id] == int(petID)