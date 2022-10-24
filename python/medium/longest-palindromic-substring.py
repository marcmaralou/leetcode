# Given a string s, return the longest palindromic substring in s.
# A string is called a palindrome string if the reverse of that string is the same as the original string.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
  
# Example 2:
# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            
            return s[l + 1:r]

        output = ''
        for i in range(len(s)):
            x = helper(i, i + 1)

            if len(x) > len(output):
                output = x
            x = helper(i, i)

            if len(x) > len(output):
                output = x
        
        return output
