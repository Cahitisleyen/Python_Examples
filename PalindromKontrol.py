def palindrom(kelime):
    if len(kelime)<=1:
        return True
    else:
        return kelime[0]==kelime[-1] and palindrom(kelime[1:-1])
kelime=raw_input("Bir kelime gir :")
print palindrom(kelime)
