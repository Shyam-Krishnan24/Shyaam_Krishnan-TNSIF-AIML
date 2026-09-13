
arr=[1, 2, 3, 5, 6, 7]

def large_small(arr):
    large=arr[0]
    small=arr[0]

    for i in arr:
        if i>large:
            large=i
        if i<small:
            small=i

    for i in range(small,large+1):
        if i not in arr:
            print(f"Missing Number: {i}")
large_small(arr)

def method_2(arr):
    for i in range(arr[0],arr[-1]+1):
        print()
        if i not in arr:
            print(f"Missing Number: {i}")
method_2(arr)