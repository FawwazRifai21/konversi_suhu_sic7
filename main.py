# Nama: Fawwaz Absyar Rifai
# Kelompok: Ultraquest

from utils import proses_konversi

print("=====KONVERSI SUHU=====")
suhu = int(input("Masukkan nilai suhu: "))
satuan = input("Dari Satuan (C/F/K): ").upper()
konversi = input("Ke Satuan (C/F/K): ").upper()

output = proses_konversi(suhu, satuan, konversi)

print(f'Hasil Konversi: {output}')