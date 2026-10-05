
arr = [2, 7, 11, 15]
target = 9
seen = {}

for i in range(len(arr)):
    need = target - arr[i]
    if need in seen:
        print([seen[need], i])
        break
    seen[arr[i]] = i
