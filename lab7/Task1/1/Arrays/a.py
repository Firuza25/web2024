a = int(input())
arr = list(map(int, input().split()))

for i in range(a):
    if i%2 == 0:
        print(arr[i], end=" ")