# Input: Menanyakan apakah pelanggan memiliki kartu member
member = input("Apakah member ? (Ya/tidak): ").lower()  # Input 'ya' atau 'tidak', mengubah input menjadi lowercase untuk mempermudah pengecekan

# Input: Menanyakan total belanja
total_belanja = float(input("Masukkan total belanja: Rp "))

# Variabel untuk menyimpan diskon dan total yang harus dibayar
diskon = 0
diskon_persen = 0

# Logika untuk menentukan diskon berdasarkan kartu member dan total belanja
if member == "ya":  # Jika pelanggan memiliki kartu member
    if total_belanja > 500000:
        diskon_persen = 20
        diskon = total_belanja * diskon_persen / 100
    else:
        diskon_persen = 10
        diskon = total_belanja * diskon_persen / 100
else:  # Jika pelanggan tidak memiliki kartu member
    if total_belanja > 500000:
        diskon_persen = 5
        diskon = total_belanja * diskon_persen / 100
    else:
        diskon_persen = 0
        diskon = 0

# Menghitung total yang harus dibayar setelah diskon
bayar = total_belanja - diskon

# Output hasil perhitungan
print(f"Total belanja: Rp {total_belanja:,.0f}")
print(f"Diskon persen: {diskon_persen}%")
print(f"Diskon: Rp {diskon:,.0f}")
print(f"Bayar: Rp {bayar:,.0f}")