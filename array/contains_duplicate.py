# https://leetcode.com/problems/contains-duplicate/

# Different approaches:
# 1) Brute force: for each element iterate over oll other elements to see if a duplicate exists
# 2) Sort an array and then iterate over it just once (duplicate values will be adjacent)
# 3) Store unique elements in a set as we iterate over the array

# Solution implements approach #3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_vals = set()
        for num in nums:
            if num in unique_vals:
                return True
            unique_vals.add(num)
        return False
