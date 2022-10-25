# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
    
# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0

        for i in range(len(s)):
            l, r = i, i
            while 0 <= l < len(s) and 0 <= r < len(s) and s[l] == s[r]:
               output += 1
               l -= 1
               r += 1

            l, r = i, i + 1
            while 0 <= l < len(s) and 0 <= r < len(s) and s[l] == s[r]:
               output += 1
               l -= 1
               r += 1

        return output
