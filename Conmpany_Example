import  sqlite3

import  time


class Kisi():

    def __init__(self,isim,soyisim,departman,maas,adres,no):

        self.isim=isim
        self.soyisim=soyisim
        self.departman=departman
        self.maas=maas
        self.adres=adres
        self.no=no
    def __str__(self):
        return "İsim :{}\nSoyisim:{}\nDepartman:{}\nMaas:{}\nAdres:{}\nNo:{}".format(self.isim,self.soyisim,self.departman,self.maas,self.adres,self.no)




class Firma():

    def __init__(self):

        self.baglanti_olustur()



    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("Holding.db")
        self.imlec = self.baglanti.cursor()

        tablo= "CREATE TABLE IF NOT EXISTS kisiler(İsim TEXT,Soyisim TEXT,Departman TEXT,Maas INT,Adres TEXT,No INT)"
        self.imlec.execute(tablo)
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def kisileri_goster(self):
        goster ="SELECT *FROM kisiler"

        self.imlec.execute(goster)

        kisiler =self.imlec.fetchall()

        if len(kisiler)==0:
            print("Sistemde kayıtlı kimse yok")
        else:
            for i in kisiler:

                kisi = Kisi(i[0],i[1],i[2],i[3],i[4],[5])
                print(kisi)

    def kisi_sorgula(self,no):
        sorgu="SELECT * FROM kisiler WHERE no =?"
        self.imlec.execute(sorgu,(no,))
        kisiler =self.imlec.fetchall()

        if len(kisiler)==0:
            print("Aranılan Kişi Sistemde Bulunmamaktadır..")

        else:
            kisi =Kisi(kisiler[0][0],kisiler[0][1],kisiler[0][2],kisiler[0][3],kisiler[0][4],kisiler[0][5])
            print(kisi)

    def kisi_ekle(self,kisi):
        ekle ="INSERT INTO kisiler VALUES(?,?,?,?,?,?)"
        self.imlec.execute(ekle,(kisi.isim,kisi.soyisim,kisi.departman,kisi.maas,kisi.adres,kisi.no))
        self.baglanti.commit()

    def kisi_sil(self,isim):

        sorgu="DELETE FROM kisiler WHERE isim = ?"
        self.imlec.execute(sorgu,(isim,))
        self.baglanti.commit()

    def maas_zam(self,no):

        sorgu="SELECT * FROM kisiler WHERE no = ?"
        self.imlec.execute(sorgu,(no,))

        kisiler =self.imlec.fetchall()

        if len(kisiler)==0:
            print("Böyle bir çalışan yok")

        else:
            maas=kisiler[0][3]
            maas +=500
            sorgu2="UPDATE kisiler SET maas = ? WHERE no = ?"
            self.imlec.execute(sorgu2,(maas,no))
            self.baglanti.commit()



print("""
**************************************
ARAS HOLDİNG PERSONEL SİSTEMİ
İŞLEMLER ;
1.KİŞİ EKLE 
2.KİŞİ SORGULAMA
3.KİŞİLERİ GÖSTER
4.KİŞİ SİLME
5.MAAŞ ZAM YAP
Çıkmak için 'q' ye basın
**************************************
""")

kisim = Firma()
while True:
    islem= input("Bir ilem seçin :")

    if islem=="q":
        print("Çıkış yapılıyor...")
        time.sleep(2)
        print("Çıkış Yapıldı")

    elif islem=="1":
        isim = input("İsim :")
        soyisim = input("Soyisim :")
        departman = input("Departman :")
        maas = int(input("Maas:"))
        adres = input("Adres :")
        no = int(input("No :"))

        yeni_kisi = Kisi(isim, soyisim, departman, maas, adres, no)
        print("Kişi Ekleniyor ...")
        time.sleep(2)
        print("Kişi Eklendi")

        kisim.kisi_ekle(yeni_kisi)


    elif islem=="2":
        no =input("Sorgulamak istediğiniz kişinin No'sunu girin :")
        print("Kişi sorgulanıyor ...")
        time.sleep(2)
        kisim.kisi_sorgula(no)
    elif islem=="3":

        kisim.kisileri_goster()



    elif islem=="4":
        no =int(input("Silmek istediğiniz kişinin No' sunu girin :"))
        tekrar =input("Kişiyi silmek istediğinizden emin misiniz(E/H):")
        if tekrar=="E":
            print("Kişi Siliniyor...")
            time.sleep(2)
            print("kişi Sistemden Silindi")
            kisim.kisi_sil()
    elif islem=="5":
        no =int(input("Maaş zam yapmak istediğiniz kişinin No' sunu girin :"))
        print("Zam yapılıyor...")
        time.sleep(2)
        print("Zam yapıldı.")
        kisi.maas_zam()

    else:
        print("Geçersiz işlem")
