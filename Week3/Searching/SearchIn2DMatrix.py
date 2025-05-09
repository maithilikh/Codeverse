class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix = [j for i in matrix for j in i]
        if len(matrix) < 2:
            return matrix[0] == target
        else:
            l, r = 0, len(matrix)-1
            while l < r:
                mid = (l+r)//2
                # print(matrix[l], matrix[r], matrix[mid])
                if target in [matrix[mid], matrix[l], matrix[r]]:
                    return True
                elif matrix[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
