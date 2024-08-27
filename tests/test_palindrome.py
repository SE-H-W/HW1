
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from main import isPalindrome

def test_pass():
    assert isPalindrome('HowwoH')==True

def test_fail():
    assert isPalindrome('1331')==False

