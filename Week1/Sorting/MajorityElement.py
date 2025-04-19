def majorityElement(self, nums: List[int]) -> int:
    ln = len(nums)
    tarc, d = ln//2, {}
    for i in nums:
        if i in d:
            d[i] += 1
            if d[i] > tarc:
                return i
        else:
            d[i] = 1
    return i
