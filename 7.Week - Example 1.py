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

# def at(atmaSay�s�):
#     heads=0
#     for i in range(atmaSay�s�):
#         if random.choice(('H','T')) == 'H':
#             heads+=1
#     return heads/atmaSay�s�
# def atSim(numFlipsPerTrial, denemeSay�s�):
#     fracHeads=[]
#     for i in range(denemeSay�s�):
#         fracHeads.append(at(numFlipsPerTrial))
#         mean=sum(fracHeads)/len(fracHeads)
#     return mean

# print(atSim(10,10000))
def yaz�tura(enaz,encok):
    deneme=[]
    yb�l�t=[]
    yeksit=[]
    for i in range(enaz,encok+1):
        deneme.append(2**i)
    for dene in deneme:
        ysay�s�=0
        tsay�s�=0
        for n in range(dene):
            if(random.choice(('Y','T'))=='Y'):
                ysay�s�+=1
            else:
                tsay�s�+=1
        yb�l�t.append(ysay�s�/tsay�s�)
        yeksit.append(abs(ysay�s�-tsay�s�))
    pylab.title('Yaz�-Tura Fark�')
    pylab.xlabel('Deneme Say�s�')
    pylab.plot(deneme,yeksit)
    pylab.figure()
    pylab.title('Yaz�/Tura Oran�')
    pylab.xlabel('Deneme Say�s�')
    pylab.plot(deneme,yb�l�t)