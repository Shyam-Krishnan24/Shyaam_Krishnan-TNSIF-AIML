
arr=[2, 5, 2, 8, 5, 2, 3, 5, 2]

def mose_freq(arr):
    print()
    seen={}

    for i in arr:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1

    ele=max(seen,key=seen.get)
    print(f"The most freq element {ele}")
    print(f"The frequencey {seen[ele]}")
mose_freq(arr)