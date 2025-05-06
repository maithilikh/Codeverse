class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        tbr = 0
        for i in range(0, len(nums), 2):
            tbr += nums[i]
        return tbr
