def fix_teen(n):
  if n >= 13 and n<=19 and not (n==15 or n == 16):
    return 0
  else:
    return n
  

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c) 
  
  