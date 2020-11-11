# BENDA
deskripsi = ("deskripsi baju")
baju = []

# String
model = input("model baju :")
print("model baju adalah:", model)
print("_bertype :", type(model))
baju.append(model)

# integer
ukuran = int(input("ukuran baju :"))
print("ukuran baju adalah :", ukuran)
print("_bertype :", type(ukuran))
baju.append(ukuran)

# float
harga = float(input("harga baju :"))
print("harga baju adalah :", harga)
print("_bertype :", type(harga))
baju.append(harga)
# string 
warna = input("warna baju :")
print("warna baju :", warna)
print("_bertype :", type(warna))
baju.append(warna)

# integer

jumlah = int(input("jumlah baju yang di miliki :"))
print("jumlah baju :", jumlah)
print("_bertype", type(jumlah))
baju.append(jumlah)

print("model baju",model, "dengan ukuran",ukuran, "harga baju",harga, "jumlah baju",jumlah,)

print(baju)