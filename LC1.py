#1. Two Sum

# Given an array of integers, return indices of the two numbers such that they add 
# up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may not 
# use the same element twice.
# 
# Example:
#   
#   Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

input1 = [2,7,11,15]
target = 9

def returnTwo(input1, target):
    for i in range(len(input1)):
        input0 = input1[:i] + input1[(i+1):]
        for j in range(len(input0)):
            if((input1[i]+input0[j]) == target):
                print (input1[i], input0[j])
                break

print(returnTwo(input1,target) )