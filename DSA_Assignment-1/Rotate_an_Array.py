
arr= [1, 2, 3, 4, 5]
k=2

def rotate(arr):
    print(arr[-k:]+arr[:-k])
    
rotate(arr)

