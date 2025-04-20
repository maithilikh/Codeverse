def isValid(self, s: str) -> bool:
    if len(s)%2==1:
        return False
    else:
        st = []
        d={'(':')', '{':'}', '[':']'}
        for i in s:
            if i in d:
                st.append(i)
            elif st == [] or i != d[st[-1]]:
                return False
            else:
                st.pop()
        if st == []:
            return True
        return False
