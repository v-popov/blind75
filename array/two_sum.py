# nums -> [2,7,11,15]
# target -> 9
# Iterating over elements. num=2 -> another number should be diff=(9-2)=7. It could appear
# either before the current num, or after it -> save the differences and their positions to a hashmap.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i, num in enumerate(nums):
            if num in differences:
                return differences[num], i
            else:
                differences[target - num] = i
