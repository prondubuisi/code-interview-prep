# 2 sum intends to see if 2 numbers in an array can sum up to a target number
# Constraints. no element is repeated 

# Algorithm
# create a dictionary to store array elements as a key value pair  {value:index}
# loop through array
# find matches for each arry element, where match is target - element
# if match in dictionary return current index and index for match(dictionary value)
# otherwise add element to dictionary


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        store = {}
        for i, value in enumerate(nums):
            match = target - value 
            if match in store:
                return [i, store[match]]
            else:
                store[value] = i

# time complexity 0(n)
# space complexity O(n)    
            
            

solution = Solution()

print(solution.twoSum([1,2,3], 5))

