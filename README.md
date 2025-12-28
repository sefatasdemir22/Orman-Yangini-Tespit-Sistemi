project:
  name: "Orman Yangını Tespit Sistemi"
  description: >
    Bu proje, görüntüler üzerinden orman yangını (Fire) ve normal durum (No-Fire)
    sınıflandırması yapabilen, Derin Öğrenme (CNN) tabanlı bir görüntü
    sınıflandırma sistemidir. Model, önceden eğitilmiş bir mimari kullanılarak
    eğitilmiş ve Gradio tabanlı bir web arayüzü ile sunulmuştur.

readme_content: |
  🚒 **Orman Yangını Tespit Sistemi (Wildfire Detection System)**

  Bu proje, orman yangınlarını erken tespit etmeye yönelik geliştirilmiş,
  Derin Öğrenme (CNN) tabanlı bir görüntü sınıflandırma uygulamasıdır.
  Fire ve No-Fire sınıflarına ait görüntüler kullanılarak eğitilen model,
  yüksek doğrulukla sınıflandırma yapabilmektedir.

  Proje; model eğitiminin gerçekleştirildiği Jupyter Notebook’u ve kullanıcı
  dostu **Gradio Web Arayüzü**nü içermektedir.

  🔗 **Gradio Demo:**
  https://a8412ce0d8e4278783.gradio.live

  ------------------------------------------------------------

  🚀 **Proje Özellikleri ve Başarımlar**

  • CNN tabanlı görüntü sınıflandırma
  • Transfer Learning (MobileNetV2)
  • Fire / No-Fire sınıflandırması
  • Doğrulama doğruluğu: %93.8
  • Gradio tabanlı web arayüzü
  • Keras (.keras) formatında eğitilmiş model

  ------------------------------------------------------------

  📂 **Proje Dosya Yapısı**

  Proje içerisindeki klasör ve dosyaların görevleri şöyledir:

  • app.py
    → Gradio tabanlı web arayüzünü başlatan ana uygulama dosyası

  • notebook/
    → Modelin eğitildiği ve analiz edildiği Jupyter Notebook

  • models/
    → Eğitilmiş Keras modeli (yangin_tespit_modeli.keras)

  • assets/
    → Eğitim doğruluk ve kayıp grafikleri

  • README.md
    → Proje dokümantasyonu

  • requirements.txt
    → Gerekli Python kütüphaneleri

  ------------------------------------------------------------

  📥 **Veri Seti (Kurulum İçin Önemli)**

  Bu projede kullanılan veri seti, yangın içeren ve normal durumları
  temsil eden görüntülerden oluşmaktadır.

  • Sınıflar: Fire, No-Fire
  • Toplam veri: 2500+ görüntü

  Veri seti, geliştirme sürecinde yerel ortamda ZIP dosyası olarak
  kullanılmıştır. GitHub dosya boyutu kısıtlamaları nedeniyle doğrudan
  repoya eklenmemiştir.

  Kullanılan klasör yapısı:

      data/
          Fire/
          NoFire/

  Notebook ve eğitim kodları bu dizin yapısına göre hazırlanmıştır.

  ------------------------------------------------------------

  🛠 **Kurulum ve Kullanım**

  Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

  1️⃣ Projeyi Klonlayın

      git clone https://github.com/sefatasdemir22/Orman-Yangini-Tespit-Sistemi.git
      cd Orman-Yangini-Tespit-Sistemi

  2️⃣ Gerekli Kütüphaneleri Yükleyin

      pip install -r requirements.txt

  3️⃣ Uygulamayı Başlatın (Arayüz)

      python app.py

  Bu komut size tarayıcıda çalışan bir Gradio arayüz linki verecektir.

  ------------------------------------------------------------

  📊 **Model Eğitimi ve Sonuçlar**

  Model 5 epoch boyunca eğitilmiştir.

  • Eğitim doğruluğu: %97.2
  • Doğrulama doğruluğu: %93.8

  Eğitim sürecine ait doğruluk ve kayıp grafikleri assets klasöründe
  paylaşılmıştır.

  Örnek eğitim grafiği:

  ![Model Başarı Grafiği](assets/basari_grafigi.png)

  ------------------------------------------------------------

  🎤 **Sunum Akışı (2 Dakika)**

  • Problem tanımı ve proje amacı
  • Veri seti ve kullanılan yöntem
  • Gradio üzerinden 2–3 örnek demo
  • Sonuçların kısa değerlendirmesi

  ------------------------------------------------------------

  🔮 **Gelecek Çalışmalar**

  • Daha büyük ve çeşitli veri setleriyle modelin geliştirilmesi
  • Farklı çevresel koşullarda performans analizi
  • Gerçek zamanlı sistemlere entegrasyon

  ------------------------------------------------------------

  👤 **Hazırlayan**

  Sefa Taşdemir
  İstanbul Medeniyet Üniversitesi
  Bilgisayar Mühendisliği
