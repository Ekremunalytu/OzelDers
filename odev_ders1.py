

print("=" * 50)
print("     DERS 1 - EV ODEVI BASLADI")
print("=" * 50)
print()


# ************************************************************
# BOLUM 1: PRINT VE DEGISKENLER
# ************************************************************
#
#  print() --> Ekrana yazi yazdirir
#  Degisken --> Bir kutunun icine deger koyma
#
#     +----------+     +--------+     +---------+
#     |  isim    |     |  yas   |     |  boy    |
#     | -------- |     | ------ |     | ------- |
#     | "Ahmet"  |     |   17   |     |  1.75   |
#     +----------+     +--------+     +---------+
#       (str)           (int)          (float)
#
# ************************************************************

print("--- BOLUM 1: Print ve Degiskenler ---")
print()

# ORNEK:
okul = "Nuri Demirag MTAL"
sinif = "11/D"
ogrenci_sayisi = 25
print(f"Okul: {okul}")
print(f"Sinif: {sinif}, Ogrenci sayisi: {ogrenci_sayisi}")
print()


# ----------------------------------------------------------
# GOREV 1 (Kolay):
# Kendini tanitan degiskenler olustur ve ekrana yazdir.
# Asagidaki degiskenleri doldur ve f-string ile yazdir.
#
# Beklenen cikti (ornek):
#   Benim adim Efe, 17 yasindayim.
#   Boyum 1.72 metre, hobim futbol.
# ----------------------------------------------------------

ad = ""          # kendi adini yaz
yas = 0          # kendi yasini yaz
boy = 0.0        # kendi boyunu yaz (ornek: 1.72)
hobi = ""        # bir hobini yaz

print("GOREV 1 Cevabi:")
# BURAYA KOD YAZ (f-string kullan):



print()


# ----------------------------------------------------------
# GOREV 2 (Kolay):
# Asagidaki degiskenlerin tiplerini tahmin et,
# sonra type() ile kontrol et.
#
# Beklenen cikti:
#   a'nin tipi: <class 'str'>
#   b'nin tipi: <class 'int'>
#   c'nin tipi: <class 'float'>
#   d'nin tipi: <class 'bool'>
# ----------------------------------------------------------

a = "Merhaba"
b = 42
c = 3.14
d = True

print("GOREV 2 Cevabi:")
# BURAYA KOD YAZ (her biri icin type() kullan):



print()


# ************************************************************
# BOLUM 2: MATEMATIK ISLEMLERI
# ************************************************************
#
#  Python bir hesap makinesi gibi calisir:
#
#  +   Toplama       10 + 3  = 13
#  -   Cikarma       10 - 3  = 7
#  *   Carpma        10 * 3  = 30
#  /   Bolme         10 / 3  = 3.33...
#  //  Tam bolme     10 // 3 = 3
#  %   Kalan (mod)   10 % 3  = 1
#  **  Us alma       10 ** 3 = 1000
#
# ************************************************************

print("--- BOLUM 2: Matematik Islemleri ---")
print()

# ORNEK:
fiyat = 150
indirim_yuzde = 20
indirim_tutari = fiyat * indirim_yuzde / 100
son_fiyat = fiyat - indirim_tutari
print(f"Fiyat: {fiyat} TL")
print(f"%{indirim_yuzde} indirimle: {son_fiyat} TL")
print()


# ----------------------------------------------------------
# GOREV 3 (Kolay):
# Bir ogrencinin 3 sinav notu var: 75, 85, 60
# Ortalamasini hesapla ve yazdir.
#
# Beklenen cikti:
#   Not 1: 75
#   Not 2: 85
#   Not 3: 60
#   Ortalama: 73.33333333333333
# ----------------------------------------------------------

sinav1 = 75
sinav2 = 85
sinav3 = 60

print("GOREV 3 Cevabi:")
# BURAYA KOD YAZ:



print()


# ----------------------------------------------------------
# GOREV 4 (Orta):
# Bir isci saatte 85 TL kazaniyor.
# Haftada 45 saat calisiyor.
# Ayda 4 hafta calisiyor.
# Aylik maasini hesapla.
# Maasinin %15'i vergi olarak kesiliyor.
# Ele gecen maasi hesapla ve yazdir.
#
# Beklenen cikti:
#   Brut maas: 15300 TL
#   Vergi: 2295.0 TL
#   Net maas: 13005.0 TL
# ----------------------------------------------------------

saat_ucreti = 85
haftalik_saat = 45
hafta_sayisi = 4
vergi_orani = 15

print("GOREV 4 Cevabi:")
# BURAYA KOD YAZ:



print()


# ************************************************************
# BOLUM 3: IF / ELIF / ELSE
# ************************************************************
#
#  Bilgisayara "KOSUL'a gore karar ver" diyoruz:
#
#     Soru: Not 50'den buyuk mu?
#           |
#       +---+---+
#       |       |
#     EVET    HAYIR
#       |       |
#    Gecti    Kaldi
#
#  Yazilisi:
#     if not >= 50:
#         print("Gecti")
#     else:
#         print("Kaldi")
#
#  DIKKAT: if'ten sonra 4 BOSLUK (girinti) SART!
#
# ************************************************************

