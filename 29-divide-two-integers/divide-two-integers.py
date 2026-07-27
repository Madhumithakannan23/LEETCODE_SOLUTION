class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31

        if dividend == MIN and divisor == -1:
            return MAX

        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        answer = 0

        while dividend >= divisor:
            temp = divisor
            count = 1

            while dividend >= temp + temp:
                temp = temp + temp
                count = count + count

            dividend = dividend - temp
            answer = answer + count

        return sign * answer