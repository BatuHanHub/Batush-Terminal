class komutlar:
    def __init__(self, komutAdi, inputKomut):
        self.komutAdi = komutAdi
        self.inputKomut = inputKomut

### Komutlar ###

# Dosya ve Klasör
olsdsy = komutlar('Olustur Dosya','olşdsy')
sil = komutlar('Sil','sil')
oku = komutlar('Oku','oku')

olskls = komutlar('Oluştur Klasör','olşkls')
silkls = komutlar('Sil Klasör','silkls')

git = komutlar('Git','git')
nerde = komutlar('Nerdeyim','nerdeyim')
listele = komutlar('Listele','liste')

# Sistem 
cik = komutlar('Çık','çık')
temiz = komutlar('Temizle','temizle') 
calistir = komutlar('Çalıştır','çalıştır')
kapat = komutlar('Kapat','kapat')
bilgilendir = komutlar('Bilgilendir','bilgi')
yardim = komutlar('Yardım','yardım')
degis = komutlar('Değiş','!>')

# Ek komutlar
Ataturk = komutlar('Mustafa Kemal Atatürk','Atatürk')
tarih = komutlar('Tarih','tarih')
kalp = komutlar('<3','<kalp3')

# Python
python = komutlar('Python Başlatıcısı','python')
calistirPython = komutlar('Python Çalıştırıcısı','pyçalış')
