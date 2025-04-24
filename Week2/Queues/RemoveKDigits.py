 def removeKdigits(self, num: str, k: int) -> str:
        ln = len(num)
        if k == ln:
            return "0"
        else:
