
import streamlit as st
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAISS index and metadata
index = faiss.read_index("quote_index.faiss")
with open("quote_metadata.pkl", "rb") as f:
    df = pickle.load(f)

# Search function
def search_quotes(query, top_k=5):
    query_vector = model.encode([query]).astype("float32")
    D, I = index.search(query_vector, top_k)
    results = []
    for idx in I[0]:
        row = df.iloc[idx]
        results.append({
            "quote": row['Quote'],
            "author": row['Author'],
            "tags": row['revised_tags']
        })
    return results

# Streamlit UI
st.title("🔍 Semantic Quote Finder")
query = st.text_input("Enter a theme, topic, or author (e.g., 'life', 'Einstein'):")

if query:
    results = search_quotes(query)
    for res in results:
        st.markdown(f"> *{res['quote']}* — **{res['author']}**")
        st.markdown(f"**Tags:** {res['tags']}")
        st.markdown("---")
