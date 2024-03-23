def no_teen_sum(a, b, c):
    def fix_teen(n):
        if 13 <= n <= 19 and n != 15 and n != 16:
            return 0
        return n

    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    
    return a + b + c