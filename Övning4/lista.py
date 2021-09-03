#Kolla ifall första ordet och sista ordet i listan är samma
#IFall lista är tom så ska funktionen returna False
def same_ends(words):
  if words == []:
    return False
  elif words[0] == words[-1]:
    return True
  else:
    return False 