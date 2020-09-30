# 2 sum intends to see if 2 numbers in an array can sum up to a target number
# Constraints. no element is repeated , elements are sorted

# Sample Array [-1, 3, 6, 11]
# Sample Target 9

#Algorithm
#Start from both array ends i, j
# Add i and j
# check if sum = target 9
# if so return i,j
# if sum is > reduce j by 1
# if sum is < increase i by 1

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        i = 0
        j = len(nums) - 1

        for k in range(len(nums)):
            sum = nums[i] + nums[j]
            if sum == target :
                return [i, j]
            elif sum > target :
                j -= 1
            else :
                i += 1
            
#Time complexity O(n)
# Space complexity O(1) 
solution = Solution()

print(solution.twoSum( [-1, 3, 6, 11], 9))