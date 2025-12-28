# 🚒 Orman Yangını Tespit Sistemi (Wildfire Detection System)

  Bu proje, görüntüler üzerinden **orman yangını (Fire)** ve **normal durum (No-Fire)**
  sınıflandırması yapabilen, Derin Öğrenme (CNN) tabanlı bir görüntü sınıflandırma
  sistemidir. Amaç, orman yangınlarının erken tespitine yönelik pratik ve
  uygulanabilir bir karar destek modeli geliştirmektir.

  Proje; model eğitiminin gerçekleştirildiği Jupyter Notebook’u, eğitilmiş modeli
  ve kullanıcı dostu **Gradio Web Arayüzü**nü içermektedir.

  🔗 **Gradio Demo:**  
  BURAYA_GRADIO_LINKINI_YAPISTIR

  ---

  ## 🎯 Proje Konusu ve Seçilme Gerekçesi

  Orman yangınları erken fark edilmediğinde kısa sürede geniş alanlara yayılmakta
  ve ciddi çevresel ve ekonomik kayıplara yol açmaktadır. Bu proje, görüntü tabanlı
  derin öğrenme yaklaşımları kullanarak yangın tespitini otomatikleştirmeyi ve
  erken uyarı sistemlerine katkı sunmayı amaçlamaktadır.

  Literatürde, CNN tabanlı görüntü sınıflandırma ve transfer learning yaklaşımları
  orman yangını tespiti problemlerinde yaygın olarak kullanılmaktadır. Bu çalışma,
  literatürdeki bu yöntemleri temel alarak sade ve etkili bir prototip
  geliştirmeyi hedeflemektedir.

  ---

  ## 📥 Veri Seti

  Bu projede kullanılan veri seti, **Kaggle platformunda yer alan açık kaynaklı
  orman yangını veri kümelerinden derlenmiştir**.

  - Toplam veri sayısı: **2500+ görüntü**
  - Sınıflar: **Fire / No-Fire**
  - Veri bölünmesi: **%80 Eğitim / %20 Test**

  Modelin ezberlemesini (overfitting) önlemek amacıyla eğitim verilerine
  **data augmentation** teknikleri uygulanmıştır:
  - Görüntü döndürme (rotation)
  - Parlaklık değişimi (brightness adjustment)

  Veri seti, geliştirme sürecinde yerel ortamda ZIP dosyası olarak kullanılmıştır.
  GitHub dosya boyutu kısıtlamaları nedeniyle doğrudan repoya eklenmemiştir.

  Kullanılan klasör yapısı:

      data/
          Fire/
          NoFire/

  Notebook ve eğitim kodları bu dizin yapısına göre hazırlanmıştır.

  ---

  ## 🧠 Yöntem ve Model Seçimi

  Model eğitimi için **MobileNetV2** mimarisi kullanılmıştır. ImageNet veri seti
  üzerinde önceden eğitilmiş ağırlıklar, **Transfer Learning** yaklaşımı ile
  yeniden eğitilmiştir.

  MobileNetV2 tercih edilme nedenleri:
  - Daha az parametre sayısı
  - Hızlı eğitim ve çıkarım süresi
  - Kaynak kısıtlı sistemler için uygunluk

  Literatürde ResNet ve EfficientNet gibi daha derin mimariler de kullanılmaktadır.
  Ancak bu projede pratiklik ve verimlilik kriterleri göz önünde bulundurularak
  MobileNetV2 tercih edilmiştir.

  ---

  ## 📊 Model Eğitimi ve Değerlendirme

  Model, **5 epoch** boyunca eğitilmiştir.

  Elde edilen sonuçlar:
  - Eğitim doğruluğu: **%97.2**
  - Doğrulama doğruluğu: **%93.8**

  Eğitim sürecine ait doğruluk ve kayıp grafikleri **assets/** klasöründe
  paylaşılmıştır.

  ---

  ## 📂 Proje Dosya Yapısı

  - src/  
    → Gradio tabanlı web arayüzünü içeren uygulama kodları

  - models/  
    → Eğitilmiş Keras modeli (**yangin_tespit_modeli.keras**)

  - assets/  
    → Eğitim doğruluk ve kayıp grafikleri

  - notebook/  
    → Model eğitiminin gerçekleştirildiği Jupyter Notebook

  - docs/  
    → Proje raporu ve teknik dokümantasyon (**report.md**)

  - README.md  
    → Proje tanıtım ve kullanım dokümantasyonu

  - requirements.txt  
    → Gerekli Python kütüphaneleri

  ---

  ## 🛠 Kurulum ve Çalıştırma

  Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

      git clone https://github.com/sefatasdemir22/Orman-Yangini-Tespit-Sistemi.git
      cd Orman-Yangini-Tespit-Sistemi
      pip install -r requirements.txt
      python src/app.py

  Bu komut, tarayıcı üzerinden erişilebilen bir Gradio web arayüzü başlatacaktır.

  ---

  ## 👤 Hazırlayan

  Sefa Taşdemir  
  İstanbul Medeniyet Üniversitesi  
  Bilgisayar Mühendisliği
