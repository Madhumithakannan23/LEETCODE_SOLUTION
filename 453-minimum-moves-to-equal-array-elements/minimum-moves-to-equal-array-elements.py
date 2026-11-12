class Solution:
    def minMoves(self, nums):
        minimum = min(nums)
        moves = 0

        for i in nums:
            moves += i - minimum

        return moves