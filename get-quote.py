import random
def m():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last=22
  rnd2=random.randint(1,5)
  for x in range(rnd2):
    rnd1=random.randint(0,last)
    q = quotes[rnd1].rstrip('\n')
    print(q)
  print("do you what to add a quote then enter y less enter n ")
  d = input()
  if d=='y':
    f = open("quotes.txt",'a')
    print("enter your quote")
    addq = str(input())
    f.write(addq+'\n')
    last+=1
    f.close()
  elif d=='n':
    print("thank you")
  else:
    print("wrong input")

if __name__== "__main__":
  m()
