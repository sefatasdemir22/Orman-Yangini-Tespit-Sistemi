Orman Yangını Tespit Sistemi

Bu proje, görüntüler üzerinden orman yangını (Fire) / normal durum (No-Fire) sınıflandırması yapabilen, derin öğrenme tabanlı bir görüntü sınıflandırma sistemidir. Model, önceden eğitilmiş bir CNN mimarisi kullanılarak eğitilmiş ve Gradio tabanlı web arayüzü ile sunulmuştur.

Gradio Demo:
BURAYA_GRADIO_LINKINI_YAPISTIR

Proje Özellikleri

• CNN tabanlı görüntü sınıflandırma
• Transfer Learning (MobileNetV2)
• Fire / No-Fire sınıflandırması
• %93.8 doğrulama başarımı
• Gradio ile web arayüzü üzerinden canlı demo
• Keras (.keras) formatında eğitilmiş model

Veri Seti

Bu projede kullanılan veri seti, yangın içeren ve normal durumları temsil eden görüntülerden oluşmaktadır.

• Sınıflar: Fire, No-Fire
• Toplam veri: 2500+ görüntü
• Eğitim ve doğrulama setlerine ayrılmıştır
• Görüntüler yeniden boyutlandırılmış ve normalize edilmiştir

Veri seti, geliştirme sürecinde yerel ortamda ZIP dosyası olarak kullanılmıştır. GitHub dosya boyutu kısıtlamaları nedeniyle doğrudan repoya eklenmemiştir.

Kullanılan klasör yapısı:

data/
    Fire/
    NoFire/


Notebook ve eğitim kodları bu dizin yapısına göre hazırlanmıştır.

Kullanılan Yöntem

Model eğitimi için MobileNetV2 mimarisi kullanılmıştır. ImageNet veri seti üzerinde önceden eğitilmiş ağırlıklar transfer learning yaklaşımıyla yeniden eğitilmiştir.

Bu yaklaşımın tercih edilme nedenleri:

• Daha az parametre
• Daha hızlı eğitim ve çıkarım süresi
• Görüntü sınıflandırma problemleri için yeterli doğruluk

Model Eğitimi ve Sonuçlar

Model 5 epoch boyunca eğitilmiştir.

Elde edilen sonuçlar:

• Eğitim doğruluğu: %97.2
• Doğrulama doğruluğu: %93.8

Eğitim sürecine ait doğruluk ve kayıp grafikleri ile confusion matrix çıktıları assets klasöründe bulunmaktadır.

Örnek eğitim grafiği:

Proje Dosya Yapısı

assets
→ Eğitim grafikleri ve görseller

models
→ Eğitilmiş Keras modeli (yangin_tespit_modeli.keras)

notebook
→ Modelin eğitildiği Jupyter Notebook

app.py
→ Gradio web arayüz uygulaması

README.md
→ Proje dokümantasyonu

requirements.txt
→ Gerekli Python kütüphaneleri

Kurulum ve Çalıştırma

Projeyi bilgisayarınıza klonlayın

Gerekli kütüphaneleri requirements.txt üzerinden kurun

app.py dosyasını çalıştırın

Açılan Gradio arayüzünden bir görüntü yükleyerek tahmin alın

Demo Kullanımı

• Arayüze bir görüntü yükleyin
• Model görüntüyü analiz eder
• Sonuç “YANGIN VAR” veya “GÜVENLİ” olarak gösterilir
• Güven skoru yüzde olarak sunulur

Sunum Akışı (2 Dakika)

• Proje amacı ve problem tanımı
• Kullanılan veri seti
• Model ve yöntem
• Gradio üzerinden 2–3 örnek demo
• Sonuçların kısa değerlendirmesi

Gelecek Çalışmalar

• Daha büyük ve çeşitli veri setleriyle modelin genellenmesi
• Farklı çevresel koşulların modellenmesi
• Gerçek zamanlı sistemlere entegrasyon

Hazırlayan

Sefa Taşdemir
İstanbul Medeniyet Üniversitesi
Bilgisayar Mühendisliği