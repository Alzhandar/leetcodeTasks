from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res

s = Solution()
print(s.preorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3))) == [1, 2, 3]))
        