class Solution(object):
    def isValid(self, s):
        mp = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for x in s:
            if stack == []:
                stack.append(x)
            else:
                if stack[len(stack)-1] not in mp:
                    return False
                if mp[stack[len(stack)-1]] == x:
                    stack.pop()
                else:
                    stack.append(x)
        return stack == []

