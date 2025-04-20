def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    leni = len(intervals)
    if leni == 1:
        return intervals
    else:
        intervals.sort()
        toBeReturned, tempStart, tempEnd= [], intervals[0][0], intervals[0][1]
        for i in range(leni-1):
            if intervals[i+1][1] < tempEnd:
                continue
            elif intervals[i+1][0] > tempEnd:
                toBeReturned.append([tempStart, tempEnd])
                tempStart = intervals[i+1][0]
                tempEnd= intervals[i+1][1]
            else:
                tempEnd= intervals[i+1][1]
        toBeReturned.append([tempStart,tempEnd])
        return toBeReturned
