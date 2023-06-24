# Kütüphaneler
import datetime, time # Zamanla alakalı
import os, sys, platform, shutil # Sistemle alakalı
from colorama import Fore, init, Style

isletimSistemiTuru = os.name # kullanıcının kullandığı işletim sisteminin çekirdeği
isletimSistemiAdi = platform.system() # kullanıcının kullandığı işletim sisteminin adı 

### DOSYA VE KLASÖR İŞLEMLERİ ###

# Dosya işleri
def islev_olustur_dosya(dsyAdi):
    try:
        with open(f'{dsyAdi}','w',encoding='utf8') as dosya:
                dosya.close()

    except FileNotFoundError:
        print(Fore.RED + "Hata : Bir değer giriniz." + Style.RESET_ALL)

def islev_dosya_sil(dsySil):
    liste = os.listdir()
    try:
        if dsySil in liste:
                os.remove(dsySil)

        else:
            print(Fore.RED + f'Hata : {dsySil} adında dosya yok.' + Style.RESET_ALL)

    except AttributeError:
            print(Fore.RED + f'Hata : {dsySil} adında dosya yok.' + Style.RESET_ALL)

    except PermissionError:
        print(Fore.RED + f'Hata : Klasör silemezsin.' + Style.RESET_ALL)

def islev_dosyayi_oku(dsyAdi):
    try:
        with open(f'{dsyAdi[4:]}','r',encoding='utf8') as dosya:
            for satir in dosya.readlines():
                print(satir)
            
    except UnicodeDecodeError: # Eğer desteklenmeyen bir dosya biçimiyse
        print(Fore.RED + 'Hata : Desteklenmeyen dosya biçimi.' + Style.RESET_ALL)
    except FileNotFoundError: # Eğer böyle bir dosya yoksa
        print(Fore.RED + 'Hata : Böyle bir dosya yok.' + Style.RESET_ALL)
    except PermissionError: # Eğer kullanıcı klasör okumaya çalışırsa
        print(Fore.RED + 'Hata : Klasörü okuyamazsınız.' + Style.RESET_ALL)

# Klasör işleri    
def islev_olustur_klasor(klsAdi):
    liste = os.listdir()
    try:
        if klsAdi in liste:
            print(Fore.RED + "Hata : Aynı klasörden birden fazla olamaz." + Style.RESET_ALL)
        
        else:
            os.mkdir(klsAdi)
    except FileNotFoundError:
        print(Fore.RED + "Hata : Bir değer giriniz." + Style.RESET_ALL)

def islev_sil_klasor(klsSil):
    liste = os.listdir()
    try:
        if klsSil in liste:
            os.rmdir(klsSil)

        else:
            print(Fore.RED + f"Hata : '{klsSil}' adlı klasör yok." + Style.RESET_ALL)

    except AttributeError:
        print(Fore.RED + f'Hata : {klsSil} adında dosya yok.' + Style.RESET_ALL)

    except FileNotFoundError: # Eğer böyle bir dosya yoksa
        print(Fore.RED + 'Hata : Böyle bir dosya yok.' + Style.RESET_ALL)

# Yol işleri

def islev_nerdeyim():
    print(os.getcwd())

def islev_liste():
    for ls in os.listdir():
        print(ls)

### SİSTEM KOMUTLARI ###

def islev_cik():
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
    print("""Batush(Batuhan'ın Bash'i) Beta 7.0\n
BatuHanHub tarafından Python diliyle yazılmıştır. Sadece eğlenmek ve Python bilgimi sınamak için yazılmıştır.
Bash'in Türkçe hali ve Bash benzeri :D.

Yardım istiyorsanız `yardım` komutunu kullanabilirsiniz :)

Github: https://github.com/BatuHanHub\n""")
    
def islev_yardim():
    print("""  BATUSH KOMUTLARI

UYARI!: KOMUTLARINIZI KÜÇÜK HARFLERLE YAZINIZ. (Atatürk hariç) 

# DOSYA VE KLASÖR İŞLEMLERİ

olşdsy [dosya_adi.uzantisi] : dosya oluşturursunuz 
sil [dosya_adi.uzantisi] :  dosya siler 
oku [dosya_adi.uzantisi] : dosyayı okur

olşkls [klasor_adi]: klasör oluşturursunuz 
silkls [klasor_adi]: klasör siler 

git [yol_adi] : konumunuzu değiştirir (geri gitmek için `git <-` yazmalısınız) 
nerdeyim      : şu anki konumunuzu gösterir 
ls            : konumunuzdaki dosyaları gösterir 
kpy [dosya/klasör adi],[dosya/klasör adi] : konumunuzdaki dosyayı hedef dizine kopyalar
taşı [dosya/klasör adi],[dosya/klasör adi] : konumunuzdaki dosyayı hedef dizine taşır
isim [dosya/klasör adi],[yeni_ad] : konumunuzdaki dosya/klasör adını değiştirir

# SİSTEM KOMUTLARI
çık       : terminalden çıkarsınız
temizle   : terminali temizler
başlat [program_adi]: program çalıştırır
kapat [dosya_adi.uzantisi] : program kapatır
bilgi     : Batush hakkında bilgi verir
yardım    : terminal kodlarını ve işlevlerini gösterir
!> [komut]: Batush'da olmayan veya komutları kullanmayı veya
Bash ya da CMD komutlarınızı kullanmaya yarar.

# PYTHON
python    : Python'u açar
pyçalış [dosya_adi.py] : Python dosyasını çalıştırır

# EK KOMUTLAR
Atatürk   : ekranı temizler ve 2 dakika saygı duruşu için yazı yazamazsınız    
tarih     : zaman ve tarihi gösterir
bune [komut_adi] : komut hakkında bilgi verir
""")

def islev_degis(komut):
    if isletimSistemiTuru == 'nt':
        os.system(komut)
    else:
        os.system(komut)
    
### EK KOMUTLAR ###

def islev_ataturk():
    print("2 Dakikalık Saygı Duruşu!")
    time.sleep(120)

def islev_tarih():
    zaman = datetime.datetime.now()
    print(f"{zaman.strftime('%x-%X')}")

def islev_kalp():
    islev_temizle()
    print(Fore.RED + '''
              ******       ******
            **********   **********
          ************* *************
         *****************************
         *****************************
         *****************************
          ***************************
            ***********************
              *******************
                ***************
                  ***********
                    *******
                      ***
                       *

Benim için kıymetli hocalarım, ailem, abilerim, ablalarım(ablam yok :D), arkadaşlarım, can dostlarım veya yoldaşlarım;

Sensei Tankado / Güven Hocam / Osman Hocam / Tolga Hocam / Volkan Hocam / Ümit Hocam / Faruk Hocam / Sinan Hocam / Yeşim Hocam
Ailem / Emirhan Abim / ŞimşekBeyy / K1Y0H1M3 / Komиcсар Рабочих Мира / kullanici3 / 5Dollar / 0axper0 / Hey Efe 
Velberah / İMiracJK / Owwmen / Kaan Başgan / Tufan / Zeynep / Selçuk / Damla / Dilek / Ceylin / Yağız / Murat ve Bülent \n''' + Style.RESET_ALL)
    
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
