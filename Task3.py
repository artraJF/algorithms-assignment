def prime(n):
    arr = list(range(2, n + 1))
    for x in range(int(n**0.5)):
        for i in arr:
            if arr[x] == i:
                None
            elif (i % arr[x]) == 0:
                arr.remove(i)
    return arr

print(prime(100))