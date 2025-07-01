import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
from PIL import Image

# Page config
st.set_page_config(
    page_title="Lung Cancer Detection",
    page_icon="🫁",
    layout="centered"
)

# Load model with caching
@st.cache_resource
def load_cancer_model():
    model = load_model("best_vgg16_model.h5")  # Path relative to this file
    return model

model = load_cancer_model()

# Prediction function
def predict_image(img):
    img = img.convert("RGB")  # Convert grayscale to RGB
    img = img.resize((224, 224))  # Resize to match model input
    img_array = img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    pred_prob = model.predict(img_array)[0][0]  # Predict
    pred_class = "PNEUMONIA" if pred_prob > 0.5 else "NORMAL"
    confidence = pred_prob if pred_prob > 0.5 else 1 - pred_prob
    return pred_class, confidence

# Streamlit UI
st.title("🫁 Lung Cancer Detection using Chest X-rays")
st.write("Upload a chest X-ray image (JPEG/PNG). The model will classify it as **PNEUMONIA** or **NORMAL**.")

uploaded_file = st.file_uploader("Choose an X-ray image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Analyzing...")

    pred_class, confidence = predict_image(image)

    st.markdown(f"### 🧠 Prediction: **{pred_class}**")
    st.markdown(f"### 🔍 Confidence: **{confidence * 100:.2f}%**")

    if pred_class == "PNEUMONIA":
        st.error("⚠️ This X-ray shows signs of Pneumonia.")
    else:
        st.success("✅ This X-ray appears Normal.")

#.\venv_tf\Scripts\activate
#cd notebooks
#streamlit run lung_cancer_app.py