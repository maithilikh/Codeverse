def longestConsecutive(self, nums: List[int]) -> int:
    if nums == []:
        return 0
    else:
        maxLength, tempLength = 0, 0
        nums = sorted(list(set(nums)))
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                tempLength += 1
            else:
                maxLength = max(maxLength, tempLength+1)
                tempLength = 0
        return max(tempLength+1, maxLength)
