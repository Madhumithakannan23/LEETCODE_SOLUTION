class Solution:
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(index, parts, path):
            if parts == 4:
                if index == len(s):
                    result.append(".".join(path))
                return

            for length in range(1, 4):
                if index + length > len(s):
                    break

                part = s[index:index + length]

                if len(part) > 1 and part[0] == '0':
                    continue

                if int(part) <= 255:
                    path.append(part)
                    backtrack(index + length, parts + 1, path)
                    path.pop()

        if 4 <= len(s) <= 12:
            backtrack(0, 0, [])

        return result