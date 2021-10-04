x1 = int(input("Sisi kiri  x1: "))
x2 = int(input("Sisi kanan x2: "))
x3 = int(input("Sisi bawah x3: "))

if x1 + x2 <= x3 or x1 + x3 <= x2 or x2 + x3 <= x1 :
    print("Bukan segitiga")
elif x1 == x2 and x2 == x3 :
    print("Segitiga sama sisi")
elif x1 == x2 or x1 == x3 or x2 == x3 :
    print("Segitiga sama kaki")
elif x1*x1 + x2*x2 == x3*x3 or x1*x1 + x3*x3 == x2*x2 or x3*x3 + x2*x2 == x1*x1 :
    print("Segitiga Siku-siku")
else:
    print("Segitiga sembarang")
