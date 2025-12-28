# 🔥 Orman Yangını Tespit Sistemi

Bu proje, İstanbul Medeniyet Üniversitesi Bilgisayar Mühendisliği Bölümü Derin Öğrenme dersi bitirme ödevi kapsamında geliştirilmiştir.

## 📌 Proje Kriterleri ve Detaylar

### 1. Proje Konusu ve Önemi (15 Puan)
Orman yangınlarının erken tespiti ekosistemi korumak adına hayatidir. Bu projede, dijital görüntüler üzerinden yangın varlığını yüksek doğrulukla tespit edebilen bir derin öğrenme modeli geliştirilmiştir.

### 2. Veri Seti (15 Puan)
Eğitim sürecinde 2500'den fazla görsel içeren, yangın ve normal durumların dengeli dağıldığı 'Fire-Detection-Dataset' kullanılmıştır.

### 3. Uygulanan Yöntem ve Algoritma (15 Puan)
Model mimarisi olarak **MobileNetV2** tercih edilmiştir. 
- **Gerekçe:** MobileNetV2 mimarisi, düşük işlem gücü gereksinimi ve yüksek verimliliği (verimli parametre kullanımı) nedeniyle tercih edilmiştir.

### 4. Model Eğitimi ve Değerlendirme (20 Puan)
- **Eğitim Doğruluğu (Accuracy):** %97.2
- **Doğrulama Doğruluğu (Val Accuracy):** %93.8
- Model, karmaşıklığı azaltmak için GlobalAveragePooling2D ve Dropout katmanları ile optimize edilmiştir.

### 5. Proje Dokümantasyonu (10 Puan)
Sistem; model dosyası, arayüz kodu (Gradio) ve kütüphane gereksinimleri ile birlikte bu repoda sunulmuştur.