# a
def hypo(a,b):
    return (a**2 + b**2 ) ** 0.5

a = int(input())
b = int(input())
   
print(hypo(a,b))



# b
def pref_next(num):
    print("The next number for the number",num, "is", num+1)
    print("The previous number for the number", num, "is", num-1)
num = int(input())
pref_next(num)




# c
def apple(n,m):
    return m/n
n = int(input())
m = int(input())
print(int(apple(n,m)))


# d
def apple(n,m):
    return m/n
n = int(input())
m = int(input())
print(m-(n*int(apple(n,m))))
# or
print(m%n)







# e

def mkad():
    v = int(input())
    t = int(input())

    print((v*t)%109)
mkad()