# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        else:
            tbr, fast, slow = head, head.next, head
            while fast.next and fast.next.next:
                # print(fast.val, slow.val)
                fast = fast.next.next
                slow = slow.next            
            slow.next = slow.next.next
            return tbr
