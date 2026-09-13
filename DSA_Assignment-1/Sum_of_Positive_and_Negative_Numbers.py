arr=[10, -5, 20, -8, 15, -2]

def positive_negative(arr):
    p_sum,n_sum=0,0

    for i in arr:
        if i<0:
            n_sum+=i
        elif i>0:
            p_sum+=i
    print(f"The positive sum is {p_sum}")
    print(f"The negative sum is {n_sum}")
    
positive_negative(arr)