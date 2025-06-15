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

---

## 🔧 Neler Destekleniyor?

✅ `işlev` tanımı (fonksiyonlar)  
✅ `değişken` tanımı (sayı, yazı, ondalık)  
✅ `eğer / değilse` koşulları  
✅ `sürekli` döngüsü  
✅ `çağır` ile fonksiyon çağrısı  
✅ `yaz` komutu ile ekrana çıktı  
✅ `girdi` ile kullanıcıdan veri alma  
✅ `boyut()` ile C `sizeof()` karşılığı  
✅ Tüm komutlar Türkçe kelimelerle

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
