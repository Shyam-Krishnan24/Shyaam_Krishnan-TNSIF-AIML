
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current = arr[0]
maximum = arr[0]

for i in range(1, len(arr)):
    current = max(arr[i], current + arr[i])
    maximum = max(maximum, current)

print(maximum)
