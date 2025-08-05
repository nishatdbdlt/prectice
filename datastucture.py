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
