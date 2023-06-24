# Kütüphaneler {
import ctypes # Pencere başlığı için
from kodlar import * # Komutların bulunduğu alan
from islev import * # Komutların işlevlerinin bulunduğu alan
from colorama import init, Fore, Style
# }

def set_console_title(title):
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

if __name__ == "__main__":
    new_title = "Batush 7.0"
    set_console_title(new_title)

def hata():
    print(Fore.RED + f"'{kullanici}' diye bir komut yok, lütfen komutunuzun doğru veya tam olduğundan emin olun." + Style.RESET_ALL)

isletimSistemiRenk = None # İşletim sistemine göre renk kodu gelecek
sifirla = Style.RESET_ALL # Rengi sıfırlayacak

# Windows {
if isletimSistemiTuru == 'nt':
    isletimSistemiRenk = Fore.BLUE 
    anaDizin = os.environ["USERPROFILE"] 
    os.chdir(anaDizin + "\OneDrive")
    ad = anaDizin[9:]
# }

# Linux/MacOS/BSD(-ler) {
else:
    anaDizin = os.getenv('HOME')
    os.chdir(anaDizin)
    ad = anaDizin[6:] 

    if isletimSistemiAdi == "Darwin": 
        isletimSistemiAdi = "MacOS" 
        isletimSistemiRenk = Fore.LIGHTBLUE_EX

    elif isletimSistemiAdi == "Linux":
        isletimSistemiRenk = Fore.GREEN
    
    else:
        isletimSistemiRenk = Fore.RED
# }

while True: 
    
    yer = os.getcwd()
        
    try:
        init()

        kullanici = str(input(f"{Fore.LIGHTGREEN_EX + ad}@{isletimSistemiRenk + isletimSistemiAdi.title()}-{isletimSistemiTuru.upper()+ sifirla}>{Fore.BLUE + yer}{sifirla}$"))


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
            dizin = kullanici[4:]
  
            if dizin == '<-':
                os.chdir('..')

            elif dizin in os.listdir() or dizin not in os.listdir():
                try:
                    os.chdir(dizin)
                
                except FileNotFoundError:
                    print(Fore.RED + f"Hata : '{dizin}' böyle bir dizin yok." + Style.RESET_ALL)

                except NotADirectoryError:
                    print(Fore.RED + f"Hata : '{dizin}' bir dizin değildir." + Style.RESET_ALL)

                continue
            else:
                print(Fore.RED + f"Hata : '{dizin}' Böyle bir dizin yok." + Style.RESET_ALL)

        elif kullanici.split()[0] == nerde.inputKomut:
            islev_nerdeyim()
            
        elif kullanici.split()[0] == listele.inputKomut:
            islev_liste()

        elif kullanici.split()[0] == kopya.inputKomut:
            try:
                dsyAdi, kpDizin = kullanici[4:].split(',')    
                shutil.copy(dsyAdi,kpDizin)
            except ValueError:
                print(Fore.RED + f"Hata : Kopyalanacak dosya ve hedef dizin belirtiniz." + Style.RESET_ALL)

            except FileNotFoundError:
                print(Fore.RED + f"Hata : Hedef dizin belirtiniz." + Style.RESET_ALL)
            continue

        elif kullanici.split()[0] == tasi.inputKomut:
            try:
                dsyAdi, kpDizin = kullanici[5:].split(',')    
                shutil.move(dsyAdi,kpDizin)
            except ValueError:
                print(Fore.RED + f"Hata : Taşınacak dosya ve hedef dizin belirtiniz." + Style.RESET_ALL)

            except FileNotFoundError:
                print(Fore.RED + f"Hata : Hedef dizin belirtiniz." + Style.RESET_ALL)
            continue

        elif kullanici.split()[0] == yeniAd.inputKomut:
            try:
                eskiIsim, yeniIsim = kullanici[5:].split(',')  
                os.rename(eskiIsim,yeniIsim)
            except FileNotFoundError:
                print(Fore.RED + f"Hata : Eksik isim belirttiniz. Lütfen dosya ya da dizin belirtiniz." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + f"Hata : Eksik isim belirttiniz. Lütfen dosya ve dizin belirtiniz." + Style.RESET_ALL)
                
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
            islev_calistir(kullanici[7:])
            
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

        elif kullanici.split()[0] == bune.inputKomut:
            buneKomut = kullanici[5:] 
            for komut in tumKomutlar:
                if kullanici[5:] == komut.inputKomut:
                    komut.bilgileriYazdir()
                    break

            else:
                print(Fore.RED + f"'{buneKomut}' diye bir komut yok, lütfen komutunuzun doğru veya tam olduğundan emin olun." + Style.RESET_ALL)

        else:
            hata()
            
    except IndexError: # Eğer kullanıcı boş komut girerse :
        continue
