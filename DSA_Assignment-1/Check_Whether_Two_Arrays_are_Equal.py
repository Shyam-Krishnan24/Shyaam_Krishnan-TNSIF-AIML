arr1= [1, 2, 2, 3, 4]
arr2= [4, 2, 1, 2, 3]

def compare(arr1,arr2):
    if sorted(arr1)==sorted(arr2):
        print("Arrays are Equal")
    else:
        print("Arrays are not Equal")

compare(arr1,arr2)