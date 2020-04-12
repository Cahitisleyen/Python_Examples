def Rehbere_Kisi_Ekle(isim,soyisim,telefon,email):
    with open('rehber.txt', 'w') as file:
        file.write(isim+','+ soyisim +','+ telefon +','+ email+'\n')


def Telefon_Numarasi_Bul(isim):
    with open('rehber.txt', 'r') as file:
        rehber = file.read()

        rehber_liste = rehber.split(',')
        for i in rehber_liste:
            if isim in rehber_liste:
                print('Tel No :',rehber_liste[2])
                break


def Telefon_Numarasi_Guncelle(isim,telefon):
    with open('rehber.txt', 'r+') as file:
        rehber = file.readlines()
        for kisi in rehber:
            if isim in kisi.split(','):
                rehber.remove(kisi)
                rehber.append(str(kisi.replace(kisi.split(',')[2],telefon)))
                file.seek(0)
                file.truncate(len(rehber))
                #file.seek(file.tell())
                file.writelines(rehber)
                break


def Tum_Rehber_Goster():
    with open('rehber.txt', 'r') as file:
        rehber = file.readlines()
        for i in rehber:
            print(i)



print('''
1.) Kisi Ekle
2.) Kisi Bul
3.) Kisi Guncelle
4.) Tum Kisileri Goster
Cikmak icin q
''')
while True:
    select = input('Bir tercih yapin :')

    if select == '1':
        isim = input('Isim Girin :')
        soyisim = input('Soyisim Girin :')
        telefon = input('Telefon No Gir :')
        email = input('Email Gir  :')
        Rehbere_Kisi_Ekle(isim, soyisim, telefon, email)

    elif select == '2':
        isim = input('Isim Girin :')
        Telefon_Numarasi_Bul(isim)

    elif select == '3':
        isim = input('Isim Girin :')
        telefon = input('Telefon No Gir :')
        Telefon_Numarasi_Guncelle(isim, telefon)

    elif select == '4':
        Tum_Rehber_Goster()

    elif select=='q':
        exit()
