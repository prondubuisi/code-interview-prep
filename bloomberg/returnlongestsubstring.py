
# Algorithm 
# loop through array
# Track points along str sequence using pointers i, j'
# i for start position and j for curr pos
# have a store for non dup elements
# if duplica remove item from store
# if no dup add Item to store
# get lenth of array 
# if length is greater =  max
# save as longest string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            
        i = 0
        j = 0
        maxl = 0
        curl = 0
        maxs = ""
        store = []
        
        while(j < len(s)):
            
            if s[j] in store:
                store.pop(0)
                i += 1
                
            else:
                store.append(s[j])
                curl = j - i + 1
                maxl = max(maxl, curl )
                j += 1
                if (len(store)  >= maxl):
                    maxs = "".join(store)
        return maxs

#time complexity n, space complexity n

solution = Solution()


print(solution.lengthOfLongestSubstring("abcbd"))
