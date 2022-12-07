# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
# Please implement encode and decode

# Example 1:
# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation: One possible encode method is: "lint:;code:;love:;you"
  
# Example 2:
# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation: One possible encode method is: "we:;say:;:::;yes"

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        output = ''
        
        for str in strs: # O(n) time complexity, maybe n^2 since it copies over string? idk, no extra space except for output
          output += str(len(str)) + '#' + str
          
        return output

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        output, i = [], 0
        
        while i < len(str): # O(n) time complexity, iterating over once, no extra space except for output
          j = i
          
          while str[j] != '#':
            j += 1
          length = int(str[i:j]
          output.append(str[j + 1:j + 1 + length])
          
          i = j + 1 + length
         
        return output
          
          
          
