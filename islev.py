# Kütüphaneler
import datetime, time # Zamanla alakalı
import os, sys, platform, shutil, distro # Sistemle alakalı
from colorama import Fore, init, Style

surum = "8.0"

isletimSistemiTuru = os.name # kullanıcının kullandığı işletim sisteminin çekirdeği
isletimSistemiAdi = platform.system() # kullanıcının kullandığı işletim sisteminin adı 

if isletimSistemiAdi == "Linux":
    dagitim = distro.like()

### DOSYA VE KLASÖR İŞLEMLERİ ###

def islev_super_program_kur(program):
    if distro.like() == "debian":
        os.system(f"sudo dpkg -i {program}")

    elif distro.like() == "fedora":
        os.system(f"sudo dnf install {program}")
                    
    else:
        print(Fore.RED + "Desteklenmeyen işletim sistemi veya Linux dağıtımı." + Style.RESET_ALL)
    pass

def islev_super_guncelle():
    if isletimSistemiAdi == "Windows":
        os.system("winget upgrade --all")

    elif distro.like() == "debian":
        os.system("LC_ALL=C sudo apt-get update && sudo apt-get upgrade")  
        # LC_ALL=C yazmamdaki sebep bazı Linux dağıtımlarında update süresi ya çok uzun sürüyor ya da hiç ilerlemiyor

    elif distro.like() == "arch":
        os.system("sudo pacman -Syu && sudo pacman -Syyu")
    
    elif distro.like() == "fedora":
        os.system("sudo dnf update && sudo dnf upgrade")

    elif isletimSistemiAdi == "Bsd":
        os.system("sudo pkg upgrade")

    elif isletimSistemiAdi == "Darwin":
        print("MacOS desteği yok.")

def islev_super_kur(paketAdi):
    if isletimSistemiAdi == "Windows":
        os.system(f"winget install {paketAdi}")

    elif distro.like() == "debian":
        os.system(f"sudo apt-get install {paketAdi}")  
        
    elif distro.like() == "arch":
        os.system(f"sudo pacman -S {paketAdi}")
    
    elif distro.like() == "fedora":
        os.system(f"sudo dnf install {paketAdi}")

    elif isletimSistemiAdi == "Bsd":
        os.system(f"sudo pkg install {paketAdi}")

    elif isletimSistemiAdi == "Darwin":
        print("MacOS desteği yok.")

def islev_super_kaldir(paketAdi):
    if isletimSistemiAdi == "Windows":
        os.system(f"winget uninstall {paketAdi}")

    elif distro.like() == "debian":
        os.system(f"sudo apt-get remove {paketAdi}")  
        
    elif distro.like() == "arch":
        os.system(f"sudo pacman -R {paketAdi}")
    
    elif distro.like() == "fedora":
        os.system(f"sudo dnf remove {paketAdi}")

    elif isletimSistemiAdi == "Bsd":
        os.system(f"sudo pkg remove {paketAdi}")

    elif isletimSistemiAdi == "Darwin":
        print("MacOS desteği yok.")

def islev_super_ara(paketAdi):
    if isletimSistemiAdi == "Windows":
        os.system(f"winget show {paketAdi}")

    elif distro.like() == "debian":
        os.system(f"sudo apt search {paketAdi}")  
        
    elif distro.like() == "arch":
        os.system(f"sudo pacman -Ss {paketAdi}")
    
    elif distro.like() == "fedora":
        os.system(f"sudo dnf search {paketAdi}")

    elif isletimSistemiAdi == "Bsd":
        os.system(f"sudo pkg search {paketAdi}")

    elif isletimSistemiAdi == "Darwin":
        print("MacOS desteği yok.")

def islev_super_listele():
    if isletimSistemiAdi == "Windows":
        os.system(f"winget list")

    elif distro.like() == "debian":
        os.system(f"sudo dpkg --list")  
        
    elif distro.like() == "arch":
        os.system("sudo pacman -Q")
    
    elif distro.like() == "fedora":
        os.system("sudo dnf list installed")

    elif isletimSistemiAdi == "Bsd":
        os.system("sudo pkg info")

    elif isletimSistemiAdi == "Darwin":
        print("MacOS desteği yok.")

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
    print(f"""Batush(Batuhan'ın Bash'i) Beta {surum}\n
BatuHanHub tarafından Python diliyle yazılmıştır. Sadece eğlenmek ve Python bilgimi sınamak için yazılmıştır.
Bash'in Türkçe hali ve Bash benzeri :D.

Yardım istiyorsanız `yardım` komutunu kullanabilirsiniz :)

Github: https://github.com/BatuHanHub\n""")
    
def islev_yardim():
    print("""  BATUSH KOMUTLARI

UYARI!: KOMUTLARINIZI KÜÇÜK HARFLERLE YAZINIZ. (Atatürk hariç) 

# PAKET VE SİSTEM KOMUTU
          
Sağlayıcılar:
Windows - Winget(Windows 10 ve üstü Windows sürümlerinde çalışır.)
Linux - Debian[apt ve .deb], Arch[Pacman], Fedora[dnf ve .rpm]
BSD - pkg
          
## SÜPER KOMUTLARI
          
süper güncelle : sisteminizi ve repolarınızı günceller
süper kur [paket_adi] : paket kurmanıza yarar
süper kaldır [paket_adi] : kurulu paketi kaldırmanıza yarar
süper ara [paket_adi] : girdiğiniz paket adını arar
süper liste : sisteminizde kurulu olan paketleri listeler
          
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

# EK KOMUTLAR
Atatürk   : denemelisin    
tarih     : zaman ve tarihi gösterir
benkimim : sizin kim olduğunuzu gösterir
bune [komut_adi] : komut hakkında bilgi verir
""")

