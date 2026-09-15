arr1= [1, 2, 2, 3, 4]
arr2= [4, 2, 1, 2, 3]

def compare(arr1,arr2):
    if sorted(arr1)==sorted(arr2):
        print("Arrays are Equal")
    else:
        print("Arrays are not Equal")

compare(arr1,arr2)

# Method -2

if len(arr1)!= len(arr2):
    print("Arrays are not Equal")

else:
    equal=True

    for i in range(len(arr1)):
        count1=0
        count2=0

        for j in range(len(arr1)):
            if arr1[i]==arr1[j]:
                count1+=1
        for j in range(len(arr2)):
            if arr1[i]==arr2[j]:
                count2+=1

        if count1!=count2:
            equal=False
            break
    if equal:
        print("Arrays are Equal")
    else:
        print("Arrays are not Equal")