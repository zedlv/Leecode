#【热题100】03-有效的括号
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or  c == "[" or c == "{":
                stack.append(c)
            elif c == ")" or  c == "]" or c == "}":
                if len(stack) == 0:
                    return False
                elif c == ")" and stack[-1] != "(":
                    return False
                elif c == "]" and stack[-1] != "[":
                    return False
                elif c == "}" and stack[-1] != "{":
                    return False
                else:
                    stack.pop()
        return not stack