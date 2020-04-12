print("""
1.) Yeni Kayit
2.) Kayit Guncelle
3.) Tum Kayitlari Goster
4.) Kayit Ara
5.) Kayit Sil
6.) Kayit Yazdir
0.) Cikis
""")
import sqlite3

okul = sqlite3.connect('okul.db')
imlec = okul.cursor()

imlec.execute('CREATE TABLE IF NOT EXISTS ogrenci (Ogr_adi TEXT,Ogr_Soyadi TEXT,Ogr_no INTEGER)')


while True:
    select = int(input('Bir secenek girin cikmak icin q basin :'))

    if select==1:
        Ogr_adi = input('Ogrenci ismi girin :')
        Ogr_soyadi = input('Ogrenci soyadi girin :')
        Ogr_no = int(input('Ogrenci no girin :'))
        imlec.execute('INSERT INTO ogrenci(Ogr_adi,Ogr_soyadi,Ogr_no) VALUES(?,?,?)',(Ogr_adi,Ogr_soyadi,Ogr_no))
        okul.commit()

    elif select==2:
        imlec.execute('UPDATE ogrenci SET  Ogr_adi = "Mehmet" WHERE Ogr_no = 12')
        okul.commit()

    elif select==3:
        imlec.execute('SELECT *FROM ogrenci')
        ogrenciler = imlec.fetchall()

        for ogrenci in ogrenciler:
            print(ogrenci)


    elif select==4:
        Ogr_no = int(input('Aradiginiz kullanici numarasini girin :'))
        imlec.execute('SELECT *FROM ogrenci WHERE Ogr_no ={}'.format(Ogr_no))
        kisi = imlec.fetchall()
        print(kisi)

    elif select==5:
        Ogr_no = int(input('Aradiginiz kullanici numarasini girin :'))
        imlec.execute('DELETE FROM ogrenci WHERE Ogr_no={}'.format(Ogr_no))
        okul.commit()

    elif select==6:
        imlec.execute('SELECT *FROM ogrenci')
        ogrenciler = imlec.fetchall()
        with open('Ogrenciler.txt','w') as file:
            for ogr in ogrenciler:
                file.writelines(str(ogr)+'\n')

    elif select==0:
        exit()

