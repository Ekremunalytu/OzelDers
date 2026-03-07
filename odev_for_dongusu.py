# ============================================================
#          PYTHON FOR DONGUSU - EV ODEVI
#          Hazirlayan: Ogretmeniniz
# ============================================================
#
#  Bu odevi bastan sona oku, her adimi anlamaya calis.
#  "GOREV" yazan yerleri kendin tamamla!
#  Calistirmak icin: python odev_for_dongusu.py
#
# ============================================================


# ************************************************************
# BOLUM 0: FOR DONGUSU NEDIR?
# ************************************************************
#
#  For dongusu = Bir seyleri TEKRAR TEKRAR yapmak
#
#  Gunluk hayattan ornek:
#
#     Siniftaki HER ogrenciye "Merhaba" de
#
#     +--------+    +--------+    +--------+    +--------+
#     | Ahmet  | -> | Ayse   | -> | Mehmet | -> | Zeynep |
#     +--------+    +--------+    +--------+    +--------+
#     Merhaba!      Merhaba!      Merhaba!      Merhaba!
#
#  Bunu Python'da soyle yazariz:
#
#     for ogrenci in ["Ahmet", "Ayse", "Mehmet", "Zeynep"]:
#         print("Merhaba", ogrenci)
#
#  Ne oluyor?
#     1. adim: ogrenci = "Ahmet"   -> Merhaba Ahmet
#     2. adim: ogrenci = "Ayse"    -> Merhaba Ayse
#     3. adim: ogrenci = "Mehmet"  -> Merhaba Mehmet
#     4. adim: ogrenci = "Zeynep"  -> Merhaba Zeynep
#
# ************************************************************


print("=" * 50)
print("   FOR DONGUSU EV ODEVI")
print("=" * 50)
print()


# ************************************************************
# BOLUM 1: BASIT LISTELERDE FOR
# ************************************************************
#
#  Liste nedir?
#
#     meyveler = ["elma", "armut", "muz"]
#
#     Bu listeyi bir kutu gibi dusun:
#
#     +-------+-------+-------+
#     | elma  | armut |  muz  |
#     +-------+-------+-------+
#       [0]     [1]     [2]       <-- sira numaralari (index)
#
# ************************************************************

print("--- BOLUM 1: Basit Listelerde For ---")
print()

# ORNEK 1: Meyveleri yazdirma
meyveler = ["elma", "armut", "muz", "cilek"]

print("Meyve listem:")
for meyve in meyveler:
    print("  -", meyve)
print()

# Yukardaki kod su sekilde calisiyor:
#
#   Tur 1:  meyve = "elma"   -->  print("  -", "elma")
#   Tur 2:  meyve = "armut"  -->  print("  -", "armut")
#   Tur 3:  meyve = "muz"    -->  print("  -", "muz")
#   Tur 4:  meyve = "cilek"  -->  print("  -", "cilek")
#
#   Liste bitti --> dongu biter


# ----------------------------------------------------------
# GOREV 1 (Kolay):
# Asagidaki listeyi for dongusu ile yazdir.
# Her hayvani "Hayvan: ..." seklinde yazdir.
# Beklenen cikti:
#   Hayvan: kedi
#   Hayvan: kopek
#   Hayvan: tavsan
#   Hayvan: papagan
# ----------------------------------------------------------

hayvanlar = ["kedi", "kopek", "tavsan", "papagan"]

print("GOREV 1 Cevabi:")
# BURAYA KOD YAZ:




print()


# ************************************************************
# BOLUM 2: RANGE() FONKSIYONU
# ************************************************************
#
#  range() = Sayi listesi olusturur
#
#  range(5) demek:  0, 1, 2, 3, 4   (5 dahil DEGIL!)
#
#     Bunu soyle dusun:
#
#     Baslangic: 0
#     |
#     v
#     0 --> 1 --> 2 --> 3 --> 4 --> DUR! (5'e gelince dur)
#
#
#  range(1, 6) demek:  1, 2, 3, 4, 5   (1'den basla, 6'da dur)
#
#     Baslangic: 1          Bitis: 6 (dahil degil)
#     |                     |
#     v                     v
#     1 --> 2 --> 3 --> 4 --> 5 --> DUR!
#
# ************************************************************

print("--- BOLUM 2: range() Fonksiyonu ---")
print()

# ORNEK 2: 1'den 5'e kadar sayilari yazdirma
print("1'den 5'e kadar sayilar:")
for sayi in range(1, 6):
    print("  ", sayi)
print()

# ORNEK 3: 0'dan 4'e kadar
print("range(5) sonucu:")
for sayi in range(5):
    print("  ", sayi)
print()


# ----------------------------------------------------------
# GOREV 2 (Kolay):
# 1'den 10'a kadar sayilari yazdir.
# Beklenen cikti:
#   1
#   2
#   3
#   ...
#   10
#
# IPUCU: range(1, 11) kullan (11 dahil degil, 10'da durur)
# ----------------------------------------------------------

print("GOREV 2 Cevabi:")
# BURAYA KOD YAZ:




print()


# ----------------------------------------------------------
# GOREV 3 (Kolay):
# 1'den 10'a kadar sayilarin KARESINI yazdir.
# Kare = sayi * sayi
# Beklenen cikti:
#   1 in karesi = 1
#   2 nin karesi = 4
#   3 un karesi = 9
#   ...
#   10 un karesi = 100
#
# IPUCU: print(sayi, "in karesi =", sayi * sayi)
# ----------------------------------------------------------

print("GOREV 3 Cevabi:")
# BURAYA KOD YAZ:




print()


# ************************************************************
# BOLUM 3: FOR ICERISINDE IF KULLANMA
# ************************************************************
#
#  For ve if birlikte calisabilir!
#
#  Ornek: Sadece cift sayilari yazdir
#
#     for sayi in [1, 2, 3, 4, 5, 6]:
#         if sayi % 2 == 0:       <-- cift mi?
#             print(sayi)
#
#  Gorsel:
#
#     1 --> Tek mi? EVET  --> ATLA
#     2 --> Tek mi? HAYIR --> YAZDIR: 2
#     3 --> Tek mi? EVET  --> ATLA
#     4 --> Tek mi? HAYIR --> YAZDIR: 4
#     5 --> Tek mi? EVET  --> ATLA
#     6 --> Tek mi? HAYIR --> YAZDIR: 6
#
#  % (mod) operatoru:
#     4 % 2 = 0  (4, 2'ye tam bolunur, kalan 0)
#     5 % 2 = 1  (5, 2'ye tam bolunmez, kalan 1)
#
# ************************************************************

print("--- BOLUM 3: For + If ---")
print()

# ORNEK 4: Sadece cift sayilari yazdirma
print("1-10 arasi cift sayilar:")
for sayi in range(1, 11):
    if sayi % 2 == 0:
        print("  ", sayi, "(cift)")
print()


# ----------------------------------------------------------
# GOREV 4 (Orta):
# 1'den 20'ye kadar olan sayilardan sadece
# 3'e bolunebilenleri yazdir.
# Beklenen cikti:
#   3
#   6
#   9
#   12
#   15
#   18
#
# IPUCU: sayi % 3 == 0 kontrolu yap
# ----------------------------------------------------------

print("GOREV 4 Cevabi:")
# BURAYA KOD YAZ:




print()


# ----------------------------------------------------------
# GOREV 5 (Orta):
# Asagidaki not listesinden 50'nin ustundeki notlari
# "Gecti" olarak, 50 ve altindakileri "Kaldi" olarak yazdir.
# Beklenen cikti:
#   45 --> Kaldi
#   78 --> Gecti
#   32 --> Kaldi
#   90 --> Gecti
#   55 --> Gecti
#   48 --> Kaldi
# ----------------------------------------------------------

notlar = [45, 78, 32, 90, 55, 48]

print("GOREV 5 Cevabi:")
# BURAYA KOD YAZ:




print()


# ************************************************************
# BOLUM 4: FOR ILE TOPLAMA (AKUMULATOR DESENI)
# ************************************************************
#
#  Bir degisken ile toplam tutabiliriz:
#
#     toplam = 0                 <-- baslangic
#     for sayi in [3, 5, 2]:
#         toplam = toplam + sayi
#
#  Gorsel:
#
#     toplam = 0
#     |
#     +-- sayi = 3 --> toplam = 0 + 3 = 3
#     |
#     +-- sayi = 5 --> toplam = 3 + 5 = 8
#     |
#     +-- sayi = 2 --> toplam = 8 + 2 = 10
#     |
#     Sonuc: toplam = 10
#
# ************************************************************

print("--- BOLUM 4: For ile Toplama ---")
print()

# ORNEK 5: Liste elemanlarini toplama
sayilar = [10, 20, 30, 40]
toplam = 0

for sayi in sayilar:
    toplam = toplam + sayi
    print(f"  {sayi} eklendi, toplam simdi: {toplam}")

print(f"  Genel toplam: {toplam}")
print()


# ----------------------------------------------------------
# GOREV 6 (Orta):
# 1'den 100'e kadar tum sayilarin toplamini hesapla.
# Sonucu yazdir.
# Dogru cevap: 5050
#
# IPUCU:
#   toplam = 0
#   for ... in range(...):
#       toplam = toplam + ...
# ----------------------------------------------------------

print("GOREV 6 Cevabi:")
# BURAYA KOD YAZ:




print()


# ************************************************************
# BOLUM 5: STRING (YAZI) UZERINDE FOR
# ************************************************************
#
#  String de aslinda bir listedir! Her harfi gezebiliriz.
#
#     "PYTHON"
#     +---+---+---+---+---+---+
#     | P | Y | T | H | O | N |
#     +---+---+---+---+---+---+
#      [0] [1] [2] [3] [4] [5]
#
#     for harf in "PYTHON":
#         print(harf)
#
#     P
#     Y
#     T
#     H
#     O
#     N
#
# ************************************************************

print("--- BOLUM 5: String Uzerinde For ---")
print()

# ORNEK 6: Bir kelimeyi harf harf yazdirma
kelime = "MERHABA"
print(f"'{kelime}' kelimesinin harfleri:")
for harf in kelime:
    print("  ", harf)
print()


# ----------------------------------------------------------
# GOREV 7 (Orta):
# Kullanicidan bir kelime al ve icinde kac tane sesli harf
# oldugunu say.
# Sesli harfler: a, e, i, o, u
# Ornek: "araba" -> 3 sesli harf var
#
# IPUCU:
#   sayac = 0
#   for harf in kelime:
#       if harf in "aeiou":
#           sayac = sayac + 1
# ----------------------------------------------------------

print("GOREV 7 Cevabi:")
kelime = "programlama"  # bunu degistirebilirsin
# BURAYA KOD YAZ:




print()


# ************************************************************
# BOLUM 6: IC ICE FOR (BONUS - ZOR)
# ************************************************************
#
#  Bir for dongusunun icine baska bir for koyabiliriz.
#
#  Ornek: Carpim tablosu
#
#     for i in range(1, 4):        <-- DIS dongu
#         for j in range(1, 4):    <-- IC dongu
#             print(i, "x", j, "=", i*j)
#
#  Gorsel:
#
#     i=1:  j=1 -> 1x1=1   j=2 -> 1x2=2   j=3 -> 1x3=3
#     i=2:  j=1 -> 2x1=2   j=2 -> 2x2=4   j=3 -> 2x3=6
#     i=3:  j=1 -> 3x1=3   j=2 -> 3x2=6   j=3 -> 3x3=9
#
#     Dis dongunun HER turunda, ic dongu BASTAN BASLAR!
#
# ************************************************************

print("--- BOLUM 6: Ic Ice For (Bonus) ---")
print()

# ORNEK 7: Basit carpim tablosu (1-3)
print("Carpim Tablosu (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i*j}")
    print()  # her satir arasinda bosluk


# ----------------------------------------------------------
# GOREV 8 (Zor - Bonus):
# Asagidaki gibi bir yildiz ucgeni ciz:
#
#   *
#   **
#   ***
#   ****
#   *****
#
# IPUCU: print("*" * sayi) kullanabilirsin
#         range(1, 6) ile 1'den 5'e kadar git
# ----------------------------------------------------------

print("GOREV 8 Cevabi:")
# BURAYA KOD YAZ:




print()


# ----------------------------------------------------------
# GOREV 9 (Zor - Bonus):
# 1'den 5'e kadar carpim tablosu yap.
# Beklenen cikti:
#   1 x 1 = 1
#   1 x 2 = 2
#   ...
#   5 x 5 = 25
# ----------------------------------------------------------

print("GOREV 9 Cevabi:")
# BURAYA KOD YAZ:




print()


# ************************************************************
# BOLUM 7: EGLENCELI GOREV
# ************************************************************

# ----------------------------------------------------------
# GOREV 10 (Eglenceli):
# Bir geri sayim programi yaz!
# 10'dan 1'e kadar geri say, sonra "KALKIS!" yazdir.
# Beklenen cikti:
#   10
#   9
#   8
#   ...
#   1
#   KALKIS!
#
# IPUCU: range(10, 0, -1) kullan
#        range(baslangic, bitis, adim)
#        adim = -1 olunca geriye sayar
# ----------------------------------------------------------

print("GOREV 10 Cevabi:")
# BURAYA KOD YAZ:




print()


# ************************************************************
#  ODEV BITTI!
# ************************************************************
#
#  OZET - FOR DONGUSU KALIPLARI:
#
#  1. Liste gezme:
#     for eleman in liste:
#         # eleman ile bir sey yap
#
#  2. Sayi sayma:
#     for i in range(baslangic, bitis):
#         # i ile bir sey yap
#
#  3. For + If:
#     for eleman in liste:
#         if kosul:
#             # kosul dogru ise yap
#
#  4. For ile toplama:
#     toplam = 0
#     for eleman in liste:
#         toplam = toplam + eleman
#
#  5. String gezme:
#     for harf in kelime:
#         # harf ile bir sey yap
#
#  6. Ic ice for:
#     for i in range(...):
#         for j in range(...):
#             # i ve j ile bir sey yap
#
# ************************************************************

print("=" * 50)
print("  Tebrikler, odevi tamamladin!")
print("  Takildgin yerleri not al,")
print("  bir sonraki derste soralim.")
print("=" * 50)
