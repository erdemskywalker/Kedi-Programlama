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

Online Web Editor: http://176.96.131.83:5000/

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
işlev SelamVer(yazı Ad)
    eğer Ad=="Erdem"
        yaz "Hoşgeldin %s\n",Ad
    .
    değilse
        yaz "Tanınmayan Kişi %s\n",Ad
    .
.

değişken yazı İsim[10]
yaz "Adınız:"
girdi (İsim, boyut(İsim))
çağır SelamVer(İsim)
```

⚙️ Nasıl Çalıştırılır?
bash
Copy
Edit
git clone https://github.com/erdemskywalker/Kedi-Programming
cd kedi.py
python kedi.py -s program # program adında bir laneb dosyası olmalı
Çıktı program.c olarak oluşur ve otomatik derlenip çalıştırılır.
Desteklenen platformlar: Linux / Windows (GCC kurulu olması gerekir)

👨‍💻 Geliştirici
Yapımcı: Erdem Skywalker
Amaç: Eğitim, yazılım sevgisi ve özgünlük.
Yazarken büyüyen, paylaştıkça gelişen bir proje.

💬 Katkı Yap
Yıldızla ⭐ | Issue aç 🔧 | PR gönder 💻 | Yorum yaz 💬
Bu proje, genç bir geliştiricinin kendi dilini yaratma hayaliyle başladı.
Senin desteğinle büyümeye devam edecek.
