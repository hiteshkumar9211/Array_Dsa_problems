def isPalindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1



    return True
print(isPalindrome("A man, a plan, a canal, Panama!"))  # Output: True
print(isPalindrome("racecar"))  # Output: True
print(isPalindrome("abcdcb")) 