def islev_degis(komut):
    if isletimSistemiTuru == 'nt':
        os.system(komut)
    else:
        os.system(komut)
    
### EK KOMUTLAR ###

def islev_ataturk():
    k = Fore.RED
    b = Fore.WHITE
    print(Fore.RED + f"""  /$$$$$$  /$$   /$$ /$$$$$$$$             /$$           /$$$$$$  /$$   /$$ /$$$$$$$ 
 /$$__  $$| $$  | $$| $$_____/            |  $$         /$$__  $$| $$  | $$| $$__  $$
| $$  \__/| $$  | $$| $$                   \  $$       | $$  \__/| $$  | $$| $$  \ $$
| $$      | $$$$$$$$| $$$$$          /$$$$$$\  $$      | $$      | $$$$$$$$| $$$$$$$/
| $$      | $$__  $$| $$__/         |______/ /$$/      | $$      | $$__  $$| $$____/ 
| $$    $$| $$  | $$| $$                    /$$/       | $$    $$| $$  | $$| $$      
|  $$$$$$/| $$  | $$| $$                   /$$/        |  $$$$$$/| $$  | $$| $$      
 \______/ |__/  |__/|__/                  |__/          \______/ |__/  |__/|__/                                                                                           

::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::{b}clol{k}:::::{b}ldoc{k}:::::::::{b}lddc{k}:::::::::::::
:::::::::::{b}lkxl{k}:::{b}clxxl{k}:::::::{b}clodxlc{k}:::::::::::::
::::::::::{b}ldoc{k}::{b}clooc{k}::::::{b}clooolc{k}::::::::::::::::
:::::::::{b}ldlc{k}:{b}clool{k}::::{b}cloooolc{k}::::::::::{b}coxdlc{k}:::
:::::::{b}codl{k}::{b}codlc{k}:::{b}coddooc{k}::::::::{b}ccloooodoc{k}::::
::::::{b}cdxl{k}:{b}coxoc{k}::{b}clddolc{k}:::::::{b}clooooolc{k}:::::::::
:::::{b}cdxlcoxdl{k}:{b}cldddlc:::::{b}cloooooolc{k}:::::::::::::
::::{b}lxxloxxlcldxdoc{k}:::{b}clodddoolcc{k}:::::::::::::::::
:::{b}lkxoxxoloxxdlccloddddoolc{k}::::::::::::{b}clolc{k}:::::
::{b}codxkxddxdolldddddolc{k}:::::::{b}cccllooooloxxlc{k}:::::
::::{b}codxxxdddxddocc{k}:{b}ccllooooooooooollccc{k}::::::::::
::::::{b}codxxddoooddddddddooollcc{k}:::::::::::::::::::
:::::::{b}cdxdddddoollcc{k}:::::::::::::::::::::::::::::
:::::::{b}cdkxxddddddddoooooooooooodxoc{k}::::::::::::::
::::::::{b}loooollllllllllllllllllloolc{k}::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::{b}

NNXNNNXNXNNNNNNN0dl;.... ..,lkXNXNNNNNNNNNNNNNNNNN
NNNNNNXXNNXNNKxc..           .;dKNNNNNNNXNNNNNNNNN
NNNNNNNNNNXkc'                  'cOXXNNNXNNNNNNNNN
NNNNNNNNNO;                       oNNNNNNNNNNNNNNN
NNNNNNNNNo                       .kNXNNNNNNNNNNNNN
NNNNNNNNNO.                      '0NNNNNXNNNNNNNNN
NNNNNNNNNXo                      ;KNNNNNNNNNNNNNNN
NNNNNNNNNN0;      .''',,;;;'.   .oNNNNNNNNNNNNNNNN
NNNNNNNNNNNk.   .cccdKXkoooddc. '0NNNNNNNNNNNNNNNN
NNNNNNNNNNNNd..:ccc,:0Xo;:clkXd.:KNXNNNNNNNNNNNNNN
NNNNNNNNNNNN0clKK0KXXXNXNNNXXNKxxKNNNNNNNNNNNNNNNN
NNNNNNNNNNNNXOllOXNKxdxO0KXNNNNKKNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNXd..kXO:,;ckKXNXNK0KNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNXNXl.ckoc;:coxOX0k0XXNNXNNNNNNNNNNNNNN
NNNNNNNNNNNXNXN0:.cKKdxXWWKdldKNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNO,.'cccoxxddK0OXNNNNNNNNNNNNNNNNNN
XNNNNXNNNNNNNNNkxOx, .cdOKKXO;.c0NNNNNNXNNNNNNNNNN
NNNNNNNNXXNNN0o..cO0xkXKxoc,.   .o0XNNNXNNNNNNNNNN
NNNNNNNNX0xo:.  ';,cccl:;,,.      .;ox0XNNNNNNNNNN
NNXNNKxc,.      cKd..ckXXKd.          .,cokKNNNNNN
NNXNXk,         :0l.cXNKl'.                'dXNNNN
NNNNNKc         ,:. .dk,                    :KNNNN
NXNNNKc.        .,. .,.                     :KNNNN
NNNNNXl....;cc' .;'',.                     .xNXNNN
NNXXNX0kkk0XXk,  ,l'                  .;:;.:KNNNNN
NNNNNNNNNXXNXOo. .''.';ccc:;'.    .:cxKXXK00XNNNNN
NNNNNNNNNNNNXNN0kkOKKKKKXKK0d,. .:ONNNNNNNNNNNNXXN
NNXNNNNNXNNXNNNNNXNNNNNXNNX0x::oxXNXXNNNNNNNXNNNNN """ + Style.RESET_ALL)

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
