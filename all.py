from typing import List

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-2) + self.fib(n-1)


class Solution:
    def palindrome_str(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


class Solution:
    def palindrome_num(self, n: int) -> bool:
        new_num = 0
        while n >= new_num:
            if (n == new_num) or (n // 10 == new_num):
                return True
            elif n < new_num:
                return False
            else:
                last_digit = n % 10
                n = n // 10
                new_num = (new_num * 10) + last_digit
        return False


class Solution:
    def check_parethesis(self, s: str) -> bool:
        stack = []
        mapping = {')' : '(', ']' : '[', '}' : '{'}
        for el in s:
            if len(stack) == 0 or el in ['(', '[', '{']:
                stack.append(el)
            else:
                if mapping[el] != stack.pop():
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        orig_size = len(nums)
        k = 0
        for i in range(orig_size):
            if i==orig_size-1 or nums[-i-2] < nums[-i-1]:
                nums.insert(0, nums[-i-1])
                k += 1
        return k


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while True:
            if i < len(strs[0]):
                current_char = strs[0][i]
                for word in strs[1:]:
                    if i >= len(word):
                        return strs[0][:i]
                    elif word[i] != current_char:
                        return strs[0][:i]
            else:
                return strs[0][:i]
            i += 1
                

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
                
        # if first few elements in nums2 are smaller than first element of nums1        
        nums1[:n] = nums2[:n]
        

                
if __name__=="__main__":
    print(Solution().merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1))
