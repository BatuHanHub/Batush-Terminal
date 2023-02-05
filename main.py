from kodlar import *

kullaniciAdi = os.environ["USERPROFILE"]
os.chdir(f"{kullaniciAdi}\Onedrive\Masaüstü\\")

bilgi()

while True: 
    kullanici = str(input(">>>"))
    
    if kullanici == "temizle":
        temizle()
        kullanici = ""
    
    elif kullanici == "çık":
        print(Style.RESET_ALL)
        cik()
        break
    
    elif kullanici == "bukelemun":
        bukelemun()
    
    elif kullanici == "sil":
        sil()
    
    elif kullanici == "liste":
        liste()
        
    elif kullanici == "oluştur":
        olustur()
    
    elif kullanici == "tarih":
        tarih()
    
    elif kullanici == "bilgi":
        bilgi()
        
    elif kullanici == "nerdeyim":
        nerde()
        
    elif kullanici == "değiş":
        degis()
    
    elif kullanici == "Atatürk":
        Ataturk()
        
    elif kullanici == "yardım":
        yardim()
    
    else:
        hata()
