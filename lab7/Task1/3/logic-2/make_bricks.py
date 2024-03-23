def make_bricks(small, big, goal):
    max_big_cover = big * 5

    remaining = goal - min(max_big_cover, goal // 5 * 5)
    return remaining <= small
