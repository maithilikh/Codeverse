class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ln = len(nums)
        if ln == 1:
            if nums[0] == target:
                return 0 
            else:
                return -1
        else:
            l, r = 0, ln-1, 
            while l < r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                elif nums[mid] > target:
                    r = mid-1
                elif nums[mid] < target:
                    l = mid + 1
            return -1
