# Loop through array
# Keep in mind i, J , i = start, j = current
# keep moving j until a duplicate is found 
# Add elements to a store until a duplicate is found
# if duplicate is found, remove an item from store at position 0
# increment i(start position by 1)
# continue while  j < len array

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        j = 0
        maxl = 0
        cstrl = 0
        store  = []

        while( j < len(s)):
            
            if(s[j] in store ):
                i += 1
                store.pop(0)

            else:
                store.append(s[j])
                cstrl = (j - i) + 1
                maxl = max(maxl, cstrl)
                j += 1
        return maxl

solution = Solution()
print(solution.lengthOfLongestSubstring(" ") )  