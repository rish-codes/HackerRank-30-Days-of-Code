import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numSwaps = 0

for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numSwaps += 1
        
print(f'Array is sorted in {numSwaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')
