def problemator(s):
  s = str(s).strip()
  if s[0] == s [-1]:
      return True 
  else :
      return False 
  
f = open("matura2022/liczby.txt", "r")

anwser = []

for x in f:
    if problemator(x):
      anwser.append(x)    
      continue

print ("The final anwser is ", str(len(anwser)) , "and " , anwser[0])
