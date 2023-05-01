# Kütüphaneler
from kodlar import * # Komutların bulunduğu alan
from islev import * # Komutların işlevlerinin bulunduğu alan

# Windows
if isletimSistemiTuru == 'nt':
    kullaniciAdi = os.environ["USERPROFILE"]
    ad = kullaniciAdi[9:]

# Linux/MacOS/BSD(-ler)
else:
    kullaniciAdi = os.getenv('HOME')
    ad = kullaniciAdi[6:]

while True: 
    
    yer = os.getcwd()
        
    try:
        kullanici = str(input(f"{ad}@{isletimSistemiAdi.title()}-{isletimSistemiTuru.upper()}>{yer}~$"))
            
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
            
    except IndexError: # Eğer kullanıcı boş komut girerse :
        continue
