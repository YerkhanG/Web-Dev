def make_bricks(small, big, goal):
  big = big * 5
  if small == goal:
    return True
  elif big == goal:
    return True
  elif small + big == goal:
    return True
  else:
    return False
