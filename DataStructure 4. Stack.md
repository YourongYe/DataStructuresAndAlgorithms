# Stack 应用
Check balanced parenthesis
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
```py
def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'[':']','{':'}','(':')'}
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                top = stack.pop() if stack else '0'
                if i != dic[top]:
                    return False
        return not stack
```
