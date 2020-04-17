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

if __name__== "__main__":
  m()
