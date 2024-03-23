# a

def even_num():
    x = int(input())
    y = int(input())
    for i in  range(x, y+1):
        if i%2==0:
            print(i, end=" ")
even_num()
# for int=0; i<n i++



# b
def remains(): 
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    for i in range(a,b+1):
        if i % d == c:
            print(i, end=" ")

remains()


# c
import math
def squares():
    a = int(input())
    b = int(input())
    for i in range(a,b+1):
        j = int(math.sqrt(i))
        if j * j == i:
            print(i)


squares()


# d?????
# def digit ():
#     x = int(input())
#     d = int(input())
#     count = 0
#     for digit in str(x):  
#         if int(digit) == d:
#             count += 1
#     print(count)

# digit()


# e
# def sums(x):
#     sum = 0
#     for i in str(x):
#         sum += int(i)
#     print(sum)

# x = int(input())
# sums(x)
        




# g
import math
def min_divisor():
    a = int(input())
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i ==0:
           return i
        return a

small_div = min_divisor()
print(small_div)

#  h
def dividers():
    a = int(input())
    for i in range(1, a+1):
        if a % i == 0 :
            print(i)
dividers()



# i
def dividers():
    count=0
    a = int(input())
    for i in range(1, a+1):
        if a % i == 0 :
            count += 1
    print(count)
           
dividers()



# j
def sumOfHun():
    count = 0
    for x in range(1, 101):
        a = int(input())
        count += a
    print(count)


# k
def sums2():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        a = int(input())
        sum+=a
    print(sum)
sums2()
        

# l
def binary(bin):
    d=0
    pow=1
    for i in reversed(bin):
        d += int(i)*pow
        pow *= 2
    return d
bin = str(input())
answer = binary(bin)
print(answer)



#  m
def zero():
    n = int(input())
    count = 0 
    for i in range(1, n+1):
        a = int(input())
        if(a == 0):
            count += 1
    print(count)

zero()