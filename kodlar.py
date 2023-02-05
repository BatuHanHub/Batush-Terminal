from colorama import *
import datetime
import time
import os

isletimSistemi = os.name
soru = ""
secim = ""

def temizle():
    if isletimSistemi == "nt":
        os.system("cls")
    elif isletimSistemi == "posix":
        os.system("clear")
        
def sil():
    soru = str(input("Hangi dosyası silmek istersiniz?\n>>>"))
    secim = str(input(f"{soru} dosyasını silmek istediğinizden emin misiniz? E/H >"))
    if secim == "E":
        os.remove(soru)
        pass
    else:
        print("İşlem iptal edildi.")
        pass
    
def cik():
    os.system("exit")

def liste():
    for liste in os.listdir():
        print(liste)
    
def olustur():
    soru = str(input("Dosya adınız ne olsun ve ne formatında (.txt vs.) [dosyaadı.format]?\n>>>"))
    dosya = open (f"{soru}", "w", encoding="utf8")
    dosya.close()

def yardim():
    temizle()
    print("""BATUSH(Batuhan'ın Bash'i) KODLARI

UYARI!: KOMUTLARINIZI KÜÇÜK HARFLERLE YAZINIZ.

# DOSYA İŞLEMLERİ
oluştur : dosya oluşturursunuz 
değiş : konumunuzu değiştirir (masaüstüne gitmek için 'Masaüstü' yazın) 
nerdeyim : şu anki konumunuzu gösterir 
liste : konumunuzdaki dosyaları gösterir 
sil : dosya siler

# TERMİNAL KOMUTLARI
temizle : terminali temizler
çık : terminalden çıkarsınız
yardım : terminal kodlarını ve işlevlerini gösterir
bukelemun : yazı rengi değiştirir

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
    temizle()
    print("2 Dakikalık Saygı Duruşu!")
    time.sleep(120)
    
def bukelemun():
    print("""Bukelemun  sürüm: 0.1 beta
Aşağıdaki renklerden birinin sayısını giriniz. \n

Kırmızı için 1
Yeşil için 2
Mavi için 3
Sarı için 4 yazınız.\n""")
    
    secim = str(input(">>>"))
    
    if secim == "1":
        print(Fore.RED + "Seçtiğiniz renk uygulandı.")
        
    elif secim == "2":
        print(Fore.GREEN + "Seçtiğiniz renk uygulandı.")
        
    elif secim == "3":
        print(Fore.BLUE + "Seçtiğiniz renk uygulandı.")
        
    elif secim == "4":
        print(Fore.YELLOW + "Seçtiğiniz renk uygulandı.")
        
    else:
        print("İşlem iptal edildi.")
        pass
    
def hata():
    print("HATA1: Komudunuzu doğru veya küçük yazdığınızdan emin olun.")
