
# 2 sum intends to see if 2 numbers in an array can sum up to a target number
# Constraints. no element is repeated 

# brute force

# Algorithm 
# Start from beginning of array 
# add numbers from beginning + 1 till the end looking for match(sum)
# if match is found return current start and index of match
# if match is not found do for next index
# repeat

arr = [3,4,2]
target = 6

def find_target1(arr, target):
   
    for i in range(len(arr)) :
        match = i + 1
        for j in range(len(arr[match:])):
            if( arr[i] + arr[match] == target) :
                return [ i, match]
            match += 1
    return 0

print(find_target1(arr, target))

# # Time complexity n2(quadratic)
# # Space complexity n

# Can this algorithm be optimized? yes

# Algorithm 

# Begin from array start position
# subtract value from target
# check if result is in array
# return  beginning index, result index
# if not found, repeat starting at next array position

def find_target2(arr, target):

    for i in arr :
        find = target - i
        search_index = arr.index(i) + 1
        if find in arr[search_index: ] :
            return [arr.index(i), arr.index(find)]
    return 0

print(find_target2(arr, target))



    

