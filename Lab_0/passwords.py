# Får en fil med användarnamn och lösenord. 
# Vill lägga in alla värden i en dictonary


def passwords(filename):
  pairs = {}
  file = open(filename)
 
  for users in file:
    key,value = users.split()
    pairs[key] = value
  return pairs