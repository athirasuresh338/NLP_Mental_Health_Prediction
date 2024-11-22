# 🧠 **Mental Health Assistant App** 💭

This project aims to predict mental health conditions such as **Anxiety**, **Depression**, **Stress**, or a **Normal** state based on textual inputs. By combining **Natural Language Processing (NLP)** and **Machine Learning (ML)**, the app provides real-time mood analysis. The solution includes a user-friendly **Streamlit-based GUI** that allows seamless interaction and insightful predictions.

---

## 🔍 **Key Features**
- **Text-Based Mood Prediction**: Leverages ML models trained on labeled mental health data.
- **Streamlit Integration**: A modern, interactive interface with dynamic animations and real-time response.
- **AI-Powered Chatbot**: Engages users in conversation to assess their mental state.
- **Multi-Classifier Approach**: Includes models like **Naive Bayes**, **Random Forest**, and **XGBoost**.
- **Custom Model Deployment**: Saved models allow quick predictions in a local or web-deployed app.

---

## 📚 **Dataset Information**
- Dataset contains records for various mental health categories: **Normal**, **Depression**, **Anxiety**, **Stress**, etc.
- Data preprocessing steps included:
  - **Text cleaning**: Removing special characters.
  - **Stopword Removal**: Eliminating redundant words.
  - **Lemmatization**: Reducing words to their base forms.
  - **Class Balancing**: Ensured balanced representation using under-sampling.

---

## 🛠️ **Tech Stack**
- **Languages**: Python
- **Libraries**: 
  - NLP: `nltk`
  - ML: `scikit-learn`, `xgboost`, `imblearn`
  - Data Processing: `pandas`, `matplotlib`
  - GUI: `Streamlit`, `streamlit_option_menu`, `streamlit_lottie`
- **Deployment**: Models saved as `.sav` files using `pickle`.

---

## 🚀 **How It Works**

### 1️⃣ **Data Preprocessing**
- Load and clean the dataset to make it suitable for ML model training.
- Convert textual data into vectors using **TF-IDF Vectorizer**.
- Handle class imbalance with **RandomUnderSampler**.
- Split data into **train** and **test sets** for model evaluation.

### 2️⃣ **Model Training**
- Implemented six classifiers:
  - **Multinomial Naive Bayes**
  - **Decision Tree**
  - **Random Forest**
  - **Gradient Boosting**
  - **AdaBoost**
  - **XGBoost**
- Fine-tuned the **XGBoost** model using **RandomizedSearchCV** for hyperparameter optimization.

### 3️⃣ **Prediction**
- New textual inputs are preprocessed and fed into the trained model for mood classification.
- The GUI displays predictions like:
  - **#Anxious**
  - **#Depressed**
  - **#Stressed**
  - **#Normal**

---

## 💻 **Streamlit GUI**
The **Streamlit-based web app** provides:
1. **Home Screen**: Introduction and app overview.
2. **Make Prediction**: Chat-based interaction to collect user input and predict mental state.
3. **How It Works**: Explains the process in a user-friendly way.
4. **More Information**: Links to dataset and additional details.

---

## 📊 **Visualization**
- Class distribution is visualized using histograms to analyze the dataset.
- Chat animation uses **Lottie files** for engaging user interaction.

---

## ⚠️ **Disclaimer**
This app provides **non-clinical insights** and is not a substitute for professional mental health advice. If you’re experiencing severe distress, please consult a healthcare provider. 

---

### 📥 **Get Started**
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

---