

# Tugas Pemograman Berorientasi Objek - Sesi 3
# Nama : MAHMUD S LAOPO
# Nim  : 20210801203

print ("---------------------------------------------------")
print ("\tMENGHITUNG NILAI AKHIR MAHASISWA")
print ("---------------------------------------------------")


nama=input("Masukkan Nama\t\t :")  
nim=input("Masukkan Nim\t\t :")
jenis_kelamin=input("Masukkan jenis Kelamin\t :")
tanggal_input=input("Masukkan Tanggal Input\t :")
matkul = input ("Masukkan Matkul\t\t :")
Kehadiran = float (input ("Masukkan Kehadiran\t :"))
Quiz = float (input ("Masukkan Quiz\t\t :"))
Tugas = float (input ("Masukkan Tugas\t\t :"))
Praktek = float (input ("Masukkan Praktek\t :"))
UTS = float (input ("Masukkan nilai UTS\t :"))
UAS = float (input ("Masukkan nilai UAS\t :"))

NA=(Kehadiran*0.05)+(Quiz*0.05)+(Tugas*0.1)+(Praktek*0.2)+(UTS*0.25)+(UAS*0.35) 

print ("\n\n============ HASIL PERHITUNGAN =====================\n")

print("Nama\t\t: ", nama)
print("Nim\t\t: ", nim)
print("Jenis Kelamin\t: ",jenis_kelamin)
print("Tanggal Input\t:", tanggal_input)
print("Matkul\t\t:", matkul)
print("Kehadiran\t:", Kehadiran)
print("Quiz\t\t:", Quiz)
print("Tugas\t\t:", Tugas)
print("Praktek\t\t:", Praktek)
print("UTS\t\t:", UTS )
print("UAS\t\t:", UAS)
print("Nilai Akhir\t:", NA) 

if NA >= 80 and NA <=100 :
    print("Grade: A")
elif NA >= 77 and NA <= 77.9: 
    print("Grade: A-")  
elif NA >= 74 and NA <= 76.9 :
    print("Grade: B+")
elif NA >= 71 and NA <= 73.9:
    print("Grade: B")
elif NA >= 68 and NA <= 70.9 :
    print("Grade: B-")
elif NA >= 64 and NA <= 67.9 :
    print("Grade: C+")
elif NA >=60 and NA <= 63.9 :
    print("Grade: C-")
elif NA >=50 and NA <= 59 :
    print("Grade: D")
elif NA <= 49 and NA >= 0 :
    print("Grade: E")

if NA >=60 :
    print("Keterangan : LULUS")
else:
    print("Keterangan : TIDAK LULUS")                     



