# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
  
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        carry = 0
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            charA = int(a[i]) if i < len(a) else 0
            charB = int(b[i]) if i < len(b) else 0

            total = charA + charB + carry
            curr = str(total % 2)
            ans = curr + ans
            carry = total // 2

        if carry == 1:
            ans = '1' + ans
        
        return ans
