from file import isPalindrome
import pytest

def test_pass():
    assert isPalindrome('HowwoH')==True

def test_fail():
    assert isPalindrome('1331')==False

if __name__=="__main__":
    pytest.main()
