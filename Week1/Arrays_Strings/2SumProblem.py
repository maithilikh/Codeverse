def twoSum(self, nums: List[int], target: int) -> List[int]:
    indexDict = {}
    for i in range(len(nums)):
        if target - nums[i] in indexDict:
            return [indexDict[target - nums[i]], i]
        else:
            indexDict[nums[i]] = i
    return 0
