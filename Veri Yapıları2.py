# Veri yapılarıyla ürünlerin, kategorilerin ve stokların yönetimi

# Liste: Alışveriş sepetindeki ürünler (tekrar olabilir)
sepet = ["elma", "muz", "elma", "çilek", "muz", "portakal"]

# Tuple: Ürünlerin sabit fiyatları (değiştirilemez)
urun_fiyatlari = (
    ("elma", 3.5),
    ("muz", 4.0),
    ("çilek", 10.0),
    ("portakal", 5.0)
)

# Sözlük: Ürün fiyatlarına hızlı erişim için dönüştürme
fiyat_dict = dict(urun_fiyatlari)

# Küme: Sepetteki farklı ürünler (benzersiz)
farkli_urunler = set(sepet)

# Sepetteki ürünlerin adet sayısı
urun_adetleri = {}
for urun in sepet:
    urun_adetleri[urun] = urun_adetleri.get(urun, 0) + 1

print("Sepet:", sepet)
print("Farklı Ürünler:", farkli_urunler)
print("Ürün Adetleri:", urun_adetleri)
print("Ürün Fiyatları:", fiyat_dict)

# Toplam tutar hesaplama
toplam_tutar = 0
for urun, adet in urun_adetleri.items():
    fiyat = fiyat_dict.get(urun, 0)
    toplam_tutar += fiyat * adet

print("Toplam Tutar: {:.2f} TL".format(toplam_tutar))
