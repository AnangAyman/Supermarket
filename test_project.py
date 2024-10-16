from project import checkLoginCode, getUserName, enterToContinue

def test_checkLoginCode():
    # False codes
    assert checkLoginCode("mockdata.csv", "000000") == False
    assert checkLoginCode("mockdata.csv", "111111") == False
    assert checkLoginCode("mockdata.csv", "222222") == False

    # True codes
    assert checkLoginCode("mockdata.csv", "123456") == True
    assert checkLoginCode("mockdata.csv", "555666") == True
    assert checkLoginCode("mockdata.csv", "777888") == True

def test_getUserName():
    assert getUserName("mockdata.csv", "000000") == False
    assert getUserName("mockdata.csv", "111111") == False
    assert getUserName("mockdata.csv", "222222") == False

    assert getUserName("mockdata.csv", "123456") == "john doe"
    assert getUserName("mockdata.csv", "555666")  == "charlie davis"
    assert getUserName("mockdata.csv", "777888") == "diana evans"


def test_enterToContinue():
    assert enterToContinue() == None
from project import login_page
from unittest.mock import patch

def test_login_page_login():
    # Mock input to return "1" (Login)
    with patch('builtins.input', return_value='1'):
        assert login_page() == 1

def test_login_page_new_customer():
    # Mock input to return "2" (New Customer)
    with patch('builtins.input', return_value='2'):
        assert login_page() == 2

def test_login_page_exit():
    # Mock input to return "3" (Exit)
    with patch('builtins.input', return_value='3'):
        assert login_page() == 3