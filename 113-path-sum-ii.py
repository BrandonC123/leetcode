class Solution:
    def traverse_tree(self, node, targetSum, cur_path, cur_sum, res):
        if not node:
            return

        new_sum = cur_sum + node.val
        new_path = cur_path + [node.val]

        if not node.left and not node.right: #Leaf node
            if new_sum == targetSum:
                res.append(new_path)
            return

        self.traverse_tree(node.left, targetSum, new_path, new_sum, res)
        self.traverse_tree(node.right, targetSum, new_path, new_sum, res)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.traverse_tree(root, targetSum, [], 0, res)
        return res