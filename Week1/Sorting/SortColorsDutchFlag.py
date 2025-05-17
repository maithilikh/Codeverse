class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln, d = len(nums), {0:0, 1:0, 2:0}
        for i in range(ln):
            d[nums[i]] += 1
        for i in range(ln):
            if d[0]:
                nums[i] = 0
                d[0] -= 1
            elif d[1]:
                nums[i] = 1
                d[1] -= 1
            else:
                nums[i] = 2
        return
