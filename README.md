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



👨‍💻 Geliştirici
Yapımcı: Erdem Skywalker
Amaç: Eğitim, yazılım sevgisi ve özgünlük.
Yazarken büyüyen, paylaştıkça gelişen bir proje.

💬 Katkı Yap
Yıldızla ⭐ | Issue aç 🔧 | PR gönder 💻 | Yorum yaz 💬
Bu proje, genç bir geliştiricinin kendi dilini yaratma hayaliyle başladı.
Senin desteğinle büyümeye devam edecek.
