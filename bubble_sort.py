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


def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return True
    return False
print(is_sorted([3,4,5,1]))


def sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
print(sorted([2, 4, 6, 8]))
print(sorted([9, 7, 5, 3]))
print(sorted([4,3,4,2,1,4]))

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            return False

    return True
print(is_sorted([9,7,5,3]))








def check_sort_order(arr):
    is_ace=True
    is_dce=True
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            is_ace=False
        if arr[i] > arr[i+1]:
            is_dce=False
    if is_ace:
        return "ascending"
    elif is_dce:
        return "descending"
    else:
        return "unsoted"
print(check_sort_order([1, 2, 3]))
print(check_sort_order([5, 3, 1]))
print(check_sort_order([3, 2, 4]))
#loop count

def check_sort_order_verbose(arr):
    is_ace=True
    is_dec=True
    loop_count=0
    for i in range(len(arr)-1):
        loop_count+=1
        print('comparing{arr[i]} and {arr[i+1]}')
        if arr[i] < arr[i+1]:
             is_ace = False
        if arr[i] > arr[i+1]:
             is_dec= False

    print("total comparing",loop_count)

    if is_ace:
         return "ascending"
    elif is_dec:
         return "decending"
    else:
        return "unsorted"
print(check_sort_order_verbose([1, 2, 3]))
print("-----")
print(check_sort_order_verbose([9, 7, 4]))
print("-----")
print(check_sort_order_verbose([3, 2, 5]))

def check_sorted_order(arr):
    is_acending=True
    is_decending=True
    cout_total= 0
    for i in range(len(arr)-1):
        cout_total+=1
        print("comparig {arr[1]},and {arr[i+1]}")
        if arr[i] < arr[i+1]:
            is_acending= False
        if arr[i] > arr[i+1]:
            is_decending=False
    print('comparing',cout_total)

    if is_acending:
        return "ascending"
    elif is_decending:
        return "desceding"
    else:
        "unsorted"

print(check_sort_order([1, 2, 3]))
print("-----")
print(check_sort_order([9, 7, 4]))
print("-----")
print(check_sort_order([3, 2, 5]))


def check_sorted(arr):
    is_ascending=True
    is_descending=True
    total_count=0
    for i in range(len(arr)-1):
        total_count+=1
        print(f"Comparing: {arr[i]} and {arr[i + 1]}")
        if arr[i] < arr[i+1]:
            is_accending=  False
        if arr[i] > arr[i+1]:
            is_desending = False
    print('conpare',total_count)

    if is_ascending:
        return  "ascending"
    elif is_descending:
        return " descending"
    else:
         return "unsorted"

print(check_sorted([10,20,30,40,50]))


# arr=[3,4,5,6,7,2,2,4,5]
# freq={}
# for num in arr:
#     if num in freq:
#         freq[num] +=1
#     else:
#         freq[num] =1
# for key in freq:
#     print(f"{key} {freq[key]} times")

arr=[3,3,3,1,1,2,2,44,5]
freq ={}
for num in arr:
    if num in freq:
        freq[num] +=1
    else:
        freq[num] =1
for key in freq:
    print(f"{key} {freq[key]} times")


arr = [3, 3, 3, 1, 1, 2, 2, 44, 5]
freq = {}

for num in arr:  # ✅ এখানে arr এর ওপর লুপ
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# রেজাল্ট দেখাও
for key in freq:
    print(f"{key} → {freq[key]} times")
