# Listeler, tuple, sözlük ve kümeler ile öğrenciler ve özellikleri üzerinde işlem yapma

# 1. Listeler: Öğrenci isimleri listesi (değiştirilebilir)
ogrenciler = ["Ali", "Ayşe", "Mehmet", "Zeynep"]

# Listeye ekleme
ogrenciler.append("Fatma")

# 2. Tuple: Değiştirilemez sınav tarihleri
sinav_tarihleri = ("2025-07-15", "2025-08-20", "2025-09-10")

# 3. Sözlük: Öğrenci ve notları
notlar = {
    "Ali": 85,
    "Ayşe": 92,
    "Mehmet": 78,
    "Zeynep": 88,
    "Fatma": 95
}

# 4. Küme: Katılan öğrenci isimleri (benzersiz, sırasız)
katilanlar = {"Ali", "Mehmet", "Fatma"}

# Küme yöntemleri
katilanlar.add("Ayşe")  # Yeni katılımcı ekle
katilanlar.discard("Mehmet")  # Katılımcı çıkar

# Çıktılar
print("Öğrenci Listesi:", ogrenciler)
print("Sınav Tarihleri:", sinav_tarihleri)
print("Notlar:", notlar)
print("Katılanlar:", katilanlar)

# Belirli öğrenci notu alma
print("Ayşe'nin Notu:", notlar.get("Ayşe"))

# Liste sıralama
ogrenciler.sort()
print("Sıralı Öğrenciler:", ogrenciler)
