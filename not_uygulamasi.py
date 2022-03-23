def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    vize = int(notlar[0])
    final = int(notlar[1])


    ortalama = ((vize*40/100) + (final*60/100))

    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 85 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 80 and ortalama <= 84:
        harf = "BB"
    elif ortalama >= 75 and ortalama <= 79:
        harf = "CB"
    elif ortalama >= 70 and ortalama <= 74:
        harf = "CC"
    elif ortalama >= 65 and ortalama <= 69:
        harf = "DC"
    elif ortalama >= 60 and ortalama <= 64:
        harf = "DD"
    elif ortalama >= 50 and ortalama <= 59:
        harf = "FD"
    else:
        harf = "FF"
    
        
    return ogrenciAdi + ": " + harf + "\n"


def notlari_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
  
def not_gir():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    vize = input("Vize notu: ")
    final = input("Final notu: ")

    with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
        file.write(ad+' '+ soyad+ ':'+vize+','+final+'\n')

def not_kayit():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)



while True:


    islem = input("1- Notları Oku\n2- Not gir\n3- Notları Kayıt Et\n4- Çıkış\n")
    
    if islem == "1":
        notlari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        not_kayit()
    else:
        break
