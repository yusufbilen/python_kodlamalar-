# Yusuf Bilen 10.01.2022

#soru 1
# print('merhaba bu benim ilk python kodum.')

#soru 3
# print(3*5)
# print(7+4)
# print(3-1)
# print(2**2)
# print(14/7)
# print(15//5)
# print(10%5)

# soru 4
# kullanıcıAadı='yusuf'
# kullanıcısoyAadı='bilen'
# print(kullanıcıAadı + ' ' + kullanıcısoyAadı)

# soru 5
# samsung=(1000*0.05)
# kinetix=(200*0.04)
# vergi=samsung+kinetix
# print(vergi)

# #soru 6
# vize = input('Vize Notunuz : ')
# final = input('Final Notunuz : ')
# ortalama=(float(vize)*0.4)+(float(final)*0.6)
# print("Ortalama :{0} ".format(ortalama))

#soru 7
# r=int(input("Yarı Çapı Girin: "))
# cevre=2*3.14*r
# alan=3.14*r*r
# print("Çevre: ",cevre)
# print("Alan: ",alan)

# soru 8
# kenar=5
# alan = 6 * kenar * kenar
# print("Küpün alanı=" , alan)
# kenar=3
# hacim= kenar * kenar * kenar
# print("Küpün hacmi=" , hacim)
x=[1.5,2,5,6]
y=[0.5,1,2,3]
a=[]
for i in range(x):
    for j in range(y):
        sonuc=i-j
        a.append((sonuc))
print(a)
