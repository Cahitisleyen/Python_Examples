import  re
dosya = open("deneme.txt","r")

data = dosya.read()

for i in range(len(data)):
    b = re.search("Python",data)
    if b:
        yeni_dosya=open("yeni.txt","w")
        yeni_dosya.write(b.group())

    else:
        print("Aranılan kelime bulunmadı")
        break

