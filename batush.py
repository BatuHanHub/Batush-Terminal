from kodlar import *
from islev import *

if isletimSistemiTuru == 'nt':
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
    if 'Masaüstü' in os.listdir():
        os.chdir('Masaüstü')
    elif 'Desktop' in os.listdir:
        os.chdir('Desktop')

while True: 
    
    if isletimSistemiTuru == 'nt':
        yer = os.getcwd()
        yer = yer[23:]
        
    else:
        yer = os.getcwd()
        sayi = len(kullaniciAdi)
        yer = yer[sayi:]
        
    try: 
        kullanici = str(input(f"{ad}@{isletimSistemiAdi.title()}-{isletimSistemiTuru.upper()}:{yer}~$"))
        
        # DOSYA İŞLEMLERİ
        
        if kullanici.startswith(olsdsy.inputKomut):
            islev_olustur_dosya(kullanici[7:])
        
        elif kullanici.startswith(olskls.inputKomut):
            islev_olustur_klasor(kullanici[7:])
            
        elif kullanici.startswith(oku.inputKomut):
            islev_dosyayi_oku(kullanici[4:])
            
        elif kullanici.startswith(sil.inputKomut):
            islev_dosya_sil(kullanici[4:])
        
        elif kullanici.startswith(silkls.inputKomut):
            islev_sil_klasor(kullanici[7:])
        
        
        elif kullanici.startswith(git.inputKomut):
            islev_git(kullanici[4:])

        elif kullanici.startswith(nerde.inputKomut):
            islev_nerdeyim()
        
        elif kullanici.startswith(listele.inputKomut):
            islev_liste()
            
        
        #TERMİNAL KOMUTLARI
        
        elif kullanici.startswith(temiz.inputKomut):
            islev_temizle()
        
        elif kullanici.startswith(cik.inputKomut):
            islev_cik()
            break
        
        elif kullanici.startswith(bukelemun.inputKomut):
            islev_bukelemun()
            
            
        elif kullanici.startswith(bilgilendir.inputKomut):
            islev_bilgi()
            
        elif kullanici.startswith(yardim.inputKomut):
            islev_yardim()
            
        #SİSTEM KOMUTLARI 

        elif kullanici.startswith(calistir.inputKomut):
            islev_calistir(kullanici[9:])
        
        elif kullanici.startswith(kapat.inputKomut):
            islev_kapat(kullanici[6:])
            
        elif kullanici.startswith(tarih.inputKomut):
            islev_tarih()
            
        # PYTHON
        
        elif kullanici.startswith(python.inputKomut):
            islev_python()
        
        elif kullanici.startswith(calistirPython.inputKomut):
            islev_calistir_python(kullanici[8:])
        
        #EK KOMUTLAR
        
        elif kullanici.startswith(Ataturk.inputKomut):
            islev_ataturk()
            
        else:
            hata()

    except UnicodeDecodeError:
        print('Hata <03> : Desteklenmeyen dosya biçimi.')
    except FileNotFoundError:
        print('Hata <04> : Böyle bir dosya yok.')
    except PermissionError:
        print('Hata <05> : Klasörü okuyamazsınız.')
