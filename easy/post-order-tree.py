from typing import List, Optional

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        res = []
        for child in root.children:
            res += self.postorder(child)
        res.append(root.val)
        return res

s = Solution()
print(s.postorder(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)]) == [5, 6, 3, 2, 4, 1]))
