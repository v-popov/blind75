# https://leetcode.com/problems/product-of-array-except-self/

# Input: nums=[1,2,3,4]
# After forward pass: answer -> [1, 1, 2, 6]
# After backward pass: answer -> [24,12,8,6]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        product_to_the_left = 1 # left padding with 1
        for i in range(len(nums)): # forward pass
            # answer[i] = product of numbers
            # to the left from the current position: [0, 1, ..., i-1]
            answer.append(product_to_the_left)
            product_to_the_left *= nums[i]

        product_to_the_right = 1 # right padding with 1
        for i in range(len(nums)): # backward pass
            # multiply answer[i] by the product of the numbers
            # to the right from the current position: [i+1, i+2, ..., N]
            answer[-1-i] *= product_to_the_right
            product_to_the_right *= nums[-1-i]

        return answer
