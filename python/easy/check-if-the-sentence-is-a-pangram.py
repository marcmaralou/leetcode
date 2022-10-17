# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Example 1:
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
  
# Example 2:
# Input: sentence = "leetcode"
# Output: false

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set()
        for letter in sentence:
            letters.add(letter)

        if len(letters) == 26:
            return True
        else:
            return False
