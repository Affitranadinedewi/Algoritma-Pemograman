Created on Mon Dec 13 23:16:34 2021

@author: ID20072
"""

	

class OOP:
	    def __init__(self,nama,nilai):
	        self.nama = nama
	        self.nilai = nilai
	                
	    def printtampil(self):
	        print('Nama: ',self.nama,'\nNilai: ',str(self.nilai))
	        
a = False 
	

while (not a ):
	    try:    
	        print("==== Progam OOP ====")
	        print("1.Mendeklarasikan Objek")
	        print("2.Menampilkan Objek")        
	        print("3.Merubah Nilai Objek")
	        print("4.Menghapus Objek")
	        print("5.Keluar dari Program")
	        print("")
	        number = int(input("Masukkan pilihan angka(1/2/3/4/5):"))
	        if number == 5:
	            a = True
	            print("thank you")
	        
	        elif number == 1:
	            name = input('Masukkan nama: ')
	            skor = input('Masukkan nilai: ')
	            copy = OOP(name, skor)
	            print("Data Berhasil Ditambahkan\n")
	            
	        elif number == 2:
	            copy = OOP(name, skor)
	            copy.printtampil()
	            print('\n')
	            
	        elif number == 3:
	            ganti = input('Apakah anda ingin mengganti?(nama/nilai): ')
	            if ganti == 'nama':
	                name = input('Masukkan nama: ')
	                print('Data Nama Berhasil Diganti\n')
	            if ganti == 'nilai':
	                nilai = input('Masukkan nilai: ')
	                print('Data Nilai Berhasil Diganti\n')
	        
	        elif number == 4:
	            print('Data berhasil dihapus\n')
	            nama = 'none'
	            nilai = 'none'
	        
	        else :
	            print ("Silahkan masukkan pilihan angka!!")
	            print("")
	            
	    except ValueError:
	        print("Masukkan pilihan dengan benar!!\n")

