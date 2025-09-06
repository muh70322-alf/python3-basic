import csv

# 1. Membaca file CSV
def baca_csv(nama_file):
    with open(nama_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for baris in reader:
            print(baris)

# 2. Menulis ke file CSV baru
def tulis_csv(nama_file, data):
    with open(nama_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Nama', 'Umur', 'Kota']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# 3. Menambahkan data baru ke CSV yang sudah ada
def tambah_data_csv(nama_file, data_baru):
    with open(nama_file, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['Nama', 'Umur', 'Kota']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data_baru)

# Contoh penggunaan:
data_awal = [
    {'Nama': 'Andi', 'Umur': 25, 'Kota': 'Jakarta'},
    {'Nama': 'Budi', 'Umur': 30, 'Kota': 'Bandung'},
    {'Nama': 'Citra', 'Umur': 22, 'Kota': 'Surabaya'}
]

# Tulis data awal ke file CSV
tulis_csv('data.csv', data_awal)

# Baca isi CSV
print("Isi file CSV:")
baca_csv('data.csv')

# Tambah satu data baru
data_baru = {'Nama': 'Dina', 'Umur': 28, 'Kota': 'Yogyakarta'}
tambah_data_csv('data.csv', data_baru)

# Baca lagi untuk melihat hasil update
print("\nSetelah menambah data:")
baca_csv('data.csv')
