nilai = float(input("Masukkan nilai: "))  # Memasukkan nilai dalam bentuk angka (misalnya 82,5)

if nilai > 90:
    grade = "A"
elif 81 <= nilai <= 90:
    grade = "A-"
elif 75 <= nilai <= 80:
    grade = "B+"
elif 70 <= nilai <= 74:
    grade = "B"
elif 65 <= nilai <= 69:
    grade = "C+"
elif 60 <= nilai <= 64:
    grade = "C"
elif 55 <= nilai <= 59:
    grade = "D"
else:  # Nilai < 55
    grade = "E"

print(f"Grade untuk nilai {nilai} adalah{grade}.")