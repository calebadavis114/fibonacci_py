def fibonacci(n):
  f = 2 
  fac = [0, 1]
  if(n == 0):
    return 0
  elif(n == 1):
    return 1
  else:
    for x in range(n - 2):
      fac.append(f)
      f = fac[-1] + fac[-1 - 1]
  return fac[-1]
