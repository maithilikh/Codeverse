class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        tbr = []
        for i in lists:
            if i:
                p = i
                while p:
                    tbr.append(p.val)
                    p = p.next
        if not tbr:
            return None 
        else:
            tbr.sort()
        h = ListNode(tbr[-1], None)
        for j in range(len(tbr)-2, -1, -1):
            q = ListNode(tbr[j], h)
            h = q
        return h
