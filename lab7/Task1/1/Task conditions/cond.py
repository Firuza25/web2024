
# a
def maxi():
    n = int(input())
    m = int(input())
    # print(max(n,m))
    if(n>=m):
        print(n)
    else:
        print(m)

maxi()


# b
def leap_year():
    l = int(input())

    if(l % 4 ==0 & l % 100 !=0):
        print("YES")
    elif(l % 400 == 0):
        print("YES")
    else: 
        print("NO")
leap_year()


# c
def testing_system(a,b):
    if a == b:
        return True
    elif a != 1 and b != 1:
        return True
    else:
        return False
    
a = int(input())
b = int(input())
if testing_system(a,b):
    print("YES")
else:
    print("NO")
    
# d
def sin(x):
    if(x>0):
        print(1)
    elif(x<0):
        print(-1)
    else: 
        print(0)

x= int(input())
sin(x)


# e
def comp(x,y):
    if(x>y):
        print(1)
    elif(x<y):
        print(2)
    else:
        print(0)

x = int(input())
y = int(input())
comp(x,y)