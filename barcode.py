from operator import index

import qrcode
data = "https://github.com/nishatdbdlt"
qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,

)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qrcode.png")

print("QR Code saved as: my_qrcode.png")

def bubble_sort(arr, target):
    n = len(arr)

    # Step 1: Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Step 2: Find all indices of the target
    indexes = []
    for i in range(len(arr)):
        if arr[i] == target:
            indexes.append(i)

    # Step 3: Return
    if indexes:
        return arr, indexes
    else:
        return arr, [-1]
arr = [3, 3, 4, 2, 4]
target = 4

sorted_arr, indices = bubble_sort(arr, target)

print("Sorted Array:", sorted_arr)
if indices != [-1]:
    print("Target found at index(es):", indices)
else:
    print("Target not found.")
from operator import index


def bubble_sort(arr, target):
    n = len(arr)

    # Step 1: Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Step 2: Find all indices of target
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)

    # Step 3: Return
    if indices:
        return arr, indices
    else:
        return arr, [-1]


# Input
arr = [2, 1, 3, 4, 5, 6]
target = 2

# Call the function
sorted_arr, indices = bubble_sort(arr, target)

# Output
print("Sorted Array:", sorted_arr)

if indices != [-1]:
    print("Target found at index(es):", indices)
else:
    print("Not found")

def bubble_sort(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] =arr[j+1],arr[j]
    indices =[]
    for i in range (len(arr)):
        if arr[i] == target:
            indices.append(i)
    if indices:
        return arr,indices
    else:
        return arr,[-1]
arr=[2,3,4,1,2,3,4]
target =2
sorted_arr,indices=bubble_sort(arr,target)
print(sorted_arr)
if indices !=[-1]:
    print('index at ',indices)
else:
    print('not found')

#leet code
def two_sum(nums,target):

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
         if nums[i]+nums[j] ==target:
            return [i,j]
nums=[2,7,11,15]
target=9

result=two_sum(nums,target)
print(result)
from PIL.Image import radial_gradient

from nishat import total

arr=[2,3,4,4,4,42,2,]
feq={}
for num in arr:
    if num in feq:
        feq[num] +=1
    else:
        feq[num]=1
for key in feq:
    print(f"{key} {feq[key]} times")

arr =[3,3,2,1,1,1,2,2,2,3,3,]
freq={}
for num in arr:
    if num in freq:
        freq[num] +=1
    else:
        freq[num]=1

for key in freq:
    print(f"{key} {freq[num]} times")

def check_sorted(arr):
    is_ascending=True
    is_dscending=True
    total_count=0
    for i in range(len(arr)-1):
        total_count+=1
        print(f"comparing {arr[i]},{arr[i+1]}")

        if arr[i]< arr[i+1]:
            is_ascending=False
        elif arr[i] > arr[i+1]:
            is_dscending = False
    print('comapring,',total_count)

    if is_ascending:
        return "ascending"
    elif is_dscending:
        return ("dscending")
    else:
        "unsorted"

def sorted(arr):
    is_ascending =True
    is_dscending=True
    total_count =0
    for i in range(len(arr)-1):
        total_count +=1
        print(f"comparing,{arr[i]}  {arr[i+1]}")

        if arr[i]  > arr[i+1]:
            is_ascending = False
        elif arr[i] < arr[i+1]:
            is_dscending =False
    print("total_Count",total_count)

    if is_ascending:
        return "ascending"
    elif is_dscending:
        return "dscending"
    else:
         return "unsorted"
print(sorted([12,34,5,67]))


def sorted_check(arr):
    is_ascending =True
    is_dscending=True
    total_count= 0
    for i in range(len(arr)-1):
        total_count+=1
        print(f"comaparing,{arr[i]} {arr[i+1]}")

    if arr[i] > arr[i+1]:
        is_ascending=False
    elif arr[i] < arr[i+1]:
        is_dscending =True
    print('total count',total_count)

    if is_ascending:
        return "ascending"
    elif is_dscending:
        return "dscending"
    else:
        return "unsorted"
print(sorted_check([4,3,2,1,2,3,4,56,7]))






