class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp, cnt, ln = sorted(heights), 0, len(heights)
        for i in range(ln):
            if exp[i] != heights[i]:
                cnt += 1
        return cnt
