# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # set left pointer to 0
        lp = 0
        # set right pointer to last index
        rp = len(s) - 1

        # loop through while pointers have not met
        while lp < rp:
            # guard for index out of bounds and check for if not alpha numerical
            while lp < rp and not self.isAlphaNumerical(s[lp]):
                # increment pointer
                lp += 1
            # guard for index out of bounds and check for if not alpha numerical
            while rp > lp and not self.isAlphaNumerical(s[rp]):
                # decrement pointer
                rp -= 1
            # if values do not match then not a Palindrome
            if s[lp].lower() != s[rp].lower():
                return False

            lp = lp + 1 
            rp = rp - 1

        # success isPalindrome
        return True
    
    def isAlphaNumerical(self, c):
        # check if ascii value of char is alpha numerical
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))

        # O(n) Time 
        # O(1) Space

# Simple Solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create empty string
        str = ""
        
        # loop through string
        for c in s:
            # check if char is alpha numerical
            if c.isalnum():
                # add to string
                str += c.lower()
                
        # return if string is equal to it's reverse
        return str == str[::-1]