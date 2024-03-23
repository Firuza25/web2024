# a

def min(a,b,c,d):
    if a <= b and a <= c and a <= d:
        return a
    elif b <= a and b <= c and b <= d:
        return b
    elif c <= a and c <= b and c <= d:
        return c
    else:
        return d

a,b,c,d =  map(int, input().split())
print(min(a,b,c,d))


# b
def double_power(a,n):
    return a**n

a,n =  map(int, input().split())
print(double_power(a,n))



# c
def xor(a, b):
    return a ^ b
a, b = map(int, input().split())
print(int(xor(a, b)))