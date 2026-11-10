# nomor 1
def celcius_ke_fahreinheit(celcius):
    return (celcius * 9/5) +32

print(celcius_ke_fahreinheit(0))
print(celcius_ke_fahreinheit(100))

# nomor 2
def is_genap(angka):
    return angka % 2 == 0

print (is_genap(4))
print (is_genap(7))

# nomor 3
def nilai(angka):
    if angka >= 70:
        print("lulus")
    else:
        print("gagal")

nilai(80)  # lulus
nilai(60)  # gagal

# nomor 4
def bilangan(angka):
    for i in range(1,angka,2):
        if i < angka - 1:
            print(i, end=",")
        else:
            print(i)

bilangan(20)

    