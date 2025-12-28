import gradio as gr
import tensorflow as tf
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
MODEL_PATH = PROJECT_ROOT / "models" / "yangin_tespit_modeli.keras"


# Modeli yükle
model = tf.keras.models.load_model(MODEL_PATH)

IMG_SIZE = (224, 224)

def predict(img):
    """
    Gradio image input genelde numpy array (H, W, C) gelir.
    Bazı durumlarda 0-255 uint8, bazen 0-1 float olabilir.
    Bu fonksiyon ikisini de güvenli biçimde normalize eder.
    """

    # img None gelirse (kullanıcı yüklemezse)
    if img is None:
        return "Lütfen bir görüntü yükleyin."

    # Gradio bazen float (0-1), bazen uint8 (0-255) döndürür.
    img = img.astype(np.float32)

    # Eğer maksimum 1.0 ise 0-1 aralığında; değilse 0-255'tir
    if img.max() > 1.5:
        img = img / 255.0

    # (H, W, C) -> TF tensor
    img_tf = tf.convert_to_tensor(img)

    # Eğer tek kanal gelirse RGB'ye çevir
    if len(img_tf.shape) == 2:
        img_tf = tf.expand_dims(img_tf, axis=-1)

    # Kanal sayısı 1 ise 3'e çıkar
    if img_tf.shape[-1] == 1:
        img_tf = tf.image.grayscale_to_rgb(img_tf)

    # Boyutlandır
    img_tf = tf.image.resize(img_tf, IMG_SIZE)

    # Batch ekle
    img_tf = tf.expand_dims(img_tf, axis=0)

    # Tahmin
    pred = model.predict(img_tf, verbose=0)

    # Çıkış formatına göre olasılığı çek
    # Binary sigmoid ise (1,1) olur; softmax ise (1,2) olabilir.
    if pred.shape[-1] == 1:
        p = float(pred[0][0])           # "pozitif sınıf" olasılığı
    else:
        p = float(pred[0][1])           # genelde [NoFire, Fire] veya [Fire, NoFire] olabilir (aşağıda açıklıyorum)

    # ÖNEMLİ: Burada p'nin hangi sınıfa ait olduğu model eğitimine bağlı.
    # Senin mevcut mantığında: p < 0.5 -> YANGIN VAR diyorsun (yani p = "GÜVENLİ" olasılığı gibi kullanılmış).
    # Ben aynı mantığı koruyorum:
    if p < 0.5:
        yangin_orani = int((1 - p) * 100)
        return f"Sonuç: YANGIN VAR | Güven Skoru: %{yangin_orani}"
    else:
        guvenli_orani = int(p * 100)
        return f"Sonuç: GÜVENLİ | Güven Skoru: %{guvenli_orani}"

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Textbox(label="Tahmin"),
    title="Orman Yangını Tespit Sistemi",
    description="Bir görüntü yükleyin. Model, Fire / No-Fire sınıflandırması yapar."
)

# Lokal çalıştırma için share=True olabilir.
# HuggingFace Spaces'ta share=False kullanmalısın.
if __name__ == "__main__":
    demo.launch(share=True)
