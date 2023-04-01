# Küütüphaneler
from colorama import * 
import datetime, time # Zamanla alakalı
import os, sys, platform # Sistemle alakalı

isletimSistemiTuru = os.name # kullanıcının kullandığı işletim sisteminin çekirdeği
isletimSistemiAdi = platform.system() # kullanıcının kullandığı işletim sisteminin adı 

### DOSYA VE KLASÖR İŞLEMLERİ ###

# Dosya işleri
def islev_olustur_dosya(dsyAdi):
    with open(f'{dsyAdi}','w',encoding='utf8') as dosya:
            dosya.close()

def islev_dosya_sil(dsySil):
    os.remove(dsySil)

def islev_dosyayi_oku(dsyAdi):
    with open(f'{dsyAdi}','r',encoding='utf8') as dosya:
        print('===Okudum===')
        for satir in dosya.readlines():
            print(satir)
        print('============\n')
        
# Klasör işleri    
def islev_olustur_klasor(klsAdi):
    os.mkdir(klsAdi)

def islev_sil_klasor(klsSil):
    os.rmdir(klsSil)

# Yol işleri
def islev_git(yol):
    if yol in os.listdir():
        os.chdir(yol)
        
    elif yol == '--':
        os.chdir('..')
             
    else:
        print('Hata <02> : Böyle bir dizin yok')

def islev_nerdeyim():
    print(os.getcwd())

def islev_liste():
    for ls in os.listdir():
        print(ls)

### SİSTEM KOMUTLARI ###

def islev_cik():
    print(Style.RESET_ALL)
    sys.exit()
    
def islev_temizle():
    if isletimSistemiTuru == 'nt':
        os.system('cls')
    else:
        os.system('clear')
           
def islev_calistir(program):
    if isletimSistemiTuru == 'nt':
        os.system(f"start {program}")
    else:
        os.system(program)

def islev_kapat(program):
    if isletimSistemiTuru == 'nt':
        os.system(f'taskkill /f /im "{program}"')
    else:
        os.system(f'killall {program}')    

def islev_bilgi():
    print("""Batush(Batuhan'ın Bash'i) Beta 5.0\n
BatuHanHub tarafından Python diliyle yazılmıştır. Sadece eğlenmek ve Python bilgimi sınamak için yazılmıştır.
GPL 3.0 lisansı ile dağıtılmaktadır. Telif hakkı (c) BatuHanHub

Yardım istiyorsanız `yardım` komutunu kullanabilirsiniz :)

Github: https://github.com/BatuHanHub
Bloğum: https://tatliyazilimci.blogspot.com/ \n""")
    
def islev_yardim():
    print("""  BATUSH KOMUTLARI

UYARI!: KOMUTLARINIZI KÜÇÜK HARFLERLE YAZINIZ. (Atatürk hariç) 

# DOSYA VE KLASÖR İŞLEMLERİ

olşdsy [dosya_adi.uzantisi] : dosya oluşturursunuz 
sil [dosya_adi.uzantisi] :  dosya siler 
oku [dosya_adi.uzantisi] : dosyayı okur

olşkls [klasor_adi]: klasör oluşturursunuz 
silkls [klasor_adi]: klasör siler 

git [yol_adi] : konumunuzu değiştirir (geri gitmek için `git --` yazmalısınız) 
nerdeyim      : şu anki konumunuzu gösterir 
liste         : konumunuzdaki dosyaları gösterir 

# SİSTEM KOMUTLARI
çık       : terminalden çıkarsınız
temizle   : terminali temizler
çalıştır [program_adi]: program çalıştırır
kapat [dosya_adi.uzantisi] : program kapatır
bilgi     : Batush hakkında bilgi verir
yardım    : terminal kodlarını ve işlevlerini gösterir

# PYTHON
python    : Python'u açar
pyçalış [dosya_adi.py] : Python dosyasını çalıştırır

# EK KOMUTLAR
Atatürk   : Ekranı temizler ve 2 dakika saygı duruşu için yazı yazamazsınız    
tarih     : zaman ve tarihi gösterir
bukelemun : yazı rengi değiştirir

""")
    
### EK KOMUTLAR ###

def islev_ataturk():
    print("2 Dakikalık Saygı Duruşu!")
    time.sleep(120)

def islev_tarih():
    zaman = datetime.datetime.now()
    print(f"{zaman.strftime('%x-%X')}")
    
def islev_bukelemun():
    print("""Bukelemun  sürüm: 1.2 beta
Aşağıdaki renklerden birinin sayısını giriniz. \n

Kırmızı için 1
Yeşil için 2
Mavi için 3
Sarı için 4 
Eski haline (beyaz) için 5 yazınız.\n""")
    
    secim = str(input(">>>"))
    
    if secim == "1":
        print(Fore.RED + "Seçtiğiniz renk uygulandı.")
        
    elif secim == "2":
        print(Fore.GREEN + "Seçtiğiniz renk uygulandı.")
        
    elif secim == "3":
        print(Fore.BLUE + "Seçtiğiniz renk uygulandı.")
        
    elif secim == "4":
        print(Fore.YELLOW + "Seçtiğiniz renk uygulandı.")
        
    elif secim == "5":
        print(Style.RESET_ALL + "Seçtiğiniz renk uygulandı")
        
    else:
        print("İşlem iptal edildi.")
        pass
    
### PYTHON ### 

# Python'ı açar
def islev_python():
    if isletimSistemiTuru == 'nt':
        os.system(f"python")
    else:
        os.system(f'python3')

# `.py` uzantılı dosyaları çalıştırır   
def islev_calistir_python(py):
    if isletimSistemiTuru == 'nt':
        os.system(f"python {py}")
    else:
        os.system(f'python3 {py}')
        
### HATALAR ###

def hata():
    print("Hata <01> : Girdiğiniz komutun doğru veya tam olduğundan emin olun!")
