def make_chocolate(small, big, goal):
    max_big= big * 5
    remaining = goal - min(max_big, goal // 5 * 5)
    
    
    if remaining <= small:
        return remaining
    else:
        return -1

