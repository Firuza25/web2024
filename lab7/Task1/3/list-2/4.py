def sum67(nums):
    total = 0
    check = False
    for i in range(len(nums)):
        if nums[i] == 6:
            check = True
        if not check:
            total += nums[i]
        if nums[i] == 7 and check:
            check = False
            
    return total