def isPalindrome(text):

    reversed_text=''

    for i in range(len(text)):
        reversed_text = text[i] + reversed_text
    
    if text == reversed_text:
        return True
    else:
        return False



