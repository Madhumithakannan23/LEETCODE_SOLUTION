class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0

        for i in range(len(s)):
            temp = ""

            for j in range(i, len(s)):
                if s[j] not in temp:
                    temp += s[j]
                else:
                    break

            if len(temp) > maximum:
                maximum = len(temp)

        return maximum