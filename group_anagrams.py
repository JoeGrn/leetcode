class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap where each key maps to a list 
        # key is the count of individual chars in the string
        #   {
        #       key: []
        #   }

        res = defaultdict(list)

        for s in strs:
            # create a list of 26 0's
            count = [0] * 26

            for c in s:
                # total the number of each individual char in a string
                # using the ascii value eg. ascii "a" = 80 ascii b = "81" 81-80 = index 1
                count[ord(c) - ord("a")] += 1

            # for that count array append the string
            res[tuple(count)].append(s)

        # return hash.values()
        return res.values()

        # m = len input strings
        # n = len of string
        # O(m*n*26)