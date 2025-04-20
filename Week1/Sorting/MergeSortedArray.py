def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Modifying nums1 in-place.
    """
    if m == 0:
        for i in range(n):
            nums1[i] = nums2[i]
        return
    elif n==0:
        return
    else:
        p1, p2, tarl = 0, 0, m+n
        while p1 < m and p2 < n:
            # print(p1, p2)
            if nums1[p1] < nums2[p2]:
                p1 += 1
                continue
            else:
                for i in range(m-1, p1-1, -1):
                    # print(i, nums1[i+1], nums1[i])
                    nums1[i+1] = nums1[i]
                nums1[p1] = nums2[p2]
                p2 += 1
                p1 += 1
                m += 1
                # print(p1, nums1)
        if m == tarl:
            return
        else:
            for i in range(m, tarl):
                nums1[i] = nums2[p2]
                p2 += 1
            return
