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
        
    
    kullanici = str(input(f"{ad}@{isletimSistemiAdi.title()}-{isletimSistemiTuru.upper()}:{yer}~$"))
        
    # DOSYA İŞLEMLERİ
        
    if kullanici.split()[0] == olsdsy.inputKomut:
        islev_olustur_dosya(kullanici[7:])
        
    elif kullanici.split()[0] == olskls.inputKomut:
        islev_olustur_klasor(kullanici[7:])
            
    elif kullanici.split()[0] == oku.inputKomut:
        islev_dosyayi_oku(kullanici)
            
    elif kullanici.split()[0] == sil.inputKomut:
        islev_dosya_sil(kullanici[4:])
        
    elif kullanici.split()[0] == silkls.inputKomut:
        islev_sil_klasor(kullanici[7:])
        
        
    elif kullanici.split()[0] == git.inputKomut:
        islev_git(kullanici[4:])

    elif kullanici.split()[0] == nerde.inputKomut:
        islev_nerdeyim()
        
    elif kullanici.split()[0] == listele.inputKomut:
        islev_liste()
            
        
    #TERMİNAL KOMUTLARI
        
    elif kullanici.split()[0] == temiz.inputKomut:
        islev_temizle()
        
    elif kullanici.split()[0] == cik.inputKomut:
        islev_cik()
        break
            
    elif kullanici.split()[0] == bilgilendir.inputKomut:
        islev_bilgi()
            
    elif kullanici.split()[0] == yardim.inputKomut:
        islev_yardim()
            
    #SİSTEM KOMUTLARI 

    elif kullanici.split()[0] == calistir.inputKomut:
        islev_calistir(kullanici[9:])
        
    elif kullanici.split()[0] == kapat.inputKomut:
        islev_kapat(kullanici[6:])
            
    elif kullanici.split()[0] == tarih.inputKomut:
        islev_tarih()
            
    elif kullanici.split()[0] == degis.inputKomut:
        islev_degis(kullanici[3:])
            
    # PYTHON
        
    elif kullanici.split()[0] == python.inputKomut:
        islev_python()
        
    elif kullanici.split()[0] == calistirPython.inputKomut:
        islev_calistir_python(kullanici[8:])
        
    #EK KOMUTLAR
        
    elif kullanici.split()[0] == Ataturk.inputKomut:
        islev_ataturk()
        
    elif kullanici.split()[0] == kalp.inputKomut:
        islev_kalp()
            
    else:
        hata()
