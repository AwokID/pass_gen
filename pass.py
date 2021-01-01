# Seperti biasa import doeloe :v
import random, string, time, os, sys

# buat banner
os.system("cls" if os.name == "nt" else "clear")
print("""

[#] RANDOM PASSWORD GENERATOR [#]

""")

# Input panjang password
panjang_pass = int(input("Masukan panjang pass: "))

# Katakter-karakter pass yang akan digunakan huruf,angka,simbol
pass_karakter = string.ascii_letters + string.digits + string.punctuation

# Penampung panjang pass
password = []

# Menggunakan perulangan for untuk membuat pass dengan panjang yang di inginkan
for i in range(panjang_pass):
  # Menambahkan semua karakter yang berhasil diloop untuk ditampilkan menjadi pass yang utuh
  password.append(random.choice(pass_karakter))

# Menampilkan pass + menghilangkan tampilan awal yang masih berbentuk list
print(''.join(password))
