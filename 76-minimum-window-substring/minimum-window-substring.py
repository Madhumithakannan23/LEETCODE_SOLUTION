
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count = {}

        for ch in t:
            count[ch] = count.get(ch, 0) + 1

        left = 0
        required = len(t)
        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in count:
                if count[ch] > 0:
                    required -= 1
                count[ch] -= 1

            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                ch = s[left]

                if ch in count:
                    count[ch] += 1
                    if count[ch] > 0:
                        required += 1

                left += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]
