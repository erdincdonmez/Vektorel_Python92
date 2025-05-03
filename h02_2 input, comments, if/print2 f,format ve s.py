# f, format ve %s.. kullanımı
Sinav1 = 80
sinav1 = 70 
sinav2 = 90
ortalama = (sinav1+sinav2)//2
print("1-",sinav1 ,"ve",sinav2,"için Ortalaman:", ortalama)
print(f"2-{sinav1} ve {sinav2} için ortalaman: {ortalama}")
print("3-{} ve {} için ortalaman: {}".format(sinav1,sinav2,ortalama))
print("4-%d ve %d için ortalaman: %d"%(sinav1,sinav2,ortalama))



