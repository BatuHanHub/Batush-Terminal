import datetime
import time
import os

isletimSistemi = os.name

soru = ""

def sil():
    if isletimSistemi == "nt":
        os.system("cls")
    elif isletimSistemi == "posix":
        os.system("clear")

def cik():
    os.system("exit")

def liste():
    print(os.listdir())
    
def olustur():
    soru = str(input("Dosya adınız ne olsun ve ne formatında (.txt vs.) [dosyaadı.format]?\n>>>"))
    dosya = open (f"{soru}", "w", encoding="utf8")
    dosya.close()

def yardim():
    sil()
    print("""BATUSH(Batuhan'ın Bash'i) KODLARI

UYARI!: KOMUTLARINIZI KÜÇÜK HARFLERLE YAZINIZ.

### DOSYA İŞLEMLERİ
oluştur : dosya oluşturursunuz 
değiş : konumunuzu değiştirir (masaüstüne gitmek için 'Masaüstü' yazın) 
nerdeyim : şu anki konumunuzu gösterir 
liste : konumunuzdaki dosyaları gösterir 

### TERMİNAL KOMUTLARI
sil : terminali temizler
çık : terminalden çıkarsınız
yardım : terminal kodlarını ve işlevlerini gösterir

tarih : zaman ve tarihi gösterir

Atatürk : deneyin :)
bilgi : Batush hakkında bilgi verir""")

def bilgi():
    print("""Batush(Batuhan'ın Bash'i) Beta 2.0\n
BatuHanHub tarafından Python diliyle yazılmıştır. Sadece eğlenmek ve Python bilgimi sınamak için yazılmıştır.
telif hakkı (c) BatuHanHub

Github: https://github.com/BatuHanHub
Bloğum: https://tatliyazilimci.blogspot.com/ \n""")

def tarih():
    zaman = datetime.datetime.now()
    print(f"{zaman.strftime('%x-%X')}")
    
def nerde():
    print(os.getcwd())
    
def degis():
    soru = str(input("Hangi klasöre gitmek istersiniz?\n>>>"))
    if soru in os.listdir():
        os.chdir(soru)

    elif soru == "Masaüstü":
        kullaniciAdi = os.environ["USERPROFILE"]
        os.chdir(f"{kullaniciAdi}\Onedrive\Masaüstü\\")
    
    else:
        print("HATA2: Öyle bir klasör yok")
    
def Ataturk():
    sil()
    print("2 Dakikalık Saygı Duruşu!")
    time.sleep(120)
    
def hata():
    print("HATA1: Komudunuzu doğru veya küçük yazdığınızdan emin olun.")