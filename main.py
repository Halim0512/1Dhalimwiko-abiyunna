# syarat nilai untuk lolos seleksi
SYARAT_NILAI = 420

print("================================================")

print("        SELAMAT DATANG DI SELEKSI SKD CPNS      ")
print("              SILAHKAN LENGKAPI DATA            ")

print("================================================")

NAMA = input("MASUKAN NAMA   : ")
TEMPAT_LAHIR = input("TEMPAT LAHIR   : ")
TANGGAL_LAHIR = str(input("TANGGAL LAHIR  : "))
ALAMAT = str(input("ALAMAT         : "))
print("    MASUKAN NILAI SELEKSI ANDA" )
TWK = int(input("NILAI TWK         : "))
TIU = int(input("NILAI TIU         : "))
TKP = int(input("NILAI TKP         : "))
print("                  ======= +    ")
SELEKSI = TWK+TIU+TKP
print("KESELURUHAN NILAI : ",SELEKSI)

PROSES_SELEKSI = int(input("MASUKAN KESELURUHAN NILAI : "))

if PROSES_SELEKSI>SYARAT_NILAI:
    print("=======================================")
    print(" SELAMAT ANDA LOLOS SELEKSI SKD CPNS   ")
    print("PERSIAPKAN DIRI UNTUK TAHAP BERIKUTNYA ")
    print("=======================================")

else:
    PROSES_SELEKSI<SELEKSI
    print("=======================")
    print("    ANDA TIDAK LOLOS   ")
    print("     TERUS BERJUANG    ")
    print("=======================")