# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_node(self, node1, node2):
        if not node1 and not node2: 
            return True # Loop all the way to bottom
        if (node1 and not node2) or (not node1 and node2):
            return False
        if node1.val != node2.val:
            return False
        
        left_result = self.check_node(node1.left, node2.left)
        right_result = self.check_node(node1.right, node2.right)

        return left_result and right_result

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check_node(p, q)
        