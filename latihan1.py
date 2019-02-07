print("Mencari Bilangan Terbesar dari 3 Bilangan")
a = int(input("Input Bilangan 1 : "))
b = int(input("Input Bilangan 2 : "))
c = int(input("Input Bilangan 3 : "))

if a>b :
    if a>c :
        print(a)
    else :
        print(c)
else : 
    if b>c :
        print(b)
    else :
        print(c)
