# Write a function that takes an array of integers as input, and returns the sum of all the palindromic numbers in the array. If there are no palindromic numbers in the array, the function should return 0.
#A palindromic number is a number that is the same from a reversed order. For example 122 is not a palindromic number, but 202 is one.
# For example:
# [101, 2, 85, 33, 14014] ==> 103
# [45, 21, 303, 56] ==> 303
# [12, 34, 56] ==> 0

def palindromic_number(arr):
    new_arr = []
    reversed_sum = 0
    for i in range(len(arr)):
        # print(num)
        new_arr.append(int(str(arr[i])[::-1])) #O(N*M) M= average of length of each number
        for n in new_arr:
            if n == arr[i]:

                reversed_sum += n
    return reversed_sum

    # return new_arr
        # if num == reversed_num:
        #     new_arr.append(reversed_num)
    # return new_arr

print(palindromic_number([101, 2, 85, 33, 14014]))






