# 🧠 Lung Cancer Detection using Transfer Learning (VGG16)

> A deep learning-powered system for early detection of lung cancer using chest X-ray images — built using transfer learning with VGG16 and deployed using Streamlit.

---

## 📌 Project Highlights

- ✅ Used VGG16 (Transfer Learning) on chest X-ray images
- 📊 Achieved 75% validation accuracy
- 📁 Visualized class distribution and model performance
- 💻 Real-time predictions via Streamlit web app
- 🚀 Ready for deployment and real-world usage

---

## 🔧 Tech Stack

- Python, TensorFlow, Keras, OpenCV, Matplotlib, Seaborn
- Streamlit (for frontend web app)
- Transfer Learning (VGG16)

---

## 📁 Folder Structure

```
Lung_Cancer_TransferLearning/
├── data/                   ← (Not uploaded to GitHub)
├── notebooks/
│   ├── 01_data_preprocessing_and_EDA.ipynb
│   ├── 02_model_building_and_training.ipynb
│   ├── 03_evaluation_and_visualization.ipynb
│   └── lung_cancer_app.py   ← Streamlit App
├── static/                 ← Streamlit image styling
├── templates/              ← HTML template for Streamlit
├── requirements.txt
├── README.md
├── .gitignore
```

---

## 🚀 How to Run the Streamlit App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/AtharvaPatil04/Lung_Cancer_TransferLearning.git
cd Lung_Cancer_TransferLearning
```

### 2. Create a Virtual Environment & Activate

```bash
python -m venv venv_tf
venv_tf\Scripts\activate   # For Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Download Model File

> 🔗 [Download best_vgg16_model.h5 from Google Drive](https://drive.google.com/file/d/1EEnv8InMWrE91-Mi5rAroH_lRavdg3Mf/view?usp=sharing)

- Place it in the `/notebooks` folder

### 5. Run the Streamlit App

```bash
streamlit run notebooks/lung_cancer_app.py
```

---

## 📊 Sample Results

- **Training Accuracy:** ~90%
- **Validation Accuracy:** ~75%
- Real-time prediction of "NORMAL" or "PNEUMONIA" with confidence score

---

## 📬 Contact

- 🔗 [LinkedIn](https://www.linkedin.com/in/atharvaajaypatil/)
- 📧 atharvapatil221004@gmail.com

---

## ⭐ Star this repo if you find it helpful!
