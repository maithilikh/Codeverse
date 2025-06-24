def evalRPN(self, tokens: List[str]) -> int:
        ln = len(tokens)
        if ln == 1:
            return int(tokens[0])
        else:
            stack, ops = [], {'+', '-', '*', '/'}
            for i in range(ln):
                if tokens[i] in ops:
                    op = tokens[i]
                    on1 = stack.pop()
                    on2 = stack.pop()
                    k = eval(on2 + op + on1)
                    if op == '/' and k < 0:
                        stack.append(str(math.ceil(k)))
                    else:
                        stack.append(str(math.floor(k)))
                else:
                    stack.append(tokens[i])
            return int(stack[-1])
