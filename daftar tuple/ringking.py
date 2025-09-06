if __name__ == "__main__":
    data_siswa = [
        {"nama": "Andi", "nilai": 90},
        {"nama": "Budi", "nilai": 95},
        {"nama": "Citra", "nilai": 90},
        {"nama": "Dina", "nilai": 85}
    ]

    hasil_rangking = daftar_nilai_tertinggi=(data_siswa)

    for siswa in hasil_rangking:
        print(f"{siswa['nama']} - Nilai: {siswa['nilai']}, Rank: {siswa['nilai']}'rank tertinggi'")
