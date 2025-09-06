print("MATERI 8A - FUNCTION BASIC")
print("==========================")
# function di awali dengan keyword `def`
def halo_ngab():
  print("Halo Ngab")
# function dengan parameter `nama`
def sapa_sapa(nama):
  print("Halo bang ", nama)
  print("Apa kabs bang", nama)
  print("-------------")

print("Cobain fungsinya:")
halo_ngab()
sapa_sapa("Fino")
sapa_sapa("Azzam")
sapa_sapa("Wildan")

# fungsi luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
  print("> Panjang: ", panjang)
  print("> Lebar: ", lebar)
  rumus = panjang * lebar
  print("Luas persegi panjang =", rumus)

luas_persegi_panjang(10, 20)
luas_persegi_panjang(30, 50)