# mengenal String
# kumpulan karakter

data = "ini adalah string" # 21 karakter
print(data)
print(type (data))

# 1. cara membuat string
"""
1. dengan menggunakan single qoute '...'
2. dengan menggunakan double qoute "..."
"""

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print("ini hari jum'at")
print("nama saya ma'ruf")

# 2. menggunakan tanda \

# Membuat tandsa ' menjadi string
print('mari solat jum\'at')

print('C:\\user\\adam')

# tab (\t)
print("ronaldo\t\tmessi")
print("MU\t\tjuara")

# backpace (\b)
print("MU\bjuara")

# newline (\n)
print("baris pertama.\nbaris kedua.") # LF -> Line feed
print("baris pertama.\rbaris kedua.") # CRLF -> Line feed carige return

# raw string
print(r'C:\user\adam')