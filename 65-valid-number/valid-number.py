
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        digit = False
        dot = False
        exp = False

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                digit = True

            elif ch == '.':
                if dot or exp:
                    return False
                dot = True

            elif ch == 'e' or ch == 'E':
                if exp or not digit:
                    return False
                exp = True
                digit = False

            elif ch == '+' or ch == '-':
                if i != 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False

            else:
                return False

        return digit
