def going_out2(sunny,stay_in):
  if sunny:
    res = True
    if stay_in:
      res=False
    else:
      res=True
  else:
    res=False
  
  
  return res

def going_out(sunny,stay_in):
  return sunny and not(stay_in)
