import gradio as gr
import tensorflow as tf
import numpy as np

# Yeni modeli yükle
model = tf.keras.models.load_model('yangin_tespit_modeli.keras')

def predict(img):
    # Görüntü hazırlama
    img = tf.image.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0) / 255.0
    
    # Tahmin yap
    prediction = model.predict(img)[0][0]
    
    # Sonucu yorumla
    if prediction < 0.5:
        return f"Yangın Tespiti: %{int((1-prediction)*100)} (YANGIN VAR)"
    else:
        return f"Yangın Tespiti: %{int(prediction*100)} (GÜVENLİ)"

# En sade Gradio arayüzü
demo = gr.Interface(
    fn=predict, 
    inputs="image", 
    outputs="text",
    title="Orman Yangını Tespit Sistemi"
)

demo.launch(share=True)