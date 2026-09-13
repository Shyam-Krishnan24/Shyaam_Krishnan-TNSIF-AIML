
arr=[10, 20, 30, 40, 50]

def reverse(arr):
    i=len(arr)-1
    for j in range(len(arr)//2):
        arr[i],arr[j]=arr[j],arr[i]
        i-=1
    print(arr)
    
reverse(arr)
