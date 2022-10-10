# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3
  
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        majority = len(nums) // 2

        for k, v in counter.items():
            if v > majority:
                return k
              
# Follow-up: Could you solve the problem in linear time and in O(1) space?
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        counter = 1

        for i in range(1, len(nums)):
            if ans == nums[i]:
                counter += 1
            else:
                counter -= 1
                if counter == -1:
                    ans = nums[i]
                    counter = 1
        
        return ans
