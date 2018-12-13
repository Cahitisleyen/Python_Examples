import sqlite3,os

data=sqlite3.connect("kamu.db")

db="kamu.db"
im=data.cursor()

im.execute("""CREATE TABLE IF NOT EXISTS personel(
    ad TEXT,
    soyad TEXT,
    maas INTEGER

)""")
print "(1)Veri Ekleme"
print "(2)Tablo Goruntulemek icin"
secim=raw_input("Lutfen bir secim yapin :")
if secim=="1":
    ad=raw_input("Ad :")
    soyad=raw_input("Soyad :")
    maas=input("Maas :")

    im.execute("""INSERT INTO personel(ad,soyad,maas) VALUES(?,?,?)""",(ad,soyad,maas))
    data.commit()

elif secim=="2":
    if not os.path.exists(db):
        print "veritabani bulunamadi"
    else:
        im.execute("""SELECT * FROM personel""")

        veriler=im.fetchall()
        for veri in veriler:
            print veri

