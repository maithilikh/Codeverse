class Solution:
    import heapq
    def sortArray(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        if ln == 1:
            return nums
        else:            
            tbr = []
            heapq.heapify(nums)
            # print(nums, type(nums))
            for _ in range(ln):
                tbr.append(heapq.heappop(nums))
            return tbr
