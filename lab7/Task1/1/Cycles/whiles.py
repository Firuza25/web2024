# a
def listSquares():
    n = int(input())
    i = 1 
    while (i*i <= n ):
        print(i*i)
        i+=1

listSquares()




# b
def div():
    n = int(input())
    div = 2
    while n % div != 0:
        div += 1
    print(div)
div()


# c
def powsTwo():
    n = int(input())
    powka = 0
    while 2**powka <=n:
        print(2**powka)
        powka += 1
powsTwo()




# d
def dvoika():
    n = int(input())
    while n%2 ==0:
        n /= 2
        if(n==1):
            print("YES")
        else:
            print("NO")
dvoika()


# e

def log():
    n = int(input())
    powka = 0
    cur = 1
    while cur < n:
        cur *= 2
        powka += 1
    print(powka)
log()