def word_index(string):
  words = string.split() # ['the','spider','indexes','the','spider','web']
  
  myDict = {}
  
  for index, word in enumerate(words): #[ (0,"the"), (1,"spider")....]
    if word in myDict.keys():
      myDict[word].append(index)
    else:
      myDict[word] = [index]
  
  return myDict