print("--- BOLUM 3: If / Elif / Else ---")
print()

# ORNEK:
sicaklik = 35
if sicaklik >= 35:
    print(f"{sicaklik} derece - Cok sicak! Disari cikma.")
elif sicaklik >= 25:
    print(f"{sicaklik} derece - Guzel hava.")
elif sicaklik >= 15:
    print(f"{sicaklik} derece - Serin, mont al.")
else:
    print(f"{sicaklik} derece - Soguk! Kalin giyin.")
print()


# ----------------------------------------------------------
# GOREV 5 (Kolay):
# not_ortalamasi degiskenine bir sayi ata.
# Asagidaki tabloya gore harf notunu yazdir:
#
#   90-100 --> AA
#   80-89  --> BA
#   70-79  --> BB
#   60-69  --> CB
#   50-59  --> CC
#   0-49   --> FF (Kaldi)
#
# Beklenen cikti (ornek, 72 icin):
#   Not: 72 --> Harf notu: BB
# ----------------------------------------------------------

not_ortalamasi = 72

print("GOREV 5 Cevabi:")
# BURAYA KOD YAZ (if/elif/else kullan):



print()


# ----------------------------------------------------------
# GOREV 6 (Orta):
# Kullanicinin yasina gore bilet fiyatini belirle:
#   0-6 yas:   Ucretsiz
#   7-12 yas:  Cocuk bileti - 30 TL
#   13-17 yas: Ogrenci bileti - 50 TL
#   18-64 yas: Tam bilet - 100 TL
#   65+ yas:   Yasli indirimi - 40 TL
#
# Beklenen cikti (ornek, 15 icin):
#   Yas: 15 --> Ogrenci bileti - 50 TL
# ----------------------------------------------------------

yolcu_yasi = 15

print("GOREV 6 Cevabi:")
# BURAYA KOD YAZ:



print()


# ----------------------------------------------------------
# GOREV 7 (Orta):
# Bir market kasasinda 3 urun var.
# Toplam fiyata gore indirim uygula:
#   200 TL ustu --> %20 indirim
#   100-200 TL  --> %10 indirim
#   100 TL alti --> indirim yok
# Son fiyati yazdir.
#
# Beklenen cikti:
#   Urun 1: 75 TL
#   Urun 2: 120 TL
#   Urun 3: 45 TL
#   Ara toplam: 240 TL
#   Indirim: %20 = 48.0 TL
#   Odenecek tutar: 192.0 TL
# ----------------------------------------------------------

urun1 = 75
urun2 = 120
urun3 = 45

print("GOREV 7 Cevabi:")
# BURAYA KOD YAZ:



print()


# ************************************************************
# BOLUM 4: LISTELER
# ************************************************************
#
#  Liste = Sirali cekmece, her gozun bir numarasi var
#
#     notlar = [80, 55, 90, 70]
#
#     +----+----+----+----+
#     | 80 | 55 | 90 | 70 |
#     +----+----+----+----+
#      [0]  [1]  [2]  [3]    <-- index (0'dan baslar!)
#
#  Onemli komutlar:
#     liste.append(deger)  --> Sona ekle
#     liste.remove(deger)  --> Degeri cikar
#     len(liste)           --> Eleman sayisi
#     liste[0]             --> Ilk eleman
#     liste[-1]            --> Son eleman
#
# ************************************************************

print("--- BOLUM 4: Listeler ---")
print()

# ORNEK:
renkler = ["kirmizi", "mavi", "yesil"]
print("Liste:", renkler)
print("Ilk renk:", renkler[0])
print("Son renk:", renkler[-1])

renkler.append("sari")
print("Sari eklendi:", renkler)
print("Eleman sayisi:", len(renkler))
print()


# ----------------------------------------------------------
# GOREV 8 (Kolay):
# Asagidaki listeyi kullanarak istenen islemleri yap.
#
# Beklenen cikti:
#   Tum liste: [10, 20, 30, 40, 50]
#   Ilk eleman: 10
#   Ucuncu eleman: 30
#   Son eleman: 50
#   Eleman sayisi: 5
#   25 eklendi: [10, 20, 30, 40, 50, 25]
#   20 cikarildi: [10, 30, 40, 50, 25]
# ----------------------------------------------------------

sayilar = [10, 20, 30, 40, 50]

print("GOREV 8 Cevabi:")
# BURAYA KOD YAZ:



print()


# ----------------------------------------------------------
# GOREV 9 (Orta):
# Bir sinifta 5 ogrencinin notu asagidaki listede.
# Listeden index kullanarak 3. ogrencinin notunu yazdir.
# Listeye yeni bir not ekle (append).
# En dusuk notu cikar (remove).
# Her islemden sonra listeyi yazdir.
#
# Beklenen cikti:
#   Notlar: [70, 85, 55, 92, 68]
#   3. ogrencinin notu: 55
#   Yeni not eklendi: [70, 85, 55, 92, 68, 78]
#   En dusuk not cikarildi: [70, 85, 92, 68, 78]
#   Kalan ogrenci sayisi: 5
# ----------------------------------------------------------

notlar = [70, 85, 55, 92, 68]

print("GOREV 9 Cevabi:")
# BURAYA KOD YAZ:



print()


# ************************************************************
# BOLUM 5: FONKSIYONLAR
# ************************************************************
#
#  Fonksiyon = Bir makine
#  Girdi alir --> Islem yapar --> Cikti verir
#
#     Girdi          Makine           Cikti
#  +--------+    +------------+    +--------+
#  |  3, 5  | -->|  topla()   |--> |   8    |
#  +--------+    +------------+    +--------+
#
#  Yazilisi:
#     def fonksiyon_adi(parametre1, parametre2):
#         # islem yap
#         return sonuc
#
# ************************************************************

print("--- BOLUM 5: Fonksiyonlar ---")
print()

# ORNEK:
def selamla(isim):
    return f"Merhaba {isim}, nasilsin?"

print(selamla("Efe"))
print(selamla("Yusuf"))
print()


# ----------------------------------------------------------
# GOREV 10 (Kolay):
# Iki sayi alan ve buyuk olani donduren bir fonksiyon yaz.
#
# Beklenen cikti:
#   buyuk_bul(10, 20) = 20
#   buyuk_bul(55, 33) = 55
#   buyuk_bul(7, 7) = 7
# ----------------------------------------------------------

print("GOREV 10 Cevabi:")
# BURAYA FONKSIYONU YAZ:
# def buyuk_bul(a, b):
#     ...


# Asagidaki satirlari fonksiyonu yazdiktan sonra ac (# isaretini kaldir):
# print(f"buyuk_bul(10, 20) = {buyuk_bul(10, 20)}")
# print(f"buyuk_bul(55, 33) = {buyuk_bul(55, 33)}")
# print(f"buyuk_bul(7, 7) = {buyuk_bul(7, 7)}")

print()


# ----------------------------------------------------------
# GOREV 11 (Orta):
# 3 sinav notu alan ve harf notu donduren fonksiyon yaz.
# Fonksiyon:
#   1. 3 notu parametre olarak alsin
#   2. Ortalamayi hesaplasin
#   3. Harf notunu belirlesin (Gorev 5'teki tabloyu kullan)
#   4. Harf notunu dondursun
#
# Beklenen cikti:
#   harf_notu(80, 90, 70) = BB
#   harf_notu(90, 95, 88) = AA
#   harf_notu(40, 35, 50) = FF
# ----------------------------------------------------------

print("GOREV 11 Cevabi:")
# BURAYA FONKSIYONU YAZ:
# def harf_notu(not1, not2, not3):
#     ...


# Asagidaki satirlari fonksiyonu yazdiktan sonra ac:
# print(f"harf_notu(80, 90, 70) = {harf_notu(80, 90, 70)}")
# print(f"harf_notu(90, 95, 88) = {harf_notu(90, 95, 88)}")
# print(f"harf_notu(40, 35, 50) = {harf_notu(40, 35, 50)}")

print()


# ----------------------------------------------------------
# GOREV 12 (Zor - Bonus):
# Basit bir hesap makinesi fonksiyonu yaz.
# 3 parametre alsin: sayi1, sayi2, islem
# islem: "topla", "cikar", "carp", "bol"
#
# Beklenen cikti:
#   hesapla(10, 5, "topla") = 15
#   hesapla(10, 5, "cikar") = 5
#   hesapla(10, 5, "carp") = 50
#   hesapla(10, 5, "bol") = 2.0
# ----------------------------------------------------------

print("GOREV 12 Cevabi:")
# BURAYA FONKSIYONU YAZ:
# def hesapla(sayi1, sayi2, islem):
#     ...


# Asagidaki satirlari fonksiyonu yazdiktan sonra ac:
# print(f'hesapla(10, 5, "topla") = {hesapla(10, 5, "topla")}')
# print(f'hesapla(10, 5, "cikar") = {hesapla(10, 5, "cikar")}')
# print(f'hesapla(10, 5, "carp") = {hesapla(10, 5, "carp")}')
# print(f'hesapla(10, 5, "bol") = {hesapla(10, 5, "bol")}')

print()


# ************************************************************
#  ODEV BITTI!
# ************************************************************
#
#  HATIRLATMA - OGRENDIGIN KONULAR:
#
#  1. print()      --> Ekrana yazdirma
#  2. Degiskenler  --> Deger saklama (str, int, float, bool)
#  3. Matematik    --> +, -, *, /, //, %, **
#  4. if/elif/else --> Kosula gore karar verme
#  5. Listeler     --> Birden fazla veriyi saklama
#  6. Fonksiyonlar --> Tekrar kullanilabilir kod bloklari
#
#  Takildgin yerleri not al, bir sonraki derste soralim!
#
# ************************************************************

print("=" * 50)
print("  Tebrikler, odevi bitirdin!")
print("  Takildgin yerleri not al,")
print("  bir sonraki derste soralim.")
print("=" * 50)
