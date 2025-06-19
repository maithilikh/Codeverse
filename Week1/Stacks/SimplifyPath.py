class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        p, ln = 0, len(path)
        def handleStack(partStr):
            if partStr == '.':
                return                
            elif partStr == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(partStr)
                return

        while p < ln:
            temp = ""
            while p < ln and path[p] != '/':
                temp += path[p]
                p += 1
            if temp:
                handleStack(temp)
            p += 1
        if not stack:
            return '/'
        else:
            tbr = ''
            for i in stack:
                tbr += ('/'+i)
            return tbr
