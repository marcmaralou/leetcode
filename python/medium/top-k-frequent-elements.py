# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
  
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums)
        listOfLists = [[] for i in range(len(nums) + 1)]

        for key, v in dict.items():
            listOfLists[v].append(key)
        
        output = []
        for i in range(len(listOfLists) - 1, 0, -1):
            for x in listOfLists[i]:
                output.append(x)
                if len(output) == k:
                    return output
