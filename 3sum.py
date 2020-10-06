# class Solution:
# Algorithm
# Have three pointers i, left and right
# loop through array using a length of array length - 2
# sum i, left, right at every loop
# if sum = 0
# add to set
# then increment left and decrease right
# if sum is > 0 decrease left
# if sum is < 0 increase right
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        store = set()
        for i in range(len(nums) - 2):
        
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    triplet = (nums[i], nums[left], nums[right])
                    store.add(triplet)
                    left += 1
                    right -= 1

                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1


        return store

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))

    