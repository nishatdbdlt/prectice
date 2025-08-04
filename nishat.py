name = input("enter your name")
print("hello",name,"welcome")


age = input("enter you are")
print('hello',age,'year old')



name = 'nishat'
age= 23
city ="dhaka"
print(name,age,city)


x ,y =input("enter two value").split()

print("number of boys",x)
print("number of girls",y)

x ,y ,z =input("enter you number").split()
print("enter number",x)
print("enter number",y)
print("enter number ",z)


a = "hello world"
b = 10
c= 11.12
d=('nishat','nuri','rafi')

print(type(a))
print(type(b))
print(type(c))
print(type(d))

amount= 12.346
print('amount:${:.8f}'.format(amount))

print("python",end='@')
print('nishat')

#seprating with comma
print('a','b','c',sep='')
# format date
print('02','04','1997',sep='-')
print('nishat','hasibul',sep='@')

name ="nishat"
age = 23
print(f"hello,my name is {name} i am {age} years old")


num = int(input("inter value:"))
add = (num + 4)

def combine_strings(a, b):
    """
    Combines two strings where the shorter string wraps around the longer one.
    Format: shorter + longer + shorter

    Args:
        a (str): First string
        b (str): Second string

    Returns:
        str: Combined string in shorter+longer+shorter format
    """



# # Test with the given example
# # array
#
# arr =[0] * 6


arr =[[1,2,4],[2,3,4],[3,4,5]]
print('first elemant of frist row',arr[0][0])
print('third element of third row',arr[1][2])
print('secound element of tird row',arr[2][1])


arr=[
     [1, 2, 4],
     [3, 4, 5],
     [5, 6, 7, 23]

 ]
for row in arr:
     for x in row:
        print(x,end=' ')
     print()
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Traversing each row
for row in arr:

    # Traversing each element
    # in the current row
    for x in row:
        print(x, end=" ")
    print()

arr =[
    [1,2,4,5],
    [7,6,5,4,3],
    [8,7,6]
]
for row in arr:
    for x in row:
        print(x,end=" ")
    print()


num=['nishat','nuri','rafi']
print(num[1])
print(num[-1])
num.append('nus')
print(num)
num.remove('nuri')
print(num)
for num in num:
    print(num)

nishat=[1,2,3,4,5]
nishat.append(4)
nishat.remove(4)
nishat.pop()
for ni nshat in nishat:
  print(nishat)

marks=[78,78,65,43,32]
copy_marks=marks.copy()
copy_marks.append(78)
print('orginal',marks)
print(copy_marks)
#linear search


def linner_search(arr,target):
    for i in  range (len(arr)):
        if arr[i] == target:
            return i
        return 1
numbers=[45,56,78,90]
target= 56
result=linner_search(numbers,target)
print(result)

def linner_search(arr,target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i

    return -1
num=[3,4,5,6,7,8]

target=4
nishat=linner_search(num,target)
print(nishat)