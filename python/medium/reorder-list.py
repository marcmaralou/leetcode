# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
  
# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """ 
        Do not return anything, modify head in-place instead.
        """ # O(1) space complexity, no extra space
        # finding the halfway point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # changing direction of right side
        right = slow.next
        slow.next = prev = None
        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp
        
        # splicing two sides togther
        left, right = head, prev
        while right:
            tempL, tempR = left.next, right.next
            left.next = right
            right.next = tempL
            left, right = tempL, tempR
        
        # O(n) time complexity, just iterating through linked list multiple times
