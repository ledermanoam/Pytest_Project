import pytest

@pytest.mark.sanity
def test_a1():
    assert 5 + 5 == 10
    assert 50 > 45
    assert 4 != 3

def test_a2():
    assert "abcd" == "abcd"

def test_a3():
    assert 4*4 == 16

@pytest.mark.sanity
def test_a4():
    assert 2 in divmod(10,5)
    assert 'py' in 'this is pytest'
    assert [1,2] < [1,2,4]
@pytest.mark.strtest
def test_a5():
    assert "noam lederman" in "noam lederman is a QA from AMAT"
