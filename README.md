project:
  name: "Orman Yangını Tespit Sistemi"
  course: "Derin Öğrenme"
  type: "Görüntü Sınıflandırma (CNN)"

readme_content: |
  🚒 **Orman Yangını Tespit Sistemi (Wildfire Detection System)**

  Bu proje, görüntüler üzerinden **orman yangını (Fire)** ve **normal durum (No-Fire)**
  sınıflandırması yapabilen, Derin Öğrenme (CNN) tabanlı bir görüntü
  sınıflandırma sistemidir. Amaç, orman yangınlarının erken tespitine
  yönelik pratik ve uygulanabilir bir karar destek modeli geliştirmektir.

  Proje; model eğitiminin gerçekleştirildiği Jupyter Notebook’u ve kullanıcı
  dostu **Gradio Web Arayüzü**nü içermektedir.

  🔗 **Gradio Demo:**
  BURAYA_GRADIO_LINKINI_YAPISTIR

  ------------------------------------------------------------

  🎯 **Proje Konusu ve Seçilme Gerekçesi**

  Orman yangınları, erken fark edilmediğinde kısa sürede büyük alanlara
  yayılarak ciddi çevresel ve ekonomik kayıplara yol açmaktadır. Bu proje,
  görüntü tabanlı derin öğrenme yaklaşımları kullanarak yangın tespitini
  otomatikleştirmeyi ve erken uyarı sistemlerine katkı sunmayı amaçlamaktadır.

  Literatürde, CNN tabanlı görüntü sınıflandırma ve transfer learning
  yaklaşımları orman yangını tespiti problemlerinde yaygın olarak
  kullanılmaktadır. Bu çalışma, literatürdeki bu yöntemleri temel alarak
  sade ve etkili bir prototip geliştirmeyi hedeflemektedir.

  ------------------------------------------------------------

  📥 **Veri Seti**

  Bu projede kullanılan veri seti, **Kaggle platformunda yer alan açık
  kaynaklı orman yangını veri kümelerinden derlenmiştir**.

  • Toplam veri sayısı: 2500+ görüntü  
  • Sınıflar: Fire / No-Fire  
  • Veri bölünmesi: %80 Eğitim / %20 Test  

  Modelin ezberlemesini (overfitting) önlemek amacıyla eğitim verilerine
  **data augmentation** teknikleri uygulanmıştır. Bu kapsamda:

  • Görüntü döndürme (rotation)  
  • Parlaklık değişimi (brightness adjustment)  

  Veri seti, geliştirme sürecinde yerel ortamda ZIP dosyası olarak
  kullanılmıştır. GitHub dosya boyutu kısıtlamaları nedeniyle doğrudan
  repoya eklenmemiştir.

  Kullanılan klasör yapısı:

      data/
          Fire/
          NoFire/

  Notebook ve eğitim kodları bu dizin yapısına göre hazırlanmıştır.

  ------------------------------------------------------------

  🧠 **Yöntem ve Model Seçimi**

  Model eğitimi için **MobileNetV2** mimarisi kullanılmıştır.
  ImageNet veri seti üzerinde önceden eğitilmiş ağırlıklar,
  **Transfer Learning** yaklaşımı ile yeniden eğitilmiştir.

  MobileNetV2 tercih edilme nedenleri:

  • Daha az parametre sayısı  
  • Hızlı eğitim ve çıkarım süresi  
  • Kaynak kısıtlı sistemler için uygunluk  

  Literatürde ResNet ve EfficientNet gibi daha derin mimariler de
  kullanılmaktadır. Ancak bu projede, pratiklik ve verimlilik
  kriterleri göz önünde bulundurularak MobileNetV2 tercih edilmiştir.

  ------------------------------------------------------------

  📊 **Model Eğitimi ve Değerlendirme**

  Model, 5 epoch boyunca eğitilmiştir.

  Elde edilen sonuçlar:

  • Eğitim doğruluğu: %97.2  
  • Doğrulama doğruluğu: %93.8  

  Eğitim sürecine ait doğruluk ve kayıp grafikleri **assets** klasöründe
  paylaşılmıştır.

  Örnek eğitim grafiği:

  ![Model Başarı Grafiği](assets/basari_grafigi.png)

  ------------------------------------------------------------

  📂 **Proje Dosya Yapısı**

  • app.py  
    → Gradio tabanlı web arayüzünü başlatan ana uygulama dosyası

  • notebook/  
    → Modelin eğitildiği Jupyter Notebook

  • models/  
    → Eğitilmiş Keras modeli (yangin_tespit_modeli.keras)

  • assets/  
    → Eğitim doğruluk ve kayıp grafikleri

  • README.md  
    → Proje dokümantasyonu

  • requirements.txt  
    → Gerekli Python kütüphaneleri

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
