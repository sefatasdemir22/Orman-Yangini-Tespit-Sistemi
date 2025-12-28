# Orman Yangını Tespit Sistemi – Proje Raporu

## 1. Proje Konusu ve Önemi
Bu çalışmada, görüntüler üzerinden orman yangını tespiti yapabilen bir derin öğrenme modeli geliştirilmiştir. Orman yangınları erken fark edilmediğinde ciddi çevresel ve ekonomik kayıplara yol açmaktadır. Görüntü tabanlı otomatik tespit sistemleri, erken uyarı mekanizmaları için önemli bir potansiyel sunmaktadır.

## 2. Veri Seti
Veri seti, Kaggle platformundaki açık kaynaklı yangın veri kümelerinden derlenmiştir. Toplamda 2500’den fazla görüntü kullanılmıştır. Veri seti %80 eğitim ve %20 test olacak şekilde ayrılmıştır. Overfitting’i azaltmak amacıyla döndürme ve parlaklık değişimi gibi veri artırma (data augmentation) teknikleri uygulanmıştır.

## 3. Yöntem ve Model Seçimi
Model eğitimi için MobileNetV2 mimarisi tercih edilmiştir. Transfer learning yaklaşımı kullanılarak ImageNet üzerinde önceden eğitilmiş ağırlıklar yeniden eğitilmiştir. Literatürde ResNet ve EfficientNet gibi mimariler de kullanılmakla birlikte, bu projede hızlı çıkarım süresi ve daha az parametre gereksinimi nedeniyle MobileNetV2 seçilmiştir.

## 4. Model Eğitimi ve Değerlendirme
Model 5 epoch boyunca eğitilmiştir. Eğitim doğruluğu %97.2, doğrulama doğruluğu %93.8 olarak elde edilmiştir. Eğitim sürecine ait doğruluk ve kayıp grafikleri assets klasöründe paylaşılmıştır.

## 5. Uygulama ve Arayüz
Eğitilen model, Gradio tabanlı bir web arayüzü ile sunulmuştur. Kullanıcılar, arayüz üzerinden bir görüntü yükleyerek yangın tespit sonucunu anlık olarak görüntüleyebilmektedir.

## 6. Sonuç ve Gelecek Çalışmalar
Elde edilen sonuçlar, önerilen yaklaşımın yangın tespiti için etkili olduğunu göstermektedir. Gelecek çalışmalarda daha büyük veri setleri ve farklı çevresel koşullar ile modelin genelleme yeteneğinin artırılması hedeflenmektedir.
