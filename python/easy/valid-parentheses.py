# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Examples:
# Input: s = "()"
# Output: true
# Input: s = "()[]{}"
# Output: true
# Input: s = "(]"
# Output: false

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif char == '}' and len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            elif char == ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
