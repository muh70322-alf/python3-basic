print("MATERI 7B - PYTHON DATA STRUCTURE")
print("==================================")
# set -> { } -> tidak berurutan, berubah, tidak duplikat
game_irkham = {"valorant", "drak soul"}
game_cici = {"valorant", "mlbb"}
print("Irkham games: ", game_irkham)
print("Cici games: ", game_cici)
# add (menambahkan item baru)
game_irkham.add("minicreaft")
game_cici.add("venom")
# remove (menghapus item)
game_irkham.remove("drak soul")
game_cici.remove("mlbb")
# len(menghitung jumlah item)
print("Irkham ada ", len(game_irkham)," games: ",game_irkham)
print("Cici ada ", len(game_cici)," games: ",game_cici)
# union ->(mengabungkan 2 set berbeda)
game_berdua =game_irkham.union(game_cici)
total_game = len(game_berdua)
print("semua game ada ", total_game ," games: ", game_berdua)
# intersection( -> mencari item yang kembar)
# difference (-> mencari item yg beda)
game_kembar = game_irkham.intersection(game_cici)
game_beda = game_irkham.difference(game_cici)
total_game_kembar = len(game_kembar)
total_game_beda = len(game_beda)
print("game yg kembar ", total_game_kembar ,"game:", game_kembar)
print("game yg beda ", total_game_beda ,"game:", game_beda)
# berurutab berdasarkan key
# key tidak boleh duolikat
koleksi_makanan = {
  "soto": "nano",
  "mie_ayam": "pak_yanto",
  "waifu": {
    "soto": "soto_ayam",
    "bebek": "bebek_bakar",
  }
}
print("Kolekasi Makanan: ", koleksi_makanan)
print("pengen ngemis mie ayam:", koleksi_makanan["mie_ayam"])
print("Waifu soto:", koleksi_makanan["waifu"]["soto"])

# menambah atau mengubah data dict
koleksi_makanan["mie_ayam"] = "ayam geprek"
koleksi_makanan["soto"] = "mi goreng"




