class komutlar:
    def __init__(self, komutAdi, inputKomut, bilgi):
        self.komutAdi = komutAdi
        self.inputKomut = inputKomut
        self.bilgi = bilgi

    def bilgileriYazdir(self):
        print(self.bilgi)

### Komutlar ###

# Dosya ve Klasör
olsdsy = komutlar('Olustur Dosya','olşdsy','Bulunduğunuz dizine bir dosya oluşturur.\nKullanımı: olşdsy <dosya_adi.tür>   Örneğin: olşdsy merhaba.txt\n')
sil = komutlar('Sil','sil','Bulunduğunuz dizindeki istediğiniz dosyayı siler.\nKullanımı: sil <dosya_adi.tür>   Örneğin: sil merhaba.txt\n')
oku = komutlar('Oku','oku','Bulunduğunuz dizindeki istediğiniz dosyayı okur ve ekrana yazdırır.\nKullanımı: oku <dosya_adi.tür>   Örneğin: oku merhaba.txt\n')

olskls = komutlar('Oluştur Klasör','olşkls','Bulunduğunuz dizine bir klasör oluşturur.\nKullanımı: olşkls <klasor_adi>   Örneğin: olşkls oyunlar\n')
silkls = komutlar('Sil Klasör','silkls','Bulunduğunuz dizindeki istediğiniz klasörü siler.\nKullanımı: sil <klasor_adi>   Örneğin: sil System32\n')

git = komutlar('Git','git',
'Bulunduğunuz dizinden istediğiniz dizine gitmeyi sağlar.\nKullanımı: dizin değiştirmek için; git <dizin_adi>   Örneğin: git Masaüstü | bir alt dizine gitmek için; git <-\n')
nerde = komutlar('Nerdeyim','nerdeyim','Şu anki konumunuzu ekrana yazar.\n')
listele = komutlar('Listele','ls','Bulunduğunuz dizinin içindeki dosyaları ve klasörleri listeler.\n')
kopya = komutlar('Kopyala',"kpy","İstediğiniz dosya/klasörü bir dizine kopyalar.\nKullanımı: kpy <dosya_adi.turu/dizin_adi>,<hedef_dizin>   Örneğin: kpy merhaba.txt,System32\n")
tasi = komutlar('Taşı','taşı','İstediğiniz dosya/klasörü bir dizine taşır.\nKullanımı: taşı <dosya_adi.turu/dizin_adi>,<hedef_dizin>   Örneğin: taşı merhaba.txt,System32\n')
yeniAd = komutlar('Yeniden Adlandır','isim','Seçilen dosya/klasörün adını değiştirir.\nKullanımı: isim <dosya_adi.turu/dizin_adi>,<yeni_ad> Örneğin: isim birinci.txt,ikinci.txt\n')

# Sistem 
cik = komutlar('Çık','çık','Batush\'u kapatır.')
temiz = komutlar('Temizle','temizle','Terminal/Uçbirim/Konsole ekranınızı temizler.\n') 
calistir = komutlar('Çalıştır','başlat','Program çalıştırır.\nKullanımı: başlat <program_adi.turu>   Örneğin: başlat firefox\n')
kapat = komutlar('Kapat','kapat','Çalışan programları kapatır.\nKullanımı: kapat <program_adi.turu>   Örneğin: kapat firefox\n')
bilgilendir = komutlar('Bilgilendir','bilgi','Batush hakkında bilgi verir.\n')
yardim = komutlar('Yardım','yardım','Komutlar hakkında bilgi verir.\n')
degis = komutlar('Değiş','!>','Başka Konsole/Uçbirim/Terminal komutlarını kullanmanızı sağlar.\nKullanımı: !><komut>   Örneğin: !> cls\n')

# Ek komutlar
Ataturk = komutlar('Mustafa Kemal Atatürk','Atatürk','1881-193∞\n')
tarih = komutlar('Tarih','tarih','Şu anki tarihi ekrana yazdırır.\n')
bune = komutlar('Bu ne?','bune','Komutlar hakkında bilgi verir.\n')
kalp = komutlar('<3','<kalp3','<3')

# Python
python = komutlar('Python Başlatıcısı','python','Konsole/Uçbirim/Terminal Python açar.\n')
calistirPython = komutlar('Python Çalıştırıcısı','pyçalış','Python dosyalarını çalıştırır.\nKullanımı: pyçalış <dosya_adi.py>   Örneğin: pyçalış main.py\n')

tumKomutlar = [olsdsy, sil, oku, olskls, silkls, git, nerde, listele,
kopya, tasi, yeniAd, cik, temiz, calistir, kapat, bilgilendir, yardim, degis,
Ataturk, tarih, bune, kalp, python, calistirPython]
