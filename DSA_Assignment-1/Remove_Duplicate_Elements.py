arr=[10, 20, 10, 30, 20, 40, 30]

#Method -1
def method_1(arr):
    print(list(set(arr)))
method_1(arr)

#Method-2
def method_2(arr):
    seen=set()
    s_arr=[]

    for i in arr:
        if i not in seen:
            seen.add(i)
            s_arr.append(i)
    print(s_arr)
method_2(arr)