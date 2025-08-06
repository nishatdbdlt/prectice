def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] =arr[j+1],arr[j]
    return arr
arr=[4,8,3,2,1]
nishat=bubble_sort(arr)
if nishat!=-1:
    print('found at ',nishat)
else:
    print(nishat)
# find the last value
def bubble_sort(arr):
    n =len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr[-1]
arr=[4,5,6,7,53,2]
nishat=bubble_sort(arr)
print(nishat)

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            return  False
    return True
print(is_sorted([4,1,9]))
