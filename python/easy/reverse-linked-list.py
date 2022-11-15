# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
  
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
  
# Example 3:
# Input: head = []
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ITERATIVE SOLUTION
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#        [1,2,3,4,5]
#       p c t
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
