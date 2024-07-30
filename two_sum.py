# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hash map to store previous values
        prevMap = {}

        # iterate through the list
        for i, n in enumerate(nums):
            # check if the difference is in the hash map
            diff = target - n
            if diff in prevMap:
                # return current index and index of the difference as it totals the target
                return [prevMap[diff], i]
            # store the current value in the hash map and it's index
            prevMap[n] = i 

        #   {
        #       3: 0
        #       4: 1
        #   }
        #
        #   [0, 1]

        # O(n) Time
        # O(n) Space