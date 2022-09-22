# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Examples:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Input: s = "God Ding"
# Output: "doG gniD"

# Constraints:
# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.

class Solution:
    def reverseWords(self, s: str) -> str:
        list = s.split()
        ans = []
        for word in list:
            ans.append(word[::-1])
        return " ".join(ans)
