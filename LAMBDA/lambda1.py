

#fungsi biasa dg def
def hello_world(name):
    print("Hello Mr., name")
    print(f"How are you doing {name}?")

hello_world("yuyu")          
hello_world("nana")
hello_world("duda")          
print("---------> LAMBDA <--------")
#fungsi anonim dengan'lambda' jika 1 baris yg lain
greeting = lambda name: print(f"Hello, {name} With lambda")
greeting("yuyu")
greeting("nana")
greeting("duda")
print("---------MAP .KONVERSI TYPE DATA---------")
#""artinya string walaupun dia isinya angka 
nilai_string = "1000" #type data string
nilai_integer = int(nilai_string)#int (ubah menjadi integer)
kalikan_dua_salah = nilai_string * 2
kalikan_dua_benar = nilai_integer * 2
print(kalikan_dua_salah, kalikan_dua_benar)

# map ()untuk metransformasi data dari list 
# map ([fungsi_perubahan_data]), [sumber_data])
nilai_mentah = [100, 29, 55, 82, 75, 30]
nilai_kali_seratus = map(lambda nilai:nilai * 100, nilai_mentah)
# konversii map objek menjadi list
list_nilai_kali_seratus = list(nilai_kali_seratus)
print("nilai mentahan: {nilai_mentah}")
print(f"nilai x 100: {list_nilai_kali_seratus}")

daftar_angka = [
    {"nama": "udin", "angka": 67},
    {"nama": "gojo", "angka": 79},
    {"nama": "bobo", "angka": 82},
    {"nama": "vian", "angka": 75},
]

print("DAFTAR ANGKA ASLI", daftar_angka)
daftar_siswa_terurut = sorted(daftar_angka, key=lambda siswa:
siswa['angka'])
# for loop ->mengeluarkan seluruh isi daftar
for siswa in daftar_siswa_terurut:
    print(siswa)
daftar_nama_kelas_b = ["vino", "nana", "cucu", " andra", "mono"]
daftar_nama_terurut = sorted(daftar_nama_kelas_b) #a ke z (kecil-besar)
daftar_nama_terbaik = sorted(daftar_nama_kelas_b) #z ke a (besar ke kecil)
for nama in daftar_nama_terurut:
    print(nama)
print("-----------#######-----------")
for nama in daftar_nama_terbaik:
  print(nama)


#filter()menyaring data 
transaksi = [30000,100000,25000,35000,15000]
transaksi_besar = filter(lambda angka: angka >= 30000, transaksi)
list_transaksi_besar =list(transaksi_besar)
print("data transaksi:", transaksi)
print("Transaksi di atas 30rb:", list_transaksi_besar)





