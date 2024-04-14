def isValid(s):
        dictionary = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c in dictionary:
                if stack and stack[-1] == dictionary[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False