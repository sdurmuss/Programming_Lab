from decimal import Decimal

def bozukluk(para,tutar):
    kalan=("%.2f" % (para-tutar))
    bozuk=[0.50,0.25,0.21,0.10,0.05,0.01]
    kalanbozuk={}
    paraustu=[0,0,0,0,0,0]
    if(float("%.2f" % (float(kalan)%float(0.21)))==0.00):
        paraustu[2]=int("%.0f" % (float(kalan)/float(0.21)))
        kalan=0
    for i in range(len(bozuk)):
        while(float(kalan)-bozuk[i]>=0):
            kalan=Decimal(kalan)-Decimal(bozuk[i])
            paraustu[i]+=1
            
    for j in range(len(bozuk)):
        kalanbozuk[bozuk[j]]=paraustu[j]
    return(kalanbozuk)

print(bozukluk(10.00,9.37))

#dynamic çözüm
def dynamicbozuk(bozuklukList,paraüstü,minKurus,kullanýlanKurus):
   for kurus in range(paraüstü+1):
      kurusSayýsý = kurus
      yeniKurus = 1
      for j in [c for c in bozuklukList if c <= kurus]:
            if minKurus[kurus-j] + 1 < kurusSayýsý:
               kurusSayýsý = minKurus[kurus-j]+1
               yeniKurus = j
      minKurus[kurus] = kurusSayýsý
      kullanýlanKurus[kurus] = yeniKurus
   return minKurus[paraüstü]

def printKuruslarý(kullanýlanKurus,paraüstü):
   coin = paraüstü
   while coin > 0:
      thisCoin = kullanýlanKurus[coin]
      print(thisCoin)
      coin = coin - thisCoin

deger = 21
clist = [1,5,10,21,25]
kullanýlanKurus = [0]*(deger+1)
kurusSayýsý = [0]*(deger+1)

print("Making paraüstü for",deger,"requires")
print(dynamicbozuk(clist,deger,kurusSayýsý,kullanýlanKurus),"coins")
print("They are:")
printKuruslarý(kullanýlanKurus,deger)
print("The used list is as follows:")
print(kullanýlanKurus)