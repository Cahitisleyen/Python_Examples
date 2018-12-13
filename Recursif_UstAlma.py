def facto(sayi):
    if sayi==0:
        return 1

    return sayi*facto(sayi-1)
sayi=input("Faktoriyelini bulmak istediginiz sayiyi girin : ")
print facto(sayi)
