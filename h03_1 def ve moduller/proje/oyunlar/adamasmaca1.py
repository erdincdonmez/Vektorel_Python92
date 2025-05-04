import random
kelimeler = ["taksi","araba","tanker","imza","kobay"]
can = 5
d_list = []
durum = ""
puan = 0
secilen_kelime = ""
tahmin = ""
ipucu = 3
kontrol_k = ""
def harf_tarama():
    global d_list,secilen_kelime,tahmin,d_list
    for x,y in enumerate(secilen_kelime):
        if y == tahmin:
            d_list[x] = tahmin
def kontrol():
    global d_list,kontrol_k
    kontrol_k = ""
    for i in d_list:
        kontrol_k += i
    if kontrol_k == secilen_kelime:
        return False
    else:
        return True
while can > 0:
    ipucu = 3
    sayi = random.randint(0,len(kelimeler) - 1)
    secilen_kelime = kelimeler[sayi]
    durum = len(secilen_kelime)* "-"
    d_list = list(durum)
    print(len(secilen_kelime),"harfli bir kelime arıyorsunuz:\n",durum)
    tahmin = input("Tahmininizi giriniz:")
    if bool(tahmin) != True:
        exit()
    while bool(tahmin) == True and can > 0 and kontrol and ipucu > 0:
        if kontrol_k == secilen_kelime:
            puan += 30
            print("Doğru harfler! Puanınız:",puan)
            break
        if tahmin == secilen_kelime:
            puan += 50
            print("Doğru tahmin! Puanınız:",puan)
            break
        if len(tahmin) == 1 and kontrol():
            harf_tarama()
            print(d_list)
            ipucu -= 1
            print("Kalan ipucu:",ipucu)
            tahmin = input("Tahmininizi giriniz:")
        else:
            puan -= 10
            can -= 1
            print("Yanlış tahmin! Doğrusu:",secilen_kelime,"\nPuanınız:",puan,"Kalan can:",can)
            break
print("Final skoru:",puan)
