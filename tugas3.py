

# Tugas Pemograman Berorientasi Objek - Sesi 6
# Nama : MAHMUD S LAOPO
# Nim  : 20210801203

print ("---------------------------------------------------")
print ("menghitung nilai akhir mahasiswa")
print ("---------------------------------------------------")

nama=input(  "Masukkan nama :")  
nim=input(  "Masukkan nim :")
jenis_kelamin=input("Masukkan jenis kelamin :")
tanggal_input=input("Masukkan tanggal input :")
matkul = input ("Masukkan matkul :")
absen = float (input ("Masukkan absen :"))
quiz = float (input ("Masukkan quiz :"))
Tugas = float (input ("Masukkan Tugas :"))
praktek = float (input ("Masukkan praktek :"))
UTS = float (input ("Masukkan UTS :"))
UAS = float (input ("Masukkan UAS :"))

NA=(absen*0.05)+(quiz*0.05)+(Tugas*0.1)+(praktek*0.2)+(UTS*0.25)+(UAS*0.35) 

print ("============ HASIL PERHITUNGAN =====================")

print("nama :",nama)
print("nim :", nim)
print("jenis_kelamin :",jenis_kelamin)
print("tanggal_input :", tanggal_input)
print("matkul :", matkul)
print("absen:", absen)
print("quiz :", quiz)
print("Tugas :", Tugas)
print("praktek :", praktek)
print("UTS :", UTS )
print("UAS :", UAS)
print("Nilai Akhir :", NA) 

if NA >= 80:
    print("Grade: A")
elif NA >= 77: 
    print("Grade: A-")  
elif NA >= 74 :
    print("Grade: B+")
elif NA >= 71 :
    print("Grade: B")
elif NA >= 68 :
    print("Grade: B-")
elif NA >= 64 :
    print("Grade: C+")
elif NA >=60 :
    print("Grade: C-")
elif NA >=50 :
    print("Grade: D")
elif NA <= 49 :
    print("Grade: E")

if NA >=60 :
    print("Keterangan : LULUS")
else:
    print("Keterangan : TIDAK LULUS")                     



