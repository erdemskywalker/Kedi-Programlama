<h1 align="center">🦁 Kedi Programming Language - Türkçe Betik Tabanlı Derleyici</h1>

<p align="center">
  Türkçe dilinde yazılmış özel bir betik dili ⌨️<br>
  <strong>Parser + AST + C Derleyici + GCC</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/build-passing-brightgreen?style=flat-square">
  <img src="https://img.shields.io/badge/dil-Türkçe-blue?style=flat-square">
  <img src="https://img.shields.io/badge/derleyici-GCC-red?style=flat-square">
</p>

---

## 🎯 Neden kedi.py?

🐾 Kedi.py, Türkçe'ye özel olarak geliştirilmiş bir programlama dili derleyicisidir.  
Kodlar Türkçe yazılır, otomatik olarak C diline çevrilir ve çalıştırılır.  
Amacım: Türk gençleri için yazılımı daha anlaşılır ve erişilebilir kılmak.  

🟣 Online Web Editor: https://kedi.erdemskywalker.site

---

## 🔧 Neler Destekleniyor?

<table style="width: 100%;">
    <thead>
      <tr>
        <th>Komut / Yapı</th>
        <th>Açıklama</th>
        <th>Örnek Kod</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>yaz</td><td>Ekrana çıktı verir</td><td>yaz "Merhaba"</td></tr>
      <tr><td>değişken</td><td>Değişken tanımlar</td><td>değişken yazı Ad = "Erdem"</td></tr>
      <tr><td>işlev</td><td>Fonksiyon tanımlar</td><td>işlev SelamVer(yazı Ad)</td></tr>
      <tr><td>çağır</td><td>Fonksiyon çağırır</td><td>çağır SelamVer("Erdem")</td></tr>
      <tr><td>eğer</td><td>Koşullu ifade</td><td>eğer yazikarsilastir(Ad,"Erdem")</td></tr>
      <tr><td>değilse</td><td>Alternatif durum</td><td>değilse</td></tr>
      <tr><td>sürekli</td><td>Döngü başlatır</td><td>sürekli i < 10</td></tr>
      <tr><td>girdi <span style="color:pink;">(WEB'TE KULLANILMAZ)</span></td><td>Kullanıcıdan veri alır</td><td>girdi(İsim, boyut(İsim))</td></tr>
      <tr><td>boyut()</td><td>sizeof karşılığı</td><td>boyut(İsim)</td></tr>
      <tr><td>alt</td><td>Yeni satır</td><td>alt</td></tr>
      <tr><td>.</td><td>Blok bitirici</td><td>.</td></tr>
    </tbody>
  </table>

---

## ✨ Örnek Kod

```laneb
yaz "Merhaba"
satır
```

⚙️ Linux'a İndirme
```
nano indir.sh
```
```
#!/bin/bash

echo "➡️ Kedi Programlama kuruluyor..."

if ! command -v gcc &> /dev/null; then
    echo "ℹ️  gcc yüklü değil, şimdi yüklenecek..."

    if [ -f /etc/debian_version ]; then
        sudo apt update && sudo apt install -y gcc
    elif [ -f /etc/arch-release ]; then
        sudo pacman -Sy --noconfirm gcc
    else
        echo "⚠️ Bu sistem otomatik gcc yüklemeyi desteklemiyor. Lütfen manuel yükleyin."
        exit 1
    fi
fi


git clone https://github.com/erdemskywalker/Kedi-Programlama || {
    echo "❌ Git klonlama başarısız!"
    exit 1
}


sudo mkdir -p /lib/Kedi-Programlama
sudo cp -r Kedi-Programlama/linux/* /lib/Kedi-Programlama/


sudo tee /usr/bin/kedi > /dev/null <<'EOF'
#!/bin/bash
python3 /lib/Kedi-Programlama/kedi.py "$1"
EOF


sudo chmod +x /usr/bin/kedi


rm -rf ./Kedi-Programlama

echo "✅ BAŞARIYLA YÜKLENDİ | KEDİ PROGRAMLAMA"
echo "ℹ️  Artık terminalden 'kedi' komutunu kullanabilirsin."

```
```
chmod +x indir.sh
sudo indir.sh
```

⚙️ Windowsa İndirme
```
GCC Kurulumunu Yap
```
```
indir.bat
```
```
@echo off
setlocal EnableDelayedExpansion

:: Yönetici kontrolü (basit)
net session >nul 2>&1
if ERRORLEVEL 1 (
    echo Bu scripti YONETICI olarak calistiriniz.
    pause
    exit /b
)

echo Kedi Programlama kuruluyor...

:: Python kontrolü
where python >nul 2>nul
if ERRORLEVEL 1 (
    echo Python bulunamadi. Lutfen once Python yukleyin.
    pause
    exit /b
)

:: Powershell kontrolü
where powershell >nul 2>nul
if ERRORLEVEL 1 (
    echo Powershell bulunamadi. Bu script icin Powershell gereklidir.
    pause
    exit /b
)

echo Kedi Programlama indiriliyor...
powershell -Command "Invoke-WebRequest -Uri https://github.com/erdemskywalker/Kedi-Programlama/archive/refs/heads/main.zip -OutFile Kedi.zip"
if ERRORLEVEL 1 (
    echo Zip indirme basarisiz oldu.
    pause
    exit /b
)

echo Zip dosyasi aciliyor...
powershell -Command "Expand-Archive -Path Kedi.zip -DestinationPath ."
if ERRORLEVEL 1 (
    echo Zip acma basarisiz oldu.
    pause
    exit /b
)

set "KEDI_DIR=%ProgramFiles%\Kedi-Programlama"
if not exist "%KEDI_DIR%" (
    mkdir "%KEDI_DIR%"
)

echo Dosyalar kopyalaniyor...
xcopy /E /Y "Kedi-Programlama-main\*" "%KEDI_DIR%\"
if ERRORLEVEL 1 (
    echo Dosya kopyalama basarisiz oldu.
    pause
    exit /b
)

del Kedi.zip >nul 2>nul
rmdir /S /Q Kedi-Programlama-main >nul 2>nul

echo PATH kontrol ediliyor...

:: Sistem PATH güncellemesi için
setlocal enabledelayedexpansion
echo %PATH% | find /I "%KEDI_DIR%" >nul
if ERRORLEVEL 1 (
    echo PATH'e "%KEDI_DIR%" ekleniyor...
    setx /M PATH "%PATH%;%KEDI_DIR%"
    echo PATH guncellendi. Lütfen oturumu kapatıp açın.
) else (
    echo PATH zaten %KEDI_DIR% iceriyor.
)
endlocal

@echo off
set KEDI_DIR=C:\Program Files\Kedi-Programlama

python "%KEDI_DIR%\kedi.py" %1





echo.
echo Kedi Programlama basariyla kuruldu.
echo PATH degisikligi yapildi. PATH'in aktif olmasi icin oturumu kapatip yeniden giris yapmaniz gerekebilir.
echo Artik terminalde "kedi dosya.kedi" seklinde kullanabilirsiniz.
echo.
echo GCC veya uyumlu bir C derleyici sisteminizde yuklu olmalidir. Windows icin MinGW veya MSYS2 onerilir.
pause

```


👨‍💻 Geliştirici
Yapımcı: Erdem Skywalker
Amaç: Eğitim, yazılım sevgisi ve özgünlük.
Yazarken büyüyen, paylaştıkça gelişen bir proje.

💬 Katkı Yap
Yıldızla ⭐ | Issue aç 🔧 | PR gönder 💻 | Yorum yaz 💬
Bu proje, genç bir geliştiricinin kendi dilini yaratma hayaliyle başladı.
Senin desteğinle büyümeye devam edecek.
