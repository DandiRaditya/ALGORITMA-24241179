# program untuk menentukan bonus total belanja

# input total belanja
total_belanja = int(input("Masukan total belanja anda(dalam Rp): "))

# logika menentukan bonus
if total_belanja >= 5000000:
    bonus = "mouse dan keyboard"
else:
    bonus = "gantungan kunci"

# output bonus yang di terima 
print(f"total belanja anda adalah Rp.{total_belanja:.2f}.Anda mendapatkan bonus: {bonus}.")