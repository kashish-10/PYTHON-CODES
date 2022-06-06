def duplicate_detection(arr):
    m = len(arr)
    arr.sort()
    ans = 0
    for i in range(m-1):
        if arr[i] == arr[i+1]:
            ans = arr[i]
        else:
            continue
    return ans


a = [23]
for j in range(1,100):
    a.append(j)

print(duplicate_detection(a))
