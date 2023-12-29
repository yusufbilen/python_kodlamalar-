x=[]
toplam=0
c=[]
while True:
    deger=input("x' listesi için değer giriniz: ")
    if deger=="":
        break
    else:
        x.append(float(deger))
print(f"x listesi={x}")
u=len(x)
for i in x:
    toplam=toplam+i
    o=toplam/u
print(f" listenin toplamı={toplam}")
print(f"liste'nin ortalaması={o}")

for i in x:
    toplam_1=(i-o)**2
    c.append(toplam_1)
    d=(sum(c))/(u-1)
import math
s_sapma= math.sqrt(d)
print(f"verilen listenin standart sapması ={s_sapma}")