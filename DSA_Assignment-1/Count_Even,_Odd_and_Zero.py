
arr=[10, 5, 0, 7, 8, 0, 13, 4]

def count(arr):
    odd,even,zero=0,0,0
    for i in arr:
        if i==0:
            zero+=1
        elif i%2==0:
            even+=1
        else:
            odd+=1
    print(f"The even count: {even}")
    print(f"The odd count: {odd}")
    print(f"The zero count: {zero}")
count(arr)