# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to set as more efficient
        numSet = set(nums)
        # create count integer
        longest = 0

        for n in numSet:
            # if n - 1 is in not in numset it is not a consecutive sequence so set longest to 1
            if(n - 1) not in numSet:
                length = 1
            # if n + length exists then increment to cosecutive squence count
                while (n + length) in numSet:
                    length += 1
            # calculate is current consecutive length > longest total then replace consecutive total
                longest = max(length, longest)

        return longest

        # O(n)
