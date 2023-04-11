# Küütüphaneler
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
    try:
        with open(f'{dsyAdi}','r',encoding='utf8') as dosya:
            print('===Okudum===')
            for satir in dosya.readlines():
                print(satir)
            print('============\n')
            
    except UnicodeDecodeError:
        print('Hata <03> : Desteklenmeyen dosya biçimi.')
    except FileNotFoundError:
        print('Hata <04> : Böyle bir dosya yok.')
    except PermissionError:
        print('Hata <05> : Klasörü okuyamazsınız.')
        
# Klasör işleri    
def islev_olustur_klasor(klsAdi):
    os.mkdir(klsAdi)

def islev_sil_klasor(klsSil):
    os.rmdir(klsSil)

# Yol işleri
def islev_git(yol):
    if yol in os.listdir():
        os.chdir(yol)
        
    elif yol == '<-':
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
    print("""Batush(Batuhan'ın Bash'i) Beta 6.0\n
BatuHanHub tarafından Python diliyle yazılmıştır. Sadece eğlenmek ve Python bilgimi sınamak için yazılmıştır.
Bash'in Türkçe hali ve Bash benzeri :D.

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
!> [komut]: Batush'da olmayan veya komutları kullanmayı veya
Bash ya da CMD komutlarınızı kullanmaya yarar.

# PYTHON
python    : Python'u açar
pyçalış [dosya_adi.py] : Python dosyasını çalıştırır

# EK KOMUTLAR
Atatürk   : Ekranı temizler ve 2 dakika saygı duruşu için yazı yazamazsınız    
tarih     : zaman ve tarihi gösterir
bukelemun : yazı rengi değiştirir""")
    
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
    print('''
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

Benim için kıymetli hocalarım/ailem/abilerim/ablalarım(ablam yok :D)/arkadaşlarım, can dostlarım veya yoldaşlarım;

Ailem / Hocalarım / Emirhan Abim / ŞimşekBeyy / K1Y0H1M3 
Komиcсар Рабочих Мира / kullanici3 / 5Dollar / 0axper0 / Hey Efe 
Kortitanium / İMiracJK / Owmen / Kaan evr / Tufan / Zeynep 
Damla / Dilek / Ceylin / Yağız / Murat / rushxvpn9 / rabia ve Zeynep\n''')
    
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
