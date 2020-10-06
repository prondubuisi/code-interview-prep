# loop through array
# add extra cokies at each array Index
# See if cookies is > than max
# Add true or false as necessary
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        
        mNum = max(candies)
        store = []
        for i in candies:
            iextra = i + extraCandies
            if iextra >= mNum:
                store.append(True)
            else:
                store.append(False)
        return store   

solution = Solution()
print(solution.kidsWithCandies([4,1,2,5],3) )    