🔥 Orman Yangını Tespit Sistemi (Forest Fire Detection)

Bu proje, derin öğrenme tekniklerini kullanarak görüntüler üzerinden otomatik yangın tespiti yapmak amacıyla geliştirilmiştir. Sistem, özellikle hızlı müdahale gerektiren orman yangınlarının erken teşhisi için optimize edilmiş bir görüntü sınıflandırma modelidir.

📊 Proje Kriterleri ve Başarımlar

1. Proje Konusu ve Önemi (15 Puan)

Orman yangınlarının erken tespiti, ekosistemi korumak, biyolojik çeşitliliği savunmak ve can/mal kayıplarını önlemek adına hayati önem taşır. Bu uygulama, dijital görüntülerden (insansız hava araçları veya sabit kameralar) gelen verileri saniyeler içinde analiz ederek yangın ve dumanı ayırt eder.

2. Veri Seti (15 Puan)

Eğitim sürecinde, yangın olan ve yangın olmayan durumları içeren yaklaşık 2500 görsellik dengeli bir veri seti kullanılmıştır. Modelin farklı ışık koşullarında ve karmaşık arka planlarda doğru çalışabilmesi için Data Augmentation (Veri Artırma) teknikleri ile veri çeşitliliği artırılmıştır.

3. Uygulanan Yöntem ve Algoritma (15 Puan)

Model mimarisi olarak MobileNetV2 tercih edilmiştir.

Edge AI Uyumluluğu: Düşük parametre sayısı ve verimli hesaplama blokları sayesinde kısıtlı donanım kaynaklarında (Dronlar, Jetson Nano vb.) gerçek zamanlı analiz yapabilmektedir.

Transfer Learning: Model, ImageNet veri kümesinde eğitilmiş ağırlıklar üzerine inşa edilerek yüksek başarı oranı hedeflenmiştir.

4. Model Eğitimi ve Değerlendirme (20 Puan)

Model, 5 epoch gibi optimize bir sürede yüksek başarı oranlarına ulaşmıştır:

Eğitim Doğruluğu (Train Accuracy): %97.2

Doğrulama Doğruluğu (Val Accuracy): %93.8

5. Proje Dokümantasyonu ve Yapısı (10 Puan)

Proje içeriği, teknik analiz ve son kullanıcı deneyimini birleştiren profesyonel bir yapıda sunulmuştur:

app.py: Gradio tabanlı kullanıcı dostu web arayüzü dosyası.

models/: Eğitilmiş .keras formatındaki güncel model dosyası.

assets/: Modelin başarı ve hata grafiklerini içeren klasör.

requirements.txt: Sistemin çalışması için gerekli kütüphane listesi.

🛠 Kurulum ve Kullanım

Gerekli Kütüphaneleri Yükleyin:

pip install -r requirements.txt


Uygulamayı Çalıştırın:

python app.py


Komut çalıştıktan sonra terminalde çıkan gradio.live linkini kopyalayarak tarayıcınızda arayüze erişebilirsiniz.

Hazırlayan: Sefa Taşdemir

Kurum: İstanbul Medeniyet Üniversitesi - Bilgisayar Mühendisliği Bölümü