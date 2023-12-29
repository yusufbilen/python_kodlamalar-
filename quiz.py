class ogrenci:
    def _init_(self,isim,soyad,vize,final):
        self.ad=isim
        self.soyisim=soyad
        self.not1=vize
        self.not2=final
    def hesap(self):
        ortalama = (self.not1*0.4)+ (self.not2*0.6) 
        if (ortalama>=85):
            print("Harf notunuz : AA0")
        elif(ortalama>=70 and ortalama <85):
            print("Harf notunuz : BA")
 
        elif(ortalama>=60 and ortalama <70):
            print("Harf notunuz : BB")
 
        elif (ortalama >= 45 and ortalama < 60):
            print("Harf notunuz : CB")
 
        elif(ortalama>=0 and ortalama <45):
            print("Harf notunuz : FF")

def selection_sort(liste):
    for i in range(0,len(liste)-1):
        minındex=i
        for j in range(i+1,len(liste)):
            if liste[j]<liste[minındex]:
                minındex=j
        if minındex!=i:
            liste[i],liste[minındex]=liste[minındex],liste[i]
            print(liste)



