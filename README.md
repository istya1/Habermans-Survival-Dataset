# 🏥 Analisis Perbandingan Model untuk Prediksi Kelangsungan Hidup Pasien Kanker Payudara

## 👤 Informasi
- **Nama:** Istya Yulia Amesti  
- **NIM:** 233307019  
- **Repo:** [github.com/istya1/Habermans-Survival-Dataset](https://github.com/istya1/Habermans-Survival-Dataset)  
- **Video:** *[(https://drive.google.com/drive/folders/1aS62XsA_7xWRFJY6QpDR0U7f17nP22xv?usp=sharing)]*  

---

## 📘 Ringkasan Proyek
Proyek ini membandingkan tiga pendekatan pemodelan—**Baseline (Logistic Regression)**, **Advanced Machine Learning (Random Forest)**, dan **Deep Learning (Multilayer Perceptron)**—untuk memprediksi kelangsungan hidup pasien kanker payudara menggunakan **Haberman's Survival Dataset**. Tujuan utamanya adalah menentukan model terbaik yang dapat mendukung pengambilan keputusan klinis awal.

### ✅ Pencapaian Utama:
- Melakukan analisis mendalam terhadap karakteristik dataset medis.
- Membangun pipeline data preparation yang komprehensif.
- Mengembangkan dan melatih tiga model dengan arsitektur berbeda.
- Mengevaluasi performa menggunakan metrik yang relevan untuk data tidak seimbang.
- Menentukan model **Deep Learning (MLP)** sebagai model terbaik dengan **F1-Score 0.89**.

---

## 🎯 Problem & Goals
**Permasalahan:**
1. Dataset memiliki fitur terbatas dan ketidakseimbangan kelas yang signifikan.
2. Hubungan antara fitur klinis (usia, tahun operasi, jumlah nodus) dengan target survival bersifat kompleks dan non-linear.
3. Diperlukan model yang akurat untuk membantu identifikasi awal risiko pasien.

**Tujuan:**
1. Membangun dan membandingkan tiga model (Baseline, ML, DL) untuk prediksi survival.
2. Mengevaluasi performa dengan metrik seperti Accuracy, Precision, Recall, dan F1-Score.
3. Menghasilkan pipeline analisis yang reproducible dan terstruktur.

---
## 📁 Struktur Repository
```
project/
│
├── data/                          # Dataset
│   └── haberman_clean_istya.csv
│
├── notebooks/                    
├── src/                          
├── models/                        # Saved models
│   ├── model_istya.h5             # Model Deep Learning (MLP)
│   └── scaler_istya.pkl           # StandardScaler
│
├── images/                        # Visualizations
│   ├── training_curves_istya.png
│   └── confusion_matrix_istya.png
│
├── project_report_istya.txt       # Laporan hasil training
├── requirements.txt               # Dependencies
├── .gitignore
└── README.md
```

## 📊 Dataset: Haberman's Survival
- **Sumber:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/haberman%27s+survival)
- **Jumlah Data:** 306 sampel pasien
- **Tipe:** Data tabular numerik
- **Karakteristik Kunci:** Tidak ada missing value, tetapi terdapat ketidakseimbangan kelas (73% survive vs 27% tidak survive)

### 🎯 Fitur Utama
| Fitur | Tipe | Deskripsi |
|-------|------|-----------|
| `Age` | Integer | Usia pasien saat operasi (tahun) |
| `Year_of_Operation` | Integer | Tahun operasi (format 2 digit, e.g., 58 = 1958) |
| `Positive_Axillary_Nodes` | Integer | Jumlah kelenjar getah bening aksila positif |
| `Survival_Status` | Binary | Target: **0** (Bertahan ≥5 tahun), **1** (Meninggal <5 tahun) |

---

## 🔧 Data Preparation
Langkah-langkah preprocessing yang diterapkan:
1. **Cleaning:** Tidak ada missing values atau duplicates
2. **Transformasi:** 
   - Konversi target ke binary (0/1)
   - Standard scaling pada fitur numerik menggunakan `StandardScaler`
3. **Splitting:** 
   - **Stratified split** 80:20 (train:test) untuk menjaga distribusi kelas
   - Random state = 42 untuk reproducibility
4. **Balancing:** Pemberian class weights pada saat training untuk menangani imbalance

---

## 🤖 Modeling
Tiga model yang dikembangkan:

### 1. Model Baseline: Logistic Regression
- **Alasan:** Sederhana, interpretatif, sebagai pembanding dasar
- **Hyperparameter:** C=1.0, solver='lbfgs', max_iter=100

### 2. Model Advanced ML: Random Forest Classifier
- **Alasan:** Mampu menangkap hubungan non-linear, robust terhadap imbalance
- **Hyperparameter:** n_estimators=100, max_depth=10, random_state=42

### 3. Model Deep Learning: Multilayer Perceptron (MLP)
- **Alasan:** Mempelajari pola kompleks pada data tabular
- **Arsitektur:** Input(3) → Dense(128, ReLU) → Dropout(0.3) → Dense(64, ReLU) → Dropout(0.3) → Output(1, Sigmoid)
- **Training:** Optimizer=Adam, epochs=30, batch_size=32, early stopping

---

## 🧪 Evaluation
Metrik utama: **F1-Score** (karena data imbalance), didukung Accuracy, Precision, dan Recall

### 📈 Hasil Evaluasi
| Model | Accuracy | Precision | Recall | **F1-Score** | Training Time |
|-------|----------|-----------|--------|--------------|---------------|
| **1. Logistic Regression** | 0.75 | 0.73 | 0.76 | 0.74 | ~2 detik |
| **2. Random Forest** | 0.85 | 0.84 | 0.86 | 0.85 | ~30 detik |
| **3. MLP (Deep Learning)** | **0.89** | **0.88** | **0.90** | **0.89** | ~15 menit |

**Visualisasi:**
- Loss & Accuracy curves tersedia di folder `images/`
- Confusion matrix untuk analisis error tiap model

---

## 🏁 Kesimpulan & Insight
### 🏆 Model Terbaik: **Deep Learning (MLP)**
- Mencapai **F1-Score tertinggi (0.89)** dan unggul di semua metrik
- Mampu memodelkan hubungan non-linear kompleks antar fitur

### 💡 Insight Penting:
1. **Dari Data:** Fitur `Positive_Axillary_Nodes` merupakan prediktor paling kuat untuk survival
2. **Dari Modeling:** 
   - Model kompleks (DL) memberikan performa terbaik, tetapi butuh sumber daya lebih
   - Random Forest menawarkan trade-off yang baik antara akurasi dan kecepatan
3. **Keterbatasan:** Ukuran dataset kecil dapat membatasi kemampuan generalisasi model yang lebih kompleks

---

## 🚀 Cara Menjalankan Proyek
### Opsi 1: Google Colab (Rekomendasi)
1. Buka notebook utama: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/istya1/Habermans-Survival-Dataset/blob/main/notebooks/haberman_mlp.ipynb)
2. Klik **Runtime → Run all**

### Opsi 2: Lokal
```bash
# 1. Clone repository
git clone https://github.com/istya1/Habermans-Survival-Dataset.git
cd Habermans-Survival-Dataset

# 2. Install dependencies
pip install -r requirements.txt

# 3. Jalankan notebook
jupyter notebook notebooks/haberman_mlp.ipynb
