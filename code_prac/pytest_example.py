
import pytest

def user_add(x, y, z):
    return x+y+z

@pytest.mark.parametrize ("x,y,z,expected", [(1,2,3,6),(10,2,3,15),(1,20,3,24)])
def test_user_add(x,y,z,expected):
    assert user_add(x,y,z) == expected

if '__name__' == '__main__':
    test_user_add()