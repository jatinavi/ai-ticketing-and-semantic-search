# 🧠  AI Internship Projects – Jatin Balchandani

This repository contains both AI internship tasks completed for the Vijayi WFH Internship (May–June 2025).  
Each task showcases real-world applications of Machine Learning and NLP, using popular frameworks like Scikit-learn, FAISS, Gradio, and Streamlit.

---

## 📁 Projects Overview

### 🎫 Task 1: Ticket Classifier (ML Pipeline + Gradio)
An AI-based support ticket classification system that predicts both **issue type** and **urgency** level.

#### ✅ Key Features:
- Data cleaning, preprocessing, and vectorization
- Trained a `RandomForestClassifier` on cleaned text
- Achieved 94–100% accuracy on issue type classification
- Visualized performance using confusion matrix and classification report
- Built an interactive **Gradio app** for real-time ticket analysis

#### 📂 Files:
- `ticket_classifier.ipynb`
- `ai_dev_assignment_tickets_complex_1000.xlsx`
- `demo_video_task1.mp4` *(optional)*

---

### 🔍 Task 2: Semantic Quote Finder (RAG-style + Streamlit)
A semantic quote search engine built using **sentence-transformers** and **FAISS** for vector similarity, wrapped in a **Streamlit UI**.

#### ✅ Key Features:
- Used `all-MiniLM-L6-v2` for sentence embeddings
- Indexed over 29,000 quotes using FAISS
- Supported free-text queries like “funny quote about life”
- Deployed locally via Streamlit with full UI
- Capable of fast, meaningful semantic search with author and tags

#### 📂 Files:
- `app.py`
- `quotes.csv`
- `quote_index.faiss`
- `quote_metadata.pkl`
- `demo_video_task2.mp4` *(optional)*

---

## 🛠️ Tech Stack
- Python, Scikit-learn, Pandas, NumPy
- FAISS, Sentence-Transformers
- Gradio, Streamlit
- Matplotlib / Seaborn (for visualizations)

---

## 🚀 How to Run Locally

### Task 1: Gradio Ticket Classifier
```bash
pip install gradio scikit-learn pandas
