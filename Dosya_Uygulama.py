"""Bu yazımda dosyaya kaydettiğim 0- 10 arasındaki çift sayıların toplamını alıp ekrana yazan örnek yapacağım"""
dosya=open("deneme.txt","w")

for i in range(0,11,2):
    dosya.write(str(i)+'\n')

dosya.close()

dosya1=open("deneme.txt","r")

s=(dosya1.readlines())

data = [int(item.replace("\n", "")) for item in s]

print sum(data)

dosya1.close()
