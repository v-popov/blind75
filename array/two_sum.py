# https://leetcode.com/problems/two-sum/

# nums -> [2, 6, 7, 4]
# target -> 9

# Iterating over elements
# num=2 -> another number should be diff=(9-2)=7. 
# It could appear only after the current num, since 2 is the first number in the array.
# We will store the difference and the position of the current element in a hash map,
# unless this element equals to the difference that we've observed before.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i, num in enumerate(nums):
            if num in differences:
                return differences[num], i
            else:
                differences[target - num] = i
