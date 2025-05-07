class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln == 1:
            return nums[0]
        else:
            ln = len(nums)
            l, r, mid = 0, ln-1, ln//2
            while l < r:
                if nums[mid] not in {nums[mid-1], nums[mid+1]}:
                    return nums[mid]
                elif (nums[mid] == nums[mid-1] and mid%2==1) or (nums[mid] == nums[mid+1] and mid%2==0):
                    l = mid + 1
                    mid = (l+r)//2
                else:
                    r = mid - 1
                    mid = (l+r)//2
            return nums[mid]
