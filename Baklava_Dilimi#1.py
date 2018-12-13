
boyut=int(input("boyut gir :"))
for i in range(boyut):
    for k in range((boyut)-i):
        print(" ",end="")


    for m in range(i*2-1):
        print("*",end="")

    print()

for i in range(boyut,0,-1):
    for k in range((boyut)-i):
        print(" ",end="")


    for m in range(i*2-1):
        print("*",end="")

    print()
