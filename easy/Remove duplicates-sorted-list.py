from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next


        return head
    
s = Solution()
print(s.deleteDuplicates([1,1,2,3,3]))

# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __str__(self):
#         result = []
#         current = self
#         while current:
#             result.append(str(current.val))
#             current = current.next
#         return " -> ".join(result)

# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return head

#         current = head

#         while current and current.next:
#             if current.val == current.next.val:
#                 current.next = current.next.next
#             else:
#                 current = current.next

#         return head

# def create_linked_list(values):
#     if not values:
#         return None
#     head = ListNode(values[0])
#     current = head
#     for val in values[1:]:
#         current.next = ListNode(val)
#         current = current.next
#     return head

# s = Solution()

# input_list = [1, 1, 2, 3, 3]
# head = create_linked_list(input_list)

# result = s.deleteDuplicates(head)

# print(result) 