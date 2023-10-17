# Değişim günlüğü :rocket:
- MacOS'a süper desteği geldi
- Ufak düzeltmeler
- İpconfig/İfconfig komutları yerine => ipadr komutu eklendi (İP ADRes)

# Kullanmadan önce!
Python 3.x, Pip ve Colorama kütüphanenizin yüklü olması gerekmektedir.

# Batush Kılavuzu
![](https://miro.medium.com/max/1400/1*xjraSVbFOl1b5346bPGoIw.png)
# Batush(Batuhan'ın Bash'i) nedir?
Batush, Türkçe komutları olan Bash benzeri konsol/terminal/uçbirim.

# SÜPER PAKET YÖNETİCİ VE SİSTEM GÜNCELLEME KOMUTU 
Süper komutu, paketlerinizi yönetmeyi ve sistem güncelleştirmelerini kolay ve detaylı yapmanızı
sağlar. Windows(Winget), Linux(Debian[apt ve .deb], 
Arch(Pacman), Fedora(dnf ve .rpm)), MacOS(Homebrew) ve BSD(pkg) paket yöneticilerini kullanmanıza yarar.

### Winget nedir ve nasıl indirilir?
Windows 10 ve üstü Windows sürümlerinde kurulu gelmektedir. 
Winget açık kaynak kodlu Microsoft'a ait paket yöneticisidir.

Kaynak kodları: https://github.com/microsoft/winget-cli

## Süper komutları

süper güncelle : sisteminizi ve reponuzu günceller</br>

süper kur [paket_adi] : paket kurmanıza yarar</br>

süper kaldır [paket_adi] : kurduğunuz paketi kaldırmanıza yarar</br>

süper ara [paket_adi] : paket adını repodan arar</br>

süper liste : yüklediğiniz paketleri ve uygulamaları listeler</br>

# BATUSH KOMUTLARI

# DOSYA VE KLASÖR İŞLEMLERİ

olşdsy [dosya_adi.uzantisi] : dosya oluşturursunuz </br>

sil [dosya_adi.uzantisi] :  dosya siler </br>

oku [dosya_adi.uzantisi] : dosyayı okur</br>

olşkls [klasor_adi] : klasör oluşturursunuz</br> 

silkls [klasor_adi] : klasör siler </br>

git [yol_adi] : konumunuzu değiştirir (geri gitmek için `git <-` yazmalısınız) </br>

nerdeyim : şu anki konumunuzu gösterir </br>

ls : konumunuzdaki dosyaları gösterir </br>

kpy [dosya_adi.turu/klasör_adi],[yeniAd] : konumunuzdaki dosyayı/klasörü hedef dizine kopyalar</br>

taşı [dosya_adi.turu/klasör_adi],[yeniAd] : konumunuzdaki dosyayı/klasörü hedef dizine taşır</br>

isim [dosya_adi.turu/klasör_adi],[yeniAd] : konumunuzdaki dosya/klasörün adını değiştirir

# SİSTEM KOMUTLARI
çık : terminalden çıkarsınız</br>

temizle : terminali temizler</br>

başlat [program_adi] : program çalıştırır</br>

kapat [dosya_adi.uzantisi] : program kapatır</br>

bilgi : Batush hakkında bilgi verir</br>

yardım : terminal kodlarını ve işlevlerini gösterir</br>

!> [komut] : Batush'da olmayan veya komutları kullanmayı veya</br>
Bash ya da CMD komutlarınızı kullanmaya yarar.</br>

ipadr : İp ve MAC adresinizi ekrana yazar </br>

# PYTHON
python : Python'u açar</br>

# EK KOMUTLAR
Atatürk : denemelisiniz</br>

tarih : zaman ve tarihi gösterir</br>

benkimim : sizin kim olduğunuzu gösterir</br> 

bune [komut_adi] : komut hakkında bilgi verir</br></br>

# Desteklenen platformlar
## Windows:
![Windows](resim/Windows.png)
## Linux:
![Linux](resim/Linux.png)
## MacOS
## BSD
