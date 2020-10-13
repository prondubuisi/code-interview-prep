# Algorithm
# loop through array from behind
# set a mark for tallest building
# see if current element is greater thn tallest building
# if it is, add as it can see the sunline
# Otherwise don't add
    
def sunline(nums):
    ts = 0
    store = []
    start = len(nums) -1
    
    while start >= 0:
        if nums[start] > ts:
            store.append(start)
            ts = nums[start]
            
        start -= 1
    return store

print(sunline([4, 1, 2, 3]))