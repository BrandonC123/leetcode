from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swap(self, node):
        if not node:
            return node
        # Swap current node
        temp_right = node.right
        node.right = node.left
        node.left = temp_right
        # Swap child nodes
        self.swap(node.left)
        self.swap(node.right)

        return node
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.swap(root)


        