





def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])


productOfArray([1,2,3])