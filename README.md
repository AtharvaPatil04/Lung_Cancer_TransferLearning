# 🫁 Lung Cancer Detection using Transfer Learning

A deep learning project to classify chest X-ray images as **NORMAL** or **PNEUMONIA**, powered by **VGG16 transfer learning** and deployed as a **Streamlit web app**.

---

## 📌 Problem Statement

Lung cancer and pneumonia are major causes of death globally. Accurate and early detection can save lives, but manual diagnosis from chest X-rays is time-consuming and error-prone. This project builds a machine learning model to assist doctors in diagnosing X-rays efficiently.

---

## 🎯 Project Objectives

- Use transfer learning (VGG16) for binary image classification (Normal vs Pneumonia)
- Train the model on chest X-ray images
- Evaluate accuracy using validation/test set
- Deploy a simple web app for image prediction using Streamlit

---

## 🧠 Technologies Used

| Type | Tech |
|------|------|
| Language | Python |
| Deep Learning | TensorFlow / Keras |
| Image Processing | OpenCV, Pillow |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Web App | Streamlit |
| Model | VGG16 (Transfer Learning) |

---

## 🗂️ Folder Structure

```
Lung_Cancer_TransferLearning/
│
├── data/              # X-ray images (NOT pushed to GitHub)
├── models/            # Optional model backup
├── notebooks/
│   ├── 01_data_preprocessing_and_EDA.ipynb
│   ├── 02_model_building_and_training.ipynb
│   ├── 03_model_evaluation.ipynb
│   ├── lung_cancer_app.py
│   └── best_vgg16_model.h5
├── static/            # Streamlit assets (optional)
├── templates/         # Streamlit HTML templates (if needed)
├── venv_tf/           # Virtual environment (excluded)
├── requirements.txt   # Required libraries
├── .gitignore
└── README.md          # This file
```

---

## 🧪 Model Performance

| Metric        | Value     |
|---------------|-----------|
| Validation Accuracy | **75%** |
| Model Params  | ~14.7M (VGG16 pretrained) |
| Trainable Params | ~74K |
| Image Size    | 224 x 224 RGB |

---

## 🚀 How to Run the App Locally

### 1. Clone this repository
```bash
git clone https://github.com/your-username/Lung_Cancer_TransferLearning.git
cd Lung_Cancer_TransferLearning
```

### 2. Set up the virtual environment
```bash
python -m venv venv_tf
.\venv_tf\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run notebooks/lung_cancer_app.py
```

---

## 📸 Sample Output

> 🧠 Prediction: **PNEUMONIA**  
> 🔍 Confidence: **93.2%**  
> ✅ Image preview displayed in app  

---

## 📚 Dataset Source

Chest X-Ray Images (Pneumonia)  
📦 [Kaggle Dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

---

## 👨‍💻 Author

**Atharva Patil**  
📍 Pune, India  
💼 Aspiring Data Scientist | BSc Honours  
📧 [Connect on LinkedIn](https://www.linkedin.com/) *(insert link)*  
📸 [Instagram](https://www.instagram.com/) *(optional)*

---

## ⭐ Project Highlights

- ✅ Real-world ML application in healthcare
- ✅ Transfer learning using VGG16
- ✅ 75% validation accuracy
- ✅ Deployed as a live web app with Streamlit
