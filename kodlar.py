from colorama import *
import requests
import datetime
import time
import os

soru = ""
secim = ""

def calistir():
    soru = str(input("Başlatacağınız programın adını giriniz:[örn: Batush.exe]\n>"))
    os.system(f"start {soru}")

def kapat():
    soru = str(input("Kapatacağınız programın adını giriniz:[örn: Batush.exe]\n>"))
    os.system(f'taskkill /f /im "{soru}"')

def temizle():
    os.system("cls")
        
def sil():
    soru = str(input("Hangi dosyası silmek istersiniz?\n>>>"))
    secim = str(input(f"{soru} dosyasını silmek istediğinizden emin misiniz? e/h >"))
    if secim == "e"or"E":
        os.remove(soru)
        pass
    else:
        print("İşlem iptal edildi.")
        pass
    
def cik():
    print(Style.RESET_ALL)
    os.system("exit")

def liste():
    for liste in os.listdir():
        print(liste)
    
def olusturDosya():
    soru = str(input("Dosya adınız ne olsun ve ne formatında (.txt vs.) [dosyaadı.format]?\n>"))
    dosya = open (f"{soru}", "w", encoding="utf8")
    dosya.close()
    
def olusturKlasor():
    soru = str(input("Klasör adınız ne olsun?\n>"))
    os.mkdir(soru)

def nerde():
    print(os.getcwd())
    
def git():
    soru = str(input("Hangi klasöre gitmek istersiniz?\n>"))
    if soru in os.listdir():
        os.chdir(soru)

    elif soru == "Masaüstü":
        kullaniciAdi = os.environ["USERPROFILE"]
        os.chdir(f"{kullaniciAdi}\Onedrive\Masaüstü\\")
    
    else:
        print("HATA2: Öyle bir klasör yok")

def yardim():
    temizle()
    print("""BATUSH(Batuhan'ın Bash'i) KODLARI

UYARI!: KOMUTLARINIZI KÜÇÜK HARFLERLE YAZINIZ.

# DOSYA İŞLEMLERİ
olşdosya : dosya oluşturursunuz 
olşklasör : klasör oluşturursunuz
git : konumunuzu değiştirir (masaüstüne gitmek için 'Masaüstü' yazın) 
nerdeyim : şu anki konumunuzu gösterir 
liste : konumunuzdaki dosyaları gösterir 
sil : dosya siler

# TERMİNAL KOMUTLARI
temizle : terminali temizler
çık : terminalden çıkarsınız
yardım : terminal kodlarını ve işlevlerini gösterir
bukelemun : yazı rengi değiştirir

çalıştır : program çalıştırır
kapat : program kapatır

python : Python'u açar
çalışpy : Python dosyasını çalıştırır
tarih : zaman ve tarihi gösterir

1984 : George Orwell'ın ütopyası
6 Şubat : :(
Atatürk : deneyin :)
bilgi : Batush hakkında bilgi verir
lisans : lisansı hakkında bilgi verir

NOT: komutları kullanırken örnek olarak 'olşdosya dosyaadi.txt' yerine 'olşdosya' yazın. Size 'Dosya adını ne yapalım?'
diye soru soracaktır orada ad ve dosya uzantısı giriniz.""")

def bilgi():
    print("""Batush(Batuhan'ın Bash'i) Beta 3.0\n
BatuHanHub tarafından Python diliyle yazılmıştır. Sadece eğlenmek ve Python bilgimi sınamak için yazılmıştır.
GPL 3.0 lisansı ile dağıtılmaktadır. Telif hakkı (c) BatuHanHub

Github: https://github.com/BatuHanHub
Bloğum: https://tatliyazilimci.blogspot.com/ \n""")


def python():
    os.system("python")

def tarih():
    zaman = datetime.datetime.now()
    print(f"{zaman.strftime('%x-%X')}")

def Ataturk():
    temizle()
    print("2 Dakikalık Saygı Duruşu!")
    time.sleep(120)

def Subat_6():
    temizle()
    print("""\a
Adıyaman
Diyarbakır
Gaziantep
Hatay
Kahramanmaraş
Kilis
Malatya
Osmaniye
Şanlıurfa

AHBAP: https://ahbap.org/""")

def seniIzliyor():
    temizle()
    dosya = open("GEORGE19 ORWELL48.txt", "w", encoding="utf8")
    dosya.write("""01000010 01010101 01011001 01010101 01001011 00100000 01000010 01001001 01010010 01000001 01000100 01000101
01010010 00100000 01010011 01000101 01001110 01001001 00100000 01001001 01011010 01001100 01001001 01011001
01001111 01010010 00100001 00001010 00001010 01010011 01100001 01110110 01100001 01110011 00100000 01000010
01100001 01110010 01101001 01110011 01110100 01101001 01110010 00100000 00001010 01001111 01111010 01100111
01110101 01110010 01101100 01110101 01101011 00100000 01001011 01101111 01101100 01100101 01101100 01101001
01101011 01110100 01101001 01110010 00100000 00001010 01000011 01100001 01101000 01101001 01101100 01101100
01101001 01101011 00100000 01000111 01110101 01100011 01110100 01110101 01110010 00101110""")
    dosya.close()
    print("\a1984 saniye bekle. Bekleyene kadar bence dosyalarına bak :)") 
    time.sleep(1984)

def bukelemun():
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

def calistirpython():
    soru = str(input("Çalıştıracağınız Python dosyasının adını giriniz.[örn: dosyaadi.py]\n>"))
    os.system(f"python {soru}")

def lisans():
    temizle()
    lisans=requests.get("https://www.gnu.org/licenses/gpl-3.0.txt")
    print(lisans.text)

def hata():
    print("HATA1: Komudunuzu doğru veya küçük yazdığınızdan emin olun.")
