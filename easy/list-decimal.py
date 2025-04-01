from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary_str = ""
        current = head

        while current:
            binary_str += str(current.val)
            current = current.next

        return int(binary_str, 2)
    
head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
s = Solution()
print(s.getDecimalValue(head))  