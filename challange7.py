num = int(input("Masukkan Angka 10-15 atau 20-25 atau 35-40: "))

while num >= 0:
    if  10 <= num <= 15 or 20 <= num <= 25 or 35 <= num <= 40:
        print("True")
        break
    else:
        num = int(input("Masukkan Angka 10-15 atau 20-25 atau 35-40: "))