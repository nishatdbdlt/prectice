from typing import reveal_type

from nishat import found

print('nihaat')
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_cout=0
odd_coutn=0
for num in arr:
    if num % 2==0:
        even_cout+=1
    else:
        odd_coutn+=1
print(even_cout)
print(odd_coutn)


arr =[3,4,5,6,7,8]
target=2
found=False
for num in arr:
    if num ==target:
        found=True
        break
if found:
    print('found')
else:
    print('not found')
arr = [1, 2, 2, 3, 4, 4, 4, 5]
target =4
count=0
for num in arr:
    if num== target:
        count+=1
print(count)

def linner_search(arr,target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
    return -1
arr=[2,3,4,5,6,7]
target=0
result=linner_search(arr,target)
print('found at'if result !=-1 else "not found",result)


def linner_search(arr,target):
   for i in range(len(arr)):
      if arr[i] == target:
        return i
   return -1
arr=['nishat','karim','rahim']
target = 'rahim'
nishat=linner_search(arr,target)
print('found at indext'if nishat!=-1 else'not found',nishat)


def linner_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr=[12,33,44,55,66]
target=int(input('enter the number'))
result=linner_search(arr,target)
if result !=-1:
    print('found at index',result)
else:
    print("not found")

def buuble_sort(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(0 ,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[2,3,4,5,6,7,1]
target =1
result =buuble_sort(arr,target)
print(result)

def bubble_sort(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[3,2,1,2,3,4,5,6]
nishat=bubble_sort(arr,target)
print('sorted arr',nishat)


def bubble_sort(arr,target):
    n =len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[2,3,4,5,1,3,46]
result=buuble_sort(arr,target)
if result!=-1:
    print('found at index',result)
else:
    print("not found")