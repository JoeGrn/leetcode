# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # intitalise results array with 1 
        res = [1] * (len(nums))

        # loop through array set cur index to be sum of prefix and nums[i]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # loop through array backwards set cur to be sum of previously stored prefix and postfix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

        # O(n)