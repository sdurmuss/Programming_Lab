import random
def get_n_random_integer(n):
    random.seed(100)#100den baþlayýp sayý üretme
    numbers = []
    for i in range(n):
        s = random.randint(-100,100)
        numbers.append(s)
    return numbers

def get_mean_for_n_integer(numbers):#ortalama
    toplam = 0
    kactane = 0
    for sayi in numbers:
        toplam = toplam + sayi
        kactane = kactane + 1
    return toplam / kactane
    
    
def get_std_for_n_integer(numbers):#standart sapma
    toplam = 0
    kactane = 0
    ortalama = get_mean_for_n_integer(numbers)
    
    for sayi in numbers:
        toplam = toplam + (sayi - ortalama) ** 2
        kactane = kactane + 1
        
    varyans_1 = toplam / (kactane - 1)
    std_1 = varyans_1 ** 0.5 #kok alma
    return std_1
    
def normalizasyon(numbers):
    new_numbers = []
    ortalama = get_mean_for_n_integer(numbers)
    standart_sapma = get_std_for_n_integer(numbers)
    for x in numbers:#her sayýdan ortalama çýkart standart sapmaya böl
        new_x = (x - ortalama) / standart_sapma
        new_numbers.append(new_x)
    return new_numbers
    
def get_mean_one_std_neighbor_ratio(numbers):
    kac_tane = 0
    toplam_kac_sayi = len(numbers)
    
    ortalama = get_mean_for_n_integer(numbers)
    standart_sapma = get_std_for_n_integer(numbers)
    
    low = ortalama - standart_sapma
    high = ortalama + standart_sapma
    #belli aralýklarda sayýlarýn gelme olasýlýðý
    
    for x in numbers:
#        toplam_kac_sayi=toplam_kac_sayi+1
        if(x > low and x < high):
            kac_tane = kac_tane + 1
    return kac_tane / toplam_kac_sayi
    
#insertion sort---------------
#daha önceki sayýlarý karþýlaþtýr ihtiyaç varsa yer deðiþtir. 
def insertion(numbers):
    sayilar_2 = numbers
    length_1 = len(sayilar_2)
    
    karsilastima_sayisi = 0
    swap_sayisi = 0
    for i in range(1, length_1):
        for j in range(i, 0, -1):
            karsilastima_sayisi += 1
            if(sayilar_2[j] < sayilar_2[j - 1]):
                #swap
                swap_sayisi += 1
                temp = sayilar_2[j - 1]
                sayilar_2[j - 1] = sayilar_2[j]
                sayilar_2[j] = temp
            else:
                break
    
    return sayilar_2, swap_sayisi, karsilastima_sayisi
 
def get_mean_of_swap_in_insertion(num_trials,num_int):
    swap_sayilari = []
    for i in range(num_trials):
        sayilar_1 = get_n_random_integer(num_int)
        sayilar_2 = insertion(sayilar_1)
        s_1 = sayilar_2[1]#yer deðiþtirme sayisini bana ver
        swap_sayilari.append(s_1)
        
    mean_1 = get_mean_for_n_integer(swap_sayilari)
    std_1 = get_std_for_n_integer(swap_sayilari)
    return num_int, mean_1, std_1
    
def bubbleSort(arr): 
    n = len(arr) 
    karsilastirma_sayisi = 0
    yer_degistirme_sayisi = 0
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            karsilastirma_sayisi += 1
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                yer_degistirme_sayisi += 1
                arr[j], arr[j+1] = arr[j+1], arr[j] 

    return arr,yer_degistirme_sayisi,karsilastirma_sayisi

sayilar = get_n_random_integer(10)
print("sayilar \t: ",sayilar)
print("ortalama \t: ",get_mean_for_n_integer(sayilar))
print("standart sapma \t: ",get_std_for_n_integer(sayilar))
yeni_sayilar = normalizasyon(sayilar)
print("normalizasyon \t: ",yeni_sayilar)
print("normalizasyon ortalamasý : ",get_mean_for_n_integer(yeni_sayilar))
print("normalizasyon standart sapma \t: ",get_std_for_n_integer(yeni_sayilar))
sayilar_1 = get_n_random_integer(100)
print("-->",get_mean_one_std_neighbor_ratio(sayilar_1))
print("\n\n")



print("-->",sayilar)
ss = insertion(sayilar)
print("insertion sort : ",ss[0])
print("swap sayisi : ",ss[1])
print("karsilastirma sayisi : ",ss[2])
#print([i for i in range(10,-1,-1)])

print(get_mean_of_swap_in_insertion(10,10))
print("\n\n")
ss2 = get_n_random_integer(10)

bb = bubbleSort(ss2)
print("sayilar ->",ss2)
print("bubble sort ->",bb[0])
print("bubble swap sayisi ->", bb[1])
print("bubble karsilastirma sayisi ->", bb[2])