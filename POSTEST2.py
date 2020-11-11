# KONVERSI SUHU

print("======================================================================")
print("=======================|Rahmiatul Mawaddah|===========================")
print("===========================|2009106076|===============================")
print("                           informatika B                              ")
print("======================================================================")

# input
ulang ="ya"
while (ulang =="ya") :
  celcius = float(input("masukkan suhu :"))
  farenheit = 9/5*celcius+32
  kelvin = 273+celcius
  reamur = (4/5)*celcius

  print("\n")
  print("celcius :", celcius)
  print("farenheit :", farenheit)
  print("kelvin :", kelvin)
  print("reamur :", reamur)

  ulang = input("masukan ulang suhu? y/t :")