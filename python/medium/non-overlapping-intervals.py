# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
  
# Example 2:
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
  
# Example 3:
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() # O(nlogn)
        output = 0

        prevEnd = intervals[0][1]
        for start, end in intervals[1:]: # O(n) run time here
            if start < prevEnd:
                output += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end

        return output # no extra space
