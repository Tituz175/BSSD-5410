####################
# Question 4
# Generate an array of 200 random integers instead of the hardcoded arr and rerun your program.
####################
# linear search Code taking from:
# url https://www.geeksforgeeks.org/linear-search/
# Binary search Code taking from:
# url https://www.geeksforgeeks.org/binary-search/
# on: 01/17/2023
# license: Share-alike
# url https://www.geeksforgeeks.org/copyright-information/?ref=footer
# Changelog:
# - combine driver code to one
# - change the array data to random array
# - add a counter to count operation for individual algorithms
# - add timer code to time individual algorithms
####################

# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1


def search(arr, N, x):
    operations = 0
    for i in range(0, N):
        operations += 1
        if (arr[i] == x):
            print("Linear ops:", operations)
            return i
    print("Linear ops:", operations)
    return -1


# Python3 code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1


def binarySearch(arr, l, r, x):
    operations = 0
    while l <= r:
        operations += 1
        mid = l + (r - l) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            print("Binary ops: ", operations)
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    print("Binary ops: ", operations)
    return -1


import random
def genrateRandomInt():
    randomInt = []
    for num in range(200):
        randomInt.append(random.randint(1,100))
    return randomInt


# Driver Code
if __name__ == "__main__":
    arr = genrateRandomInt()
    x = 10
    N = len(arr)

    import timeit

    iter = 10
    lineartime = timeit.timeit(lambda: search(arr, N, x), setup="from __main__ import search", number=iter)
    binarytime = timeit.timeit(lambda: binarySearch(arr, 0, len(arr) - 1, x), setup="from __main__ import binarySearch",
                               number=iter)

    print("Linear search took:", lineartime)
    print("Binary search took:", binarytime)

    # Search function call
    result = search(arr, N, x)
    if (result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)

    # Binary function call
    result = binarySearch(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")