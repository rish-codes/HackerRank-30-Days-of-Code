arr = []
maximum = -99999
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
for i in range(6):
    for j in range(6):
        if i+2<6 and j+2<6:
            result = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if result > maximum:
                maximum = result
print(maximum)
