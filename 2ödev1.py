
# Soru 0: Ekrana Merhaba yazdiran programi yaziniz.
# print('Merhaba')

# Soru1: Kullanicidan bir sayi alip bu sayinin OBEB be OKEK ini bulan programi yaziniz.
# Yanitinizi buraya yaziniz

# sayı1=int(input("1. SAYIYI GİRİNİZ: "))
# sayı2=int(input("2. SAYIYI GİRİNİZ: "))
# if (sayı1>sayı2):
#     kucuksayı=sayı2
# else:
#     kucuksayı=sayı1
# for a in range (1,kucuksayı+1):
#     if (sayı1 % a==0) and (sayı2 % a==0):
#         ebob=a
# print("Obeb= ",ebob)
# print("Okek= ",(sayı1*sayı2)//ebob)



# Soru2: Celcius cinsinden girilen sicaklik degerini Fahrenheit ve Kelvin e ceviren programi yaziniz.
# Yanitinizi buraya yaziniz

# def	derece():
# 	celsius	= eval(input("Fahrenheit cinsinden istenilen celcius derecesi: "))
# 	fahrenheit = (9/5) * celsius + 32
# 	print("Sıcaklık",fahrenheit,"Fahrenheit	derecedir.")
# derece()
# def derece2():
#     celsius=eval(input("Kelvin cinsinden istenilen celcius derecesi: "))
#     kelvin= celsius + 273,15
#     print("Sıcaklık",kelvin,"Kelvin derecedir.")
# derece2()


# Soru3: Mil cinsinden girilen mesafeyi kilometreye ceviren programi yaziniz.

# mil = float(input("Mil Giriniz: "))
# kat_sayı = 1.609344
# km = mil * kat_sayı
# print('{0} mil = {1} kilometre. '.format(mil,km))


# Soru4: Girilen sayinin tek mi cift mi oldugunu soyleyen programi yaziniz.

# sayi = input('Sayı : ')
# if(int(sayi)%2==0):
#       print("Sayı Çift")
# else:
#       print("Sayı Tek")


# Soru5: 1'den kullanici tarafindan girilen sayiya kadar olan tum sayilarin carpimini bulan programi yaziniz
# s = input('Sayı Girin : ')
# try:
#     if int(s)>=1:
#         i =1
#         çarpım = 1
#         while (i<=int(s)):
#             çarpım = çarpım * i
#             i = i + 1
#     print("1 ve {0} arası sayıların çarpımı = {1}".format(s,çarpım))
# except:
#     print("Lütfen Sayı girişi yapın.")

# Soru6: Kullanicdan bir terim sayisi alip bu terim sayisina uygun sekilde fibonacci serisini 
# hesaplayarak ekrana terimleri yazdiran programi yaziniz. 
# Ornegin terim sayisi 6 girilirse ekranda 0 1 1 2 3 5 yazmalidir.
# def  fibonacci(sınır):
#     sayi1=0
#     sayi2=1
#     print(sayi1)
#     print(sayi2)
#     i=0
#     while(i<sınır-2):
#         sayi3=sayi1+sayi2
#         print(sayi3)
#         sayi1=sayi2
#         sayi2=sayi3
#         i+=1
# sınır=int(input("Fibonaccinin bulunmasını istediğiniz sayı: "))
# fibonacci(sınır)


# Soru7: Girilen bir sayinin ASAL sayi olup olmadigini bulan programi yaziniz.
# sayi=int(input("Sayıyı Girin : "))
# if sayi > 1:
#    for i in range(2,sayi):
#        if (sayi % i) == 0:
#            print(sayi," Asal Sayı Değildir.")
#            break
#    else:
#        print(sayi," Asal Sayıdır.")
 
# else:
#    print(sayi," Asal Sayı Değildir.")



# Soru8: 2'den baslayarak girilen sayiya kadar tum asal sayilari yazdiran programi yaziniz.
# sayi = int(input("Sayi Giriniz:"))
# sayac=0 
# toplam=0
# sayac2=0
# for i in range(2,(sayi+1)):
#     sayac=0
#     for a in range(2,i):
#         if(i%a==0):
#             sayac=sayac+1
#             break
#     if(sayac==0):
#         print(i)
#         sayac2=sayac2+1
        
# print("Toplam ",sayac2," adet asal sayı var.")



# Soru9: Kullanicidan 5 adet sayi alip daha sonrasinda girilen bu 5 sayinin en buyuk ve en kucuk
#degerlerini bulan programi yaziniz. (min ve max methodlarini KULLANMADAN)
# lst = []
# adet = int(input('Kaç Sayı Girilecek: '))
# for n in range(adet):
#     sayi = int(input('Sayıyı Gir: '))
#     lst.append(sayi)
# print("Liste İçindeki En Büyük Sayı :", max(lst), "\nListe İçindeki En Küçük Sayı :", min(lst))   


