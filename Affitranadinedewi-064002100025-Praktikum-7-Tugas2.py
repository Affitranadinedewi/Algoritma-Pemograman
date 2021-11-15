@author: ID20072
Nama : Affitra Nadine Dewi
Nim : 064002100025
"""

def convert(list):
    x = sum(d * 10**i for i, d in enumerate(list[::-1]))
    return x

def define2(x):
    if x == 2:
        return '"nd"'
    elif x == 3:
        return '"rd"'
    elif x == 1:
        return '"st"'
    else:
        return '"th"'
    
def define1(x):
    res = [int(x) for x in str(angka)]
    if len(res) >= 2:
        akhir2 = list()
        akhir2.append(res[-2])
        akhir2.append(res[-1])
        che = convert(akhir2)
        if che == 11 or che == 12 or che == 13:
            return 'th'
        else:
            return define2(res[-1])
    else:
        return define2(x)

while True:    
    try:  
        print()
        angka = int(input('enter numbers: '))
    except ValueError:
        print('INVALID')
    else:
        hasil = define1(angka)
        print(str(angka)+hasil)
