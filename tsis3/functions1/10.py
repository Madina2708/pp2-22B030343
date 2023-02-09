def uniquel(n):
  m = []
  for a in n:
    if a not in m:
      m.append(a)
  return m

print(uniquel([2,3,6,6,6,7,8,6]))