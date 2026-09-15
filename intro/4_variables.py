name = "Wilfredo Alexander Sutanto"
age = 28
is_student = True

# name, age, is_student: adalah nama variabelnya
# =, adalah assignment value, value disebelah kanan di assign / masuk ke variabel yang ada disebelah kiri
# "Wilfredo Alexander Sutanto", 28, True, itu semua adalah value

# penamaan variable (naming rules)
user_name = "fredovz" # snake_case
userName = "fredovz" # boleh, camelcase, tidak sesuai standard python (PEP8)
age2 = 34
_api_key = "secret"

# penamaan variable (naming rules) yang salah
# 2age = 34
# user-name = "fredovz"
# user name = "fredovz"
# class = "Python"

# mengubah value dari suatu variabel
score = 0
print(score) # 0

score = 10
print(score) # 10

score = score + 5
print(score) # 15

# kesalahan umum
# lupa double quotes

# name = "Wilfredo"
# name = Wilfredo # Python mencari variabel dengan nama Wilfredo

# menggunakan variabel yang tidak ada (undefined)
# print(ipk) # error, karena variabel ipk belum ada
# ipk = 3.71

# Contoh yang benar
ipk = 3.71
print(ipk)

# bingung antara = dan == (double sama dengan)
age = 28 # assign value / menyimpan value kedalam variabel

if age == 28: # membandingkan nilai
    print("Rajin olahraga ya!")