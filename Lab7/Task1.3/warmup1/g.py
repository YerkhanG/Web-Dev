def pos_neg(a, b, negative):
  if ((a < 0 and b > 0) or (a >0 and b < 0)) and negative == False:
    return True
  elif negative == True:
    if a < 0 and b < 0:
      return True
    else:
      return False
  else:
    return False
