# my extra lines of coding way
# Time and Space - O(n)
def findMaxLength(nums):
    summ = 0
    longest_array = 0
    curr_value = 0
    sums_map = {}
    for ind,val in enumerate(nums):
        if val == 0:
            summ += -1
        else:
            summ += 1
        if summ == 0:
            curr_value = ind + 1
            longest_array = max(longest_array,curr_value)
        if summ not in sums_map:
            sums_map[summ] = ind
        else:
            curr_value = ind -sums_map[summ]
            longest_array = max(longest_array,curr_value)
    return longest_array

# Fewer lines coding
def findMaxLength(nums):
    summ = 0
    longest_array = 0
    sums_map = {}
    for ind,val in enumerate(nums):
        summ += -1 if val == 0 else 1
        if summ == 0:
            longest_array = max(longest_array,ind+1)
        elif summ not in sums_map:
            sums_map[summ] = ind
        else:
            curr_value = ind -sums_map[summ]
            longest_array = max(longest_array,curr_value)
    return longest_array
