# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            arr = []
            curr, tbr = head, head
            while head:
                arr.append(head.val)                
                head = head.next
            arr, i = arr[::-1], 0
            while curr:
                # print(curr.val)
                curr.val = arr[i]
                i += 1
                curr = curr.next
            return tbr
