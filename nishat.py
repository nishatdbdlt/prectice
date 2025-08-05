# name = input("enter your name")
# print("hello",name,"welcome")
#
#
# age = input("enter you are")
# print('hello',age,'year old')
#
#
#
# name = 'nishat'
# age= 23
# city ="dhaka"
# print(name,age,city)
#
#
# x ,y =input("enter two value").split()
#
# print("number of boys",x)
# print("number of girls",y)
#
# x ,y ,z =input("enter you number").split()
# print("enter number",x)
# print("enter number",y)
# print("enter number ",z)
#
#
# a = "hello world"
# b = 10
# c= 11.12
# d=('nishat','nuri','rafi')
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
#
# amount= 12.346
# print('amount:${:.8f}'.format(amount))
#
# print("python",end='@')
# print('nishat')
#
# #seprating with comma
# print('a','b','c',sep='')
# # format date
# print('02','04','1997',sep='-')
# print('nishat','hasibul',sep='@')
#
# name ="nishat"
# age = 23
# print(f"hello,my name is {name} i am {age} years old")
#
#
# num = int(input("inter value:"))
# add = (num + 4)
#
# def combine_strings(a, b):
#     """
#     Combines two strings where the shorter string wraps around the longer one.
#     Format: shorter + longer + shorter
#
#     Args:
#         a (str): First string
#         b (str): Second string
#
#     Returns:
#         str: Combined string in shorter+longer+shorter format
#     """
#
#
#
# # # Test with the given example
# # # array
# #
# # arr =[0] * 6
#
#
# arr =[[1,2,4],[2,3,4],[3,4,5]]
# print('first elemant of frist row',arr[0][0])
# print('third element of third row',arr[1][2])
# print('secound element of tird row',arr[2][1])
#
#
# arr=[
#      [1, 2, 4],
#      [3, 4, 5],
#      [5, 6, 7, 23]
#
#  ]
# for row in arr:
#      for x in row:
#         print(x,end=' ')
#      print()
# arr = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# # Traversing each row
# for row in arr:
#
#     # Traversing each element
#     # in the current row
#     for x in row:
#         print(x, end=" ")
#     print()
#
# arr =[
#     [1,2,4,5],
#     [7,6,5,4,3],
#     [8,7,6]
# ]
# for row in arr:
#     for x in row:
#         print(x,end=" ")
#     print()
#
#
# num=['nishat','nuri','rafi']
# print(num[1])
# print(num[-1])
# num.append('nus')
# print(num)
# num.remove('nuri')
# print(num)
# for num in num:
#     print(num)
#
# nishat=[1,2,3,4,5]
# nishat.append(4)
# nishat.remove(4)
# nishat.pop()
# for i nishat in nishat:
#   print(nishat)
#
# marks=[78,78,65,43,32]
# copy_marks=marks.copy()
# copy_marks.append(78)
# print('orginal',marks)
# print(copy_marks)
# #linear search
#
#
# def linner_search(arr,target):
#     for i in  range (len(arr)):
#         if arr[i] == target:
#             return i
#         return 1
# numbers=[45,56,78,90]
# target= 56
# result=linner_search(numbers,target)
# print(result)
#
# def linner_search(arr,target):
#     for i in range (len(arr)):
#         if arr[i] == target:
#             return i
#
#     return -1
# num=[3,4,5,6,7,8]
#
# target=4
# nishat=linner_search(num,target)
# print(nishat)
from codecs import make_identity_dict
from operator import truediv
from zoneinfo import reset_tzpath

# numbers = [1,2,4,5,6]
# print("length = ",len(numbers))
# print('frist item',numbers[0])
# print('lest item',numbers[4])
# print('all item')
# for num in numbers:
#     print(num)
#

# arr =[2,3,5,6,78]
# for num in arr:
#     print(num,end=" ")
#
# numbers =[1,2,4,5,6]
# total= 0
# for num in numbers:
#     total+=num
# print('sum=',total)
#

nishat=[3,4,5,6,7,8]
total =0
for num in nishat:
    total+=num
print('sum =',total)


nishat =[3,4,5,6,7]
total =0
for num in nishat:
    total+=num
print('total =',total)

arr = [2,3,4,5,6,7]
maximun=arr[0]
for num in arr:
    if num > maximun:
        maximun = num
print(maximun)

nishat= [2,3,4,5,6,7,9]
maximun = nishat[0]
for num in nishat:
    if num > maximun:
        maximun = num

print(maximun)

nuri=[3,4,5,6,7]
minimum= nuri[0]
for num in nuri:
    if num < minimum:
        minimum=num
print(minimum)


nishat=[3,4,5,6,7,8]
minimum = nishat[0]
for num in nishat:
    if minimum > num:
        minimum=num
print(minimum)


arr =[3,4,5,6,7,8]
even_coutn=0
for num in arr:
    if num % 2 == 0:
        even_coutn +=1

print('even_count',even_coutn)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_coutn= 0
odd_coutn=0
for num in arr:
    if num % 2 ==0:
        even_coutn+=1
    else:
        odd_coutn+=1
print(even_coutn)
print(odd_coutn)

# arr=[34,45,67,78]
# target =45
# found= False
# for num in arr:
#     if num == target:
#         found=True
#         break
# if found:
#     print("found")
# else:
#     print("not found")
arr = [10, 20, 30, 40, 50, 60]
target = 40
found = False
for num in arr:
    if num == target:
     found = True
     break
if found:
    print("found")
else:
    print("not found")

arr = [22,44,55,66,77]
arr.append(34)
arr.insert(2,56)

arr.remove(22)
del arr[3]
print(arr)

arr = [10, 20, 30]
arr.append(100)
arr.insert(1,50)
del arr[0]
print(arr)


arr = [1, 2, 2, 3, 4, 4, 4, 5]
target = 4
count =0
for num in arr:
    if num == target:
     count+=1
print(f"{target} appears {count} time")


arr = [7, 8, 7, 5, 6, 7, 5, 8]
target = 8
count =0
for num in arr:
    if num == target:
        count+=1
print(f"{target}appears{count} time")


arr =[22,3,4,5,66,7,7,7,7]
target =7
count =0
for num in arr:
    if num == target:
        count+=1
print(f"{target} appears{count} time")


arr =[33,3,3,33,44]
minimum=arr[0]
for num in arr:
    if num < minimum:
        minimum=num
print(minimum)

arr =[33,3,3,33,44]
maximun= arr[0]
for num in arr:
    if num > maximun:
        maximun=num
print(maximun)

# def binnay_search(arr,target):
#     low= 0
#     high=len(arr)
#     while low < high:
#         mid=low + high /2
#         return mid
#     if low < mid :
#         return low
#     elif high > mid:
#         return high
#     else:
#         return i
# arr=[1,3,4,5,]
# target =1
# nis=binnay_search(arr,target)
# print(nis)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_coutn=0
odd_coutn =0
for num in arr:
    if num % 2==0:
        even_coutn+=1
    else:
        odd_coutn+=1
print(even_coutn)
print(odd_coutn)




















