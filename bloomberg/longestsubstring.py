# Find the length of the longest substring within a sequence without repeating characters
#example input abccabc
#returns 3 len(abc)
# loop through string
# keep track of start position
# intialize an empty list 
# add  characters to list as you loop
# if an encountered char is already in dict 
# get length of dict, store as longest
# continue, starting from start position + 1
# continue if start position is < len input

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        estart = 0
        istart = 0
        limit = len(s)
        store = []
        longest = 0
        while(istart < limit):
           
           if s[istart] in store:
               store = []
               istart = estart + 1
               estart += 1 
               
           else:
                store.append(s[istart])
                istart += 1

           if len(store) > longest:
                longest = len(store)
           
        return longest
#test position 3

sol = Solution()

print(sol.lengthOfLongestSubstring(" "))