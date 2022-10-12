# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
  
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = list(s)
        listT = list(t)
        listS.sort()
        listT.sort()
        if listS == listT:
            return True
        else:
            return False
