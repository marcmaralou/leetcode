# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "hello"
# Output: "holle"
  
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
        l, r = 0, len(s) - 1
        s2 = list(s)
        while l < r:
            if s2[l] not in vowels:
                l += 1
            if s2[r] not in vowels:
                r -= 1
            if s2[l] in vowels and s2[r] in vowels:
                s2[l], s2[r] = s2[r], s2[l]
                l += 1
                r -= 1
        return ''.join(s2)
