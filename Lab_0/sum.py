# Addera alla siffror i en fil
def filesum(numbers):
  file=open(numbers,'r')
  ans=0
  for line in file:
    ans+=int(line.strip())
  return ans