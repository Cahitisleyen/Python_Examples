def obeb(sayi1,sayi2):

    for i in range(int((sayi1+sayi2)/2),0,-1):
        if sayi1%i == 0 and sayi2%i ==0:

            break
    return i

def okek(sayi1,sayi2):

    okek=(sayi1*sayi2)/obeb(sayi1,sayi2)
    print(okek)

    return okek

