class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s 
        return res

    # "4#leet4#code"
    # O(n)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        # iterate through string
        while i < len(s):
            # set second index to start of word pre delimeter
            j = i
            # loop through until reaching the delimeter
            while s[j] != '#':
                j += 1
            # length = encoded int length of word parsed back to int
            length = int(s[i:j])
            # set i to start of word
            i = j + 1
            # set j to end of word
            j = i + length
            # append word to result array
            res.append(s[i:j])
            # set i to start at end of parsed word
            i = j
            
        return res

    # O(n) 