# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true
  
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
  
# Example 3:
# Input: s = "paper", t = "title"
# Output: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(word):
            list = []
            dict = {}
            i = 0

            for letter in word:
                if letter not in dict:
                    dict[letter] = i
                    i += 1
                list.append(dict[letter])

            return list

        return helper(s) == helper(t)