# Soru10: Kullanicidan bir karakter dizisi alip daha sonra kullaniciya 3 secenekden sunan
# 1-) hepsi kucuk
# 2-) HEPSI BUYUK
# 3-) Sadece Bas Harfleri Buyuk
# yapilan tercihe gore girilen karakter dizisinin yazim stilini degistiren programi yaziniz.
# adsoyad=input('karakter giriniz')
# adsoyad = adsoyad.lower()
# print(adsoyad)
# adsoyad=input('karakter giriniz')
# adsoyad = adsoyad.upper()
# print(adsoyad)
# adsoyad=input('karakter giriniz')
# adsoyad = adsoyad.capitalize()
# print(adsoyad)


# Soru11: Kullanicidan bir karakter dizisi ve bir atlama degeri alip bu atlama degerine gore
# stringi atlayarak yazdiran programi yaziniz. 
# for i in range(10):
#     if i ==5:
#         continue
#     print(i)

# Soru12: 1'den baslayarak kullanicidan alinan sayiya kadar olan tum sayilardan tek olanlarinin toplamini
# cift olanlarin carpimini bulup ekrana yazdiran programi yaziniz.
# sayi = input('Sayıyı Girin : ')
# tekToplam=0
# ciftCarpım=1
# for i in range(1,int(sayi)):
#       if(i%2==0):
#             ciftCarpım*=i
#       else:
#             tekToplam+=i
# print("Tek Sayıların Toplamı : {0}".format(tekToplam))
# print("Çift Sayıların Çarpımı : {0}".format(ciftCarpım))


# Soru13: Kullanicidan alinan 2 sayidan buyuk olani donduren fonksiyonu 
# ve bu sayiyi ekrana yazdiran programi yaziniz.
# a = int((input("Lütfen birinci sayıyı giriniz: "))) 
# b = int((input("Lütfen ikinci sayıyı giriniz: "))) 
# if a > b: 
#     print ("Büyük sayı: %d" % a)
# elif b > a: 
#     print ("Büyük sayı: %d" % b)
# else: 
#     print ("Sayılar eşit.")


# Soru14: 1'den baslayarak kullanicidan alinan sayiya kadar olan tum sayilari 
# tek ve cift olarak etiketleyen programi yaziniz. 
# Ornek: 1 TEK 
# 2 CIFT 
# sayı=int(input("Sayı giriniz: "))
# i=0
# while i<sayı:
#     if i%2==1:
#          print(str(i)+" tek sayıdır")
#     else:
#          print(str(i)+" çift sayıdır")
#     i+=1


# Soru15: Kullanicidan bir hiz degeri alan ve girilen hiz 120 den fazlaysa 
# 4 ceza puani 100 ile 120 arasindaysa 2 ceza puani veren ve toplam puan
# 6 yi gectiginde ehliyetinize el konulmustur yazdiran programi yaziniz.

# deger=int(input("HIZ DEĞERİ GİRİNİZ: "))

# if deger>=120:
#     print("4 Ceza puanı aldınız.")
# elif 100<=deger<=120:
#     print("2 Ceza puanı aldınız. ")

# Soru16: 1 den baslayarak kullanicidan alinan sayiya kadar olan sayilar icinde 3 ve 7 ile 
# bolunebilenleri ekrana yazdiran programi yaziniz.
# sayı=int(input("DEĞEER GİRİNİZ: "))
# for i in range(1,sayı):
#   if i%3==0 and i%7==0:
#     print(i)


# Soru17: Kullanicidan alinan sayi degeri kadar ekrana yildiz yazdiran programi yaziniz.
# Ornegin girilen sayi 3 ise
# *
# **
# ***
# karakter='*'
# sayi=int(input("Satır Sayısını GiriniZ:"))
 
# for i in range(sayi):
#     i=i+1
#     print(karakter*i)
    

# Soru18: Girilen dakikayi saat ve dakika seklinde yazdiran programi yaziniz.
# Ornek 123 => 2 saat 3 dakika
# dakika1=int(input("dakikayı giriniz "))
# def saatdakika(dak):
#     if dak<60:
#         print("0 saat",dak,"dakika")
#     elif dak>=60:
       
#         saat=int(dak//60)
#         cevir=dak*60
#         kalandakika=dak-cevir
#         print(saat,"saat",kalandakika,"dakika")
# def saatim(dakika):
#     if dakika<60:
#         saatdakika(dakika)
#     elif dakika>=60:
#         saat=int(dakika//60)
#         saat2=int(saat*60)
#         kalan_dakika=int(dakika-saat2)
#         print(saat,"saat",end=" ")
#         saatdakika(kalan_dakika)  
# saatim(dakika1)


# Soru19: Kullanicidan sinirsiz sayi alan ancak girilen sayi 3 oldugunda sayi almayi durduran 
# ve bunlari bir listede tutarak hem listeyi hemde bu listenin icindeki sayilarin 
# 3. kuvvetini yine farkli bir liste olarak saklayip daha sonra iki listeyide 
# ekranda gosteren programi yazdiriniz.

# Soru20: A=[1,3,4,5,8,12] ve B=[33,35,37,39] olarak verilmistir. Bu listelerinin elemanlarinin 
# kombinasyonlarinin carpimlarinin 3 ile bolunebilenlerini bir listede saklayarak 
# ekrana yazidaran programi yaziniz. Ornegin ilk kombinasyon 1 ve 33. 1*33=33. 33 3 e bolunur.



