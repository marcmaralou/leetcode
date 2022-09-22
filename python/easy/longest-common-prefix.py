# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        minLen = len(strs[0])
        for i in range(1, len(strs)):
            minLen = min(minLen, len(strs[i]))
        for i in range(0, minLen):
            curLet = strs[0][i]
            for j in range(0, len(strs)):
                if strs[j][i] != curLet:
                    return pre
            pre += curLet
        return pre 
