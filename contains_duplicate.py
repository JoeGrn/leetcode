# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True

            hashset.add(i)

        return False

    # Brute Forcing
    # O(n^2) Time
    # O(1) Space

    # Sort then compare
    # O(nlogn)
    # O(n) Space used by sorting is not counted usually although it does use more memory