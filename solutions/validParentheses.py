class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        if len(s) % 2 == 1:
            return False

        for c in s:
            if c in pairs.keys():
                print("ap")
                stack.append(c)
            elif len(stack) > 0 and pairs.get(stack[-1]) == c:
                print("pop")
                stack.pop()
            else:
                return False
        return len(stack) == 0