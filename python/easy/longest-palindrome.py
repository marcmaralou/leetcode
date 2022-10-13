# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
  
# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        length = 0
        odds = []

        for letter in counter:
            if counter[letter] % 2 == 0:
                length += counter[letter]
            else:
                odds.append(counter[letter])
        
        if odds:
            maxi = max(odds)
            length += maxi
            odds.remove(maxi)
            for odd in odds:
                length += (odd - 1)
        
        return length
