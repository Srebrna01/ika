#Zadanie 4.1 Matura 2022

f = open("matura2022/liczby.txt", "r")

anwser = []


for x in f:
    x = str(x).rstrip()
    x = str(x).lstrip()
    if str(x)[0] == str(x)[-1]:
      anwser.append(x)    
      continue
    else :
      print (" ")

length = len(anwser)

length = str(length)
    
anwser = anwser[0]

print ("The final anwser is ", length , "and " , anwser)

test