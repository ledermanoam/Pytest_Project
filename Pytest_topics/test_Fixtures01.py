import pytest
@pytest.fixture()
def setup_list():
    print('\n in Fixtures.. \n')
    city = ['NY','London','Singapore','Mumbai','TLV']
    return city

def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'NY'
    assert setup_list[::2] == ['NY','Singapore','TLV']

def myReverse(lst):
    lst.reverse()
    return lst

def test_reveresList(setup_list):
    assert setup_list[::-2] == ['TLV','Singapore','NY']
    assert setup_list[::-1] == myReverse(setup_list)