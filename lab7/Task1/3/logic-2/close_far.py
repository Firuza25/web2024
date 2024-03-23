def close_far(a, b, c):
    def is_close(x, y):
        return abs(x - y) <= 1
    
    if is_close(a, b) and not is_close(a, c) and not is_close(b, c):
        return True

    elif is_close(a, c) and not is_close(a, b) and not is_close(b, c):
        return True
    else:
        return False

