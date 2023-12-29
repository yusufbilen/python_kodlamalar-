# YUSUF BİLEN      ALGORİTMA VE PROGRAMLAMA II         FİNAL SINAVI

# #SORU1:

# def sayma(x):
#     print(x)
#     if x ==20:
#         return
#     sayma(x+3)
# sayma(5)


#SORU2:

# #GLOBAL ÖRNEĞİ: BU ÖRNEKTE EN BAŞTA BULUNAN VE TANIMLANAN DEĞİŞKEN ALTINDA BULUNAN FONKSİYONLARDA DEĞİŞTİRİLMEDİĞİ SÜRECE HER ÇAĞIRILDIĞINDA
# # İLK TANIMLANAN DEĞİŞKENİ EKRANA YAZDIRIR.

# ad="yusuf"          #GLOBAL

# def fonsiyon():
#     ad="bilen"     #ENCLOSİNG
#     #print(ad)
#     def altfonsiyon():
#         ad="muş"     #LOCAL
#       #  print(ad)
#     altfonsiyon()
# fonsiyon()
# print(ad)

# # ENCLOSİNG ÖRNEĞİ: BU ÖRNEKTE GLOBAL'IN ALTINDA TANIMLANAN FONKSİYONLARDA GLOBAL YERİNE TANIMLANAN DEĞİŞKENLER ARTIK FONKSİYON
# # HER ÇAĞIRILDIĞI ZAMAN YENİ DEĞER EKRANA YAZDIRILACAKTIR.

# ad="yusuf"              #GLOBAL

# def fonsiyon():
#     ad="bilen"         #ENCLOSİNG
#     print(ad)
#     def altfonsiyon():
#         ad="muş"     #LOCAL
#       #  print(ad)
#     altfonsiyon()
# fonsiyon()
# #print(ad)

# LOCAL ÖRNEĞİ: BU ÖRNEKTE İÇ İÇE 2 FONKSİYON TANIMLANSA BİLE EN ALT FONSİYON İÇİNDE DEĞİŞTİRİLEN YENİ DEĞER FONSİYON HER 
# ÇAĞIRILDIĞI ZAMAN KULLANILIR.

# ad="yusuf"          #GLOBAL

# def fonsiyon():
#     ad="bilen"     #ENCLOSİNG
#     #print(isim)
#     def altfonsiyon():
#         ad="muş"     #LOCAL
#         print(ad)
#     altfonsiyon()
# fonsiyon()
# print(ad)


#SORU3:


# class Ev:
#     def _init_(self,semt,oda,yılı,metre):
#         self.isim=semt
#         self.odasayısı=oda
#         self.yas=yılı
#         self.buyukluk=metre
#     def kacyıl(self):
#         return 2022-self.yas
#     def fiyat (self):
#         return ((self.isim)(self.odasayısı)(self.buyukluk))/(self.yas)
# e1=Ev(3,4,2020,200)
# print(f"{e1.kacyıl()} yaşındayım")
# print(f"{e1.fiyat()} fiyat değerindeyim")


#SORU4:

# "Quadratic Complexity (O(n^3))" cinsinden yazılmıştır.

#soru5:
# def insertion_sort(liste):         # Bir liste tanımlıyoruz def fonksyonunun içinde
#     for i in range(1,len(liste)):  # 
#         for j in range(i-1,-1,-1):
#             if liste[j+1]<liste[j]:
#                 liste[j],liste[j+1]=liste[j+1],liste[j]
#                 print(liste)
#             else:
#                 break
#     return liste

# import random
# import timeit
# liste=random.sample(range(1,1000),5)
# print(f"oluşturulan rastgele liste: {liste}")
# starttime=timeit.default_timer()
# siraliliste=insertion_sort(liste)
# endtime=timeit.default_timer()
# print(siraliliste)
# print(endtime-starttime)

#soru6:

# def bubble_sort(liste):
#     for i in range(0,len(liste)-1):
#         for j in range(0,len(liste)-1-i):
#             if liste[j]>liste[j+1]:
#                 liste[j],liste[j+1]=liste[j+1],liste[j]
#                 print(liste)

# import random
# import timeit
# liste=random.sample(range(1,1000),5)
# print(f"oluşturulan rastgele liste: {liste}")
# starttime=timeit.default_timer()
# siraliliste=bubble_sort(liste)
# endtime=timeit.default_timer()
# print(siraliliste)
# print(endtime-starttime)

#soru7:

# def selection_sort(liste):
#     for i in range(0,len(liste)-1):
#         minındex=i
#         for j in range(i+1,len(liste)):
#             if liste[j]<liste[minındex]:
#                 minındex=j
#         if minındex!=i:
#             liste[i],liste[minındex]=liste[minındex],liste[i]
#             print(liste)

# import random
# import timeit
# liste=random.sample(range(1,1000),5)
# print(f"oluşturulan rastgele liste: {liste}")
# starttime=timeit.default_timer()
# siraliliste=selection_sort(liste)
# endtime=timeit.default_timer()
# print(siraliliste)
# print(endtime-starttime)
