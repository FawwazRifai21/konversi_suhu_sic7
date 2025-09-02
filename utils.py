def proses_konversi(suhu, satuan, konversi):
    if satuan == 'C' and konversi == 'F':
        hasil = (suhu * 9/5) + 32
    elif satuan == 'C' and konversi == 'K':
        hasil = suhu + 273.15
    elif satuan == 'F' and konversi == 'C':
        hasil = (suhu - 32) * 5/9
    elif satuan == 'F' and konversi == 'K':
        hasil = (suhu - 32) * 5/9 + 273.15
    elif satuan == 'K' and konversi == 'C':
        hasil = suhu - 273.15
    elif satuan == 'K' and konversi == 'F':
        hasil = (suhu - 273.15) * 9/5 + 32
    else:
        hasil = suhu
    return hasil