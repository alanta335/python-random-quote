import random
def m():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last=22
  rnd2=random.randint(1,5)
  for x in range(rnd2):
    rnd1=random.randint(0,last)
    print(quotes[rnd1])

if __name__== "__main__":
  m()
