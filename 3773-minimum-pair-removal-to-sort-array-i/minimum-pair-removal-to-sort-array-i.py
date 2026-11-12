
class Solution:
    def minimumPairRemoval(self, nums):
        count = 0

        while nums != sorted(nums):
            min_sum = float('inf')
            index = 0

            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]

                if s < min_sum:
                    min_sum = s
                    index = i

            nums[index] = min_sum
            nums.pop(index + 1)

            count += 1

        return count
