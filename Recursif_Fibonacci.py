def fibo(sayi):
    if sayi==0:return 0

    if sayi==1:return 1

    return fibo(sayi-1) + fibo(sayi-2)

sayi=input("Bir sayi gir :")
print fibo(sayi)
