#Reverse in-place (best for DSA)

def reverse_inplace(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1

    if l >= r:
        return

    arr[l], arr[r] = arr[r], arr[l]
    reverse_inplace(arr, l + 1, r - 1)


a = [1, 2, 3, 4, 5]
reverse_inplace(a)
print(a)  # [5, 4, 3, 2, 1]



#Return a new reversed array (simpler, but extra memory)

def reversed_copy(arr, i=0):
    if i == len(arr):
        return []
    return reversed_copy(arr, i + 1) + [arr[i]]


print(reversed_copy([10, 20, 30]))  # [30, 20, 10]
