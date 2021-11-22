print(“Isi dengan Source Code kalian ya…”)
@author: Affittra Nadine Dewi
"""

print("fungsi perpangkatan menggunakan konsep rekursif")
print("program pemangkatan negatif dan positif")

def pangkat(base, power):
    if power == 0:
        return 1
    elif power < 0:
        return 1 / (base * pangkat(base, abs(power)-1))
    else:
        return base * pangkat(base, power-1)

while True:
    base = int(input("angka dimasukkan : "))
    power = int(input("pangkat dimasukkan : "))
    print(pangkat(base, power),"\n")
