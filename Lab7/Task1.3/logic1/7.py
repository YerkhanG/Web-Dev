def squirrel_play(temp, is_summer):
  if not is_summer:
    return (temp >= 60 and temp <= 90)
  else:
    return (temp >= 60 and temp <= 100)