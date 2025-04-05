def romanToInt(self, s: str) -> int:
    p, ls, num = 0, len(s), 0
    lookDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if ls == 1:
        return lookDict[s[0]]
    else:
        for p in range(ls-1):
            if lookDict[s[p]] >= lookDict[s[p+1]]:
                num += lookDict[s[p]]
            else:
                num -= lookDict[s[p]]
        num += lookDict[s[p+1]]
        return num
