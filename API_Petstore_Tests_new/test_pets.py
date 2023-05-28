import json
from utils.myConfigParser import *
from utils.myUtills import getAPIData,putData,deleteData
import logging
LOGGER = logging.getLogger(__name__)

baseURI = getPetAPIURL()
petID = "194"

def test_getPetByID_response():
    url = baseURI + petID
    data,resp_status,timeTaken = getAPIData(url)
    assert data['id'] == int(petID)
    assert resp_status == 200
    print('Time Taken: ', timeTaken)


#Test updating a pet
def test_updatingPet():
    payload = {'id':int(petID),'name':'Cutie','status':'pending'}
    data,resp_status,timeTaken = putData(baseURI,payload)
    LOGGER.info("API Call done")
    assert data['id'] == int(petID)
    print(data)

# Test Delete a pet
def test_deletePetById():
    url = baseURI + petID
    data,resp_status,timeTaken = deleteData(url)
    print(data)
    assert data['message'] == petID
    assert data['code'] == 200


