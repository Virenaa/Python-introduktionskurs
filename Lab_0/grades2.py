def grades(grade):
  
  if grade>= 90 and grade<=100:
    return "A"
  elif grade>=80 and grade<=89:
    return "B"
  elif grade>= 70 and grade<=79:
    return "C" 
  elif grade>=60 and grade<=69:
    return "D"
  else:
    return "F"