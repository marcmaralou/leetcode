# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
  
# Example 2:
# Input: strs = [""]
# Output: [[""]]
  
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list) # O(n) extra space w/ n being words in strs

        for str in strs: # O(n) time complexity for iterating through it once
            key = ''.join(sorted(list(str)))
            dict[key].append(str)
        
        return dict.values()
