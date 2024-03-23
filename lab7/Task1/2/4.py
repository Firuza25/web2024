def swap_case(s):
    ans = ''
    for i in s:
        ans += i.upper() if i.islower() else i.lower()
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)