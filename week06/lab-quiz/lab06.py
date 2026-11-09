ana_brans = ("Yazılım", "Tasarım", "Pazarlama")

tum_ogrenciler = []

ogrenci_1 = [" Yasin ".strip(), [ana_brans[0]]]
ogrenci_2 = ["Seden ".strip(), [ana_brans[2], ana_brans[1]]]
ogrenci_3 = ["Beyza".strip(), [ana_brans[2], ana_brans[0]]]

tum_ogrenciler.append(ogrenci_1)
tum_ogrenciler.append(ogrenci_2)
tum_ogrenciler.append(ogrenci_3)

baskan_ogrenci = ["  Melikşah ".strip(), [ana_brans[0]]]
tum_ogrenciler.insert(0, baskan_ogrenci)

print(f"Toplam Kayıtlı Öğrenci Sayısı: {len(tum_ogrenciler)}")

for ogrenci_index in tum_ogrenciler:
    if ogrenci_index[0] == "Yasin":
        tum_ogrenciler.remove(ogrenci_index)
        break

cikan_ogrenci = tum_ogrenciler.pop()
print(f"Sistemden en son çıkan öğrenci: {cikan_ogrenci[0]}")

ogrenci_son = [" Burak Tan ".strip(), [ana_brans[1]]]
tum_ogrenciler.append(ogrenci_son)

print(sorted(tum_ogrenciler))
print(tum_ogrenciler)

tum_ogrenciler.sort()
print(tum_ogrenciler)