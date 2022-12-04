# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)
# (0,8),(8,10) is not conflict at 8

# Example 1:
# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: 2
# Explanation:
# We need two meeting rooms
# room1: (0,30)
# room2: (5,10),(15,20)
  
# Example 2:
# Input: intervals = [(2,7)]
# Output: 1
# Explanation: 
# Only need one meeting room

from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        output, count, sp, ep = 0, 0, 0, 0
        
        while sp < len(intervals):
          if start[sp] < end[ep]:
            sp += 1
            count += 1
          else:
            ep += 1
            count -= 1
          
          output = max(output, count)
        
        return output
        

# TIME COMPLEXITY: O(nlogn) # sorting x2 plus O(n) for the while loop
# SPACE COMPLEXITY: O(n) # for start and end arrays, intervals/2 * 2
