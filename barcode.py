# from operator import index
#
# import qrcode
# data = "https://github.com/nishatdbdlt"
# qr=qrcode.QRCode(
#     version=1,
#     box_size=10,
#     border=4,
#
# )
# qr.add_data(data)
# qr.make(fit=True)
# img = qr.make_image(fill_color="black", back_color="white")
# img.save("my_qrcode.png")
#
# print("QR Code saved as: my_qrcode.png")
#
# def bubble_sort(arr, target):
#     n = len(arr)
#
#     # Step 1: Bubble Sort
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#     # Step 2: Find all indices of the target
#     indexes = []
#     for i in range(len(arr)):
#         if arr[i] == target:
#             indexes.append(i)
#
#     # Step 3: Return
#     if indexes:
#         return arr, indexes
#     else:
#         return arr, [-1]
# arr = [3, 3, 4, 2, 4]
# target = 4
#
# sorted_arr, indices = bubble_sort(arr, target)
#
# print("Sorted Array:", sorted_arr)
# if indices != [-1]:
#     print("Target found at index(es):", indices)
# else:
#     print("Target not found.")
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
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    indices =[]
    for i in  range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    if indices:
        return arr,indices
    else:
        return arr[-1]
arr=[4,4,3,1,5,6]
target=1
sorted_arr,indices=bubble_sort(arr,target)
print(sorted_arr)
if indices !=-1:
    print('found at index',indices)
else:
    print("not found")
