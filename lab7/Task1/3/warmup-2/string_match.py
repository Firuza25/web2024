def string_match(a, b):
  min_text = min(len(a), len(b))
  count=0
  for i in range(min_text-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count += 1
  return count