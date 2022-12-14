# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# RECURSIVELY
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.isMirror(root, root)
    
    def isMirror(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        else:
            return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

# ITERATIVELY
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        list = [root, root]
        
        while list:
            left = list.pop(0)
            right = list.pop(0)

            if left and not right:
                return False
            if not left and right:
                return False
            if not left and not right:
                continue
            if left.val != right.val:
                return False
            
            list.append(left.left)
            list.append(right.right)
            list.append(left.right)
            list.append(right.left)

        return True
