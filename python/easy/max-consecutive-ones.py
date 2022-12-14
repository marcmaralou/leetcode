# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
  
# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pointer, consecutive, maxi = 0, 0, 0

        while pointer < len(nums):
            if nums[pointer] == 1:
                consecutive += 1
                pointer += 1
            else:
                maxi = max(maxi, consecutive)
                consecutive = 0
                pointer += 1
        
        return max(consecutive, maxi)
