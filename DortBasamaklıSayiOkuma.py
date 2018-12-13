sayi=input("bir sayi girin :")
yeni_liste=[]

binler1=sayi/1000
sayi=sayi-binler1*1000
yuzler1=sayi/100
sayi=sayi-yuzler1*100
onlar1=sayi/10
sayi=sayi-onlar1*10
birler1=sayi
binler={1:"bin",2:"ikibin",3:"ucbin",4:"dortbin",5:"besbin",6:"altibin",
        7:"yedibin",8:"sekizbin",9:"dokuzbin"}
yuzler={1:"yuz",2:"ikiyuz",3:"ucyuz",4:"doryuz",5:"besyuz",6:"altiyuz",
        7:"yediyuz",8:"sekizyuz",9:"dokuzyuz"}
onlar={1:"on",2:"yermi",3:"otuz",4:"kirk",5:"elli",6:"altmis",
        7:"yetmis",8:"seksen",9:"doksan"}
birler={1:"bir",2:"iki",3:"uc",4:"dort",5:"bes",6:"alti",
        7:"yedi",8:"sekiz",9:"dokuz"}
for i in binler:
        if binler1==i:

                yeni_liste.append(binler.get(binler1))

for i in yuzler:
        if yuzler1==i:
                yeni_liste.append(yuzler.get(yuzler1))
