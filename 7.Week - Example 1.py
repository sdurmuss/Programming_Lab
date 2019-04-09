import random
import pylab
import numpy

# def ZarAt():
#     """Return a random int between 1-6"""
#     return random.choice([1,2,3,4,5,6])

# def Tane(n):
#     result=''
#     for i in range(n):
#         result= result+str(ZarAt())+" "
#     print(result)

# Tane(10)

# def at(atmaSayýsý):
#     heads=0
#     for i in range(atmaSayýsý):
#         if random.choice(('H','T')) == 'H':
#             heads+=1
#     return heads/atmaSayýsý
# def atSim(numFlipsPerTrial, denemeSayýsý):
#     fracHeads=[]
#     for i in range(denemeSayýsý):
#         fracHeads.append(at(numFlipsPerTrial))
#         mean=sum(fracHeads)/len(fracHeads)
#     return mean

# print(atSim(10,10000))
def yazýtura(enaz,encok):
    deneme=[]
    ybölüt=[]
    yeksit=[]
    for i in range(enaz,encok+1):
        deneme.append(2**i)
    for dene in deneme:
        ysayýsý=0
        tsayýsý=0
        for n in range(dene):
            if(random.choice(('Y','T'))=='Y'):
                ysayýsý+=1
            else:
                tsayýsý+=1
        ybölüt.append(ysayýsý/tsayýsý)
        yeksit.append(abs(ysayýsý-tsayýsý))
    pylab.title('Yazý-Tura Farký')
    pylab.xlabel('Deneme Sayýsý')
    pylab.plot(deneme,yeksit)
    pylab.figure()
    pylab.title('Yazý/Tura Oraný')
    pylab.xlabel('Deneme Sayýsý')
    pylab.plot(deneme,ybölüt)