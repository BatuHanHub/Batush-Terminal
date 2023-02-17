from kodlar import *

if isletimSistemi == 'nt':
    kullaniciAdi = os.environ["USERPROFILE"]
    ad = kullaniciAdi[9:]
    os.chdir(f"{kullaniciAdi}\Onedrive")
    yol = os.listdir()
    if 'Desktop' in yol:
        os.chdir('Desktop')
    elif 'Masaüstü' in yol:
        os.chdir('Masaüstü')

else:
    kullaniciAdi = os.getenv('HOME')
    ad = kullaniciAdi[6:]
    os.chdir(kullaniciAdi)
    yol = os.listdir()
    if 'Desktop' in yol:
        os.chdir('Desktop')
    elif 'Masaüstü' in yol:
        os.chdir('Masaüstü')

bilgi()

while True: 
    kullanici = str(input(f"{ad}@{isletimSistemiAdi}-{isletimSistemi.upper()}:~$"))
    
    if kullanici == "temizle":
        temizle()
    
    elif kullanici == "çık":
        cik()
        break

    elif kullanici == "çalıştır":
        calistir()
    
    elif kullanici == "kapat":
        kapat()

    elif kullanici == "bukelemun":
        bukelemun()
        
    elif kullanici == "6 Şubat":
        Subat_6()
    
    elif kullanici == "sil":
        sil()
    
    elif kullanici == "liste":
        liste()
        
    elif kullanici == "olşdosya":
        olusturDosya()
        
    elif kullanici == "olşklasör":
        olusturKlasor()
    
    elif kullanici == "tarih":
        tarih()
    
    elif kullanici == "bilgi":
        bilgi()
        
    elif kullanici == "nerdeyim":
        nerde()
        
    elif kullanici == "git":
        git()
    
    elif kullanici == "çalışpy":
        calistirPython()

    elif kullanici == "python":
        python()
    
    elif kullanici == "Atatürk":
        Ataturk()
        
    elif kullanici == "yardım":
        yardim()

    elif kullanici == "lisans":
        lisans()
    
    elif kullanici == "1984":
        seniIzliyor()
    
    else:
        hata()
