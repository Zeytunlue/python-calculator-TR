print("""**********************
Hesap Makinesi Programi
Islemler:
1. Toplama Islemi
2. Cikarma Islemi
3. Carpma Islemi
4. Bölme Islemi
**********************""")
while True:
  a = int(input("Birinci sayi: "))
  b = int(input("Ikinci sayi: "))
  islem = input("Islemi giriniz: ")
  if islem == "1":
      print("{} ile {} sayilarinin toplami: {} dir.".format(a,b,a+b))
  elif islem == "2":
      print("{} ile {} sayilarinin farki: {} dir.".format(a,b,a-b))
  elif islem == "3":
      print("{} ile {} sayilarinin carpimi: {} dir.".format(a,b,a*b))
  elif islem == "4":
      print("{} ile {} sayilarinin bölümü: {} dir.".format(a, b, a/b))
  else:
      print("Gecersiz islem!")
  if input("Tekrar denemek ister misiniz?(evet/hayir): ").lower() != "evet":
      break
print("Gorusmek uzere!")

