# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
  
# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
  
# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list1, list2 = [], []
        dict1, dict2 = {}, {}

        i = 0
        for letter in pattern:
            if letter not in dict1:
                dict1[letter] = i
                i += 1
        j = 0
        listS = s.split()
        for word in listS:
            if word not in dict2:
                dict2[word] = j
                j += 1

        for letter in pattern:
            list1.append(dict1[letter])
        for word in listS:
            list2.append(dict2[word])
        
        if list1 == list2:
            return True
        else:
            return False
