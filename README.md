# 🎬 Movie Review Sentiment Analyzer

![Streamlit](https://img.shields.io/badge/Streamlit-1.39.0-ff4b4b?style=flat-square&logo=streamlit)  
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.17.0-orange?style=flat-square&logo=tensorflow)  
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)  
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)



A **Deep Learning web application** that predicts whether a movie review expresses **Positive or Negative sentiment**.

The application is built using **Streamlit** and powered by an **LSTM Neural Network trained on the IMDB dataset**.

The app allows users to enter movie reviews and receive **real-time sentiment predictions with confidence scores**.

---

# 🚀 Live Deployment (AWS)

The application is deployed on **AWS EC2** using a Streamlit server.

Access the live app:

http://YOUR_AWS_PUBLIC_IP:8501

---

# ✨ Features

• Predict sentiment of movie reviews (Positive / Negative)
• Confidence score for each prediction
• Example reviews for quick testing
• Interactive UI built with Streamlit
• Real-time predictions using a trained LSTM model
• Analysis history tracking

---

# 🧠 Model Details

Model Type: **LSTM Neural Network**

Framework: **TensorFlow / Keras**

Dataset: **IMDB Movie Reviews Dataset**

Training Process:

Text Preprocessing
↓
Tokenization
↓
Sequence Padding
↓
LSTM Neural Network
↓
Sentiment Prediction

---

# 🛠 Tech Stack

Python
Streamlit
TensorFlow / Keras
NumPy
Pickle
Streamlit Option Menu

---

# 📂 Project Structure

movie-review-sentiment-analyzer

app.py
model.h5
tokenizer.pkl
requirements.txt
README.md

---

# ⚙️ Run Locally

Clone the repository

git clone https://github.com/yourusername/movie-review-sentiment-analyzer.git

Navigate to the project folder

cd movie-review-sentiment-analyzer

Install dependencies

pip install -r requirements.txt

Run the Streamlit app

streamlit run app.py

Open the application

http://localhost:8501

---

# ☁️ AWS Deployment Process

The application is deployed on **AWS EC2**.

Deployment workflow:

User Browser
↓
AWS EC2 Server
↓
Streamlit Web Application
↓
TensorFlow LSTM Model

Steps used for deployment:

1. Launch AWS EC2 instance (Ubuntu)
2. Install Python and pip
3. Clone the GitHub repository
4. Install project dependencies
5. Run the Streamlit server

Command used:

streamlit run app.py --server.address 0.0.0.0 --server.port 8501

Security group configured to allow:

Port 22 (SSH)
Port 8501 (Streamlit)

---

# 📊 Example Prediction

Input:

"This movie was amazing and the acting was fantastic."

Output:

Sentiment: Positive
Confidence: 93.41%

---

# 🔮 Future Improvements

• Deploy with Docker
• Add BERT based sentiment model
• Improve UI with custom components
• Store prediction history in a database

---

## 📬 Contact

For questions or feedback, reach out to [your-email@example.com](mailto:your-email@example.com) or open an issue on GitHub.

---

**Happy Analyzing! 🎥**
