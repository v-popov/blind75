# https://leetcode.com/problems/maximum-subarray/submissions/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0] # can't set to 0, as nums can contain negative values
        cur_sum = 0

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += num
            max_sum = max(max_sum, cur_sum)

        return max_sum



# Kadane's Algorithm (https://www.youtube.com/watch?v=86CQq3pKSUw)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_best = nums[0]
        sliding_best = nums[0]

        for i in range(1, len(nums)):
            sliding_best = max(sliding_best+nums[i], nums[i])
            global_best = max(global_best, sliding_best)

        return global_optimum
