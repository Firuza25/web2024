n = int(input())
arr = list(map(int, input().split()))

def sign():
    for i in arr:
        if arr[i - 1] >0  and arr[i]>0 or arr[i - 1] <0  and arr[i]<0:
            return True

if(sign()):
    print("YES")
else:
    print("NO")