# Given an integer array nums and an integer k, return the k most frequent elements within the array.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqBucket = [[] for i in range(len(nums) + 1)]

        # count number of elements into a hash map
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # iterate through kvp to create a bucket sorted list where index is the number and value is frequency
        for n, c in count.items():
            freqBucket[c].append(n)

        result = []

        # loop through frequency bucket backwards
        for i in range(len(freqBucket) - 1, 0, -1):
            # append frequency to results array
            for n in freqBucket[i]:
                result.append(n)
                # once results reaches length of k return result
                if len(result) == k:
                    return result

    
    # O(n) + O(n)
    # bucket sort