# Nama  : Mahmud S Laopo
# Nim   : 20210801203
# TUGAS PBO - Sesi 4


def hitungPPN():
    nilaiA = int(input("Masukan Nilai Pertama: "))
    nilaiB = int(input("Masukan Nilai Kedua: "))
    persen = "10"
    if nilaiA is not None and nilaiB is not None:
        hasilTotal = int(nilaiA) + int(nilaiB)
        hasilPersen = (int(hasilTotal) * int(persen) / 100)
        hasilPPN = int(hasilTotal) - int(hasilPersen)
        return print(
            "\n" + 
            "Nilai pertama: Rp." + str(nilaiA) + "\n" + 
            "Nilai kedua: Rp."  + str(nilaiB) + "\n" + 
            "Total hasil: Rp." + str(hasilTotal) + "\n" +
            "Hasil perhitungan PPN 10%: Rp." + str(hasilPPN) + "\n"
        )
    else:
        print("Nilai tidak boleh kosong!!!")

hitungPPN()