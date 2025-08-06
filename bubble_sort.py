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

