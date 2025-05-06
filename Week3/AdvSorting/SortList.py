# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2, head3, arr, p = head, head, head, [], 0
        while head1:
            arr.append(head1.val)
            head1 = head1.next
        arr.sort()
        while head2:
            head2.val = arr[p]
            p += 1
            head2 = head2.next
        return head3
