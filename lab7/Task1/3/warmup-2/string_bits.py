def string_bits(str):
  total = ""
  for i in range(len(str)):
    if i % 2 == 0:
      total += str[i]
  return total
  