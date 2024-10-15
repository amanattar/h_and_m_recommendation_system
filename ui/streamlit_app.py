import streamlit as st
import requests

# Title of the app
st.title("H&M Personalized Fashion Recommendations")

# Input fields for Customer ID and Article ID
customer_id = st.text_input("Enter Customer ID:")
article_id = st.text_input("Enter Article ID (optional):")

# Button to get recommendations
if st.button("Get Recommendations"):
    # Make a request to the Flask API
    response = requests.post("http://127.0.0.1:5005/recommend", json={"customer_id": customer_id, "article_id": article_id})
    
    # Display the recommendations
    if response.status_code == 200:
        recommendations = response.json().get('recommendations', [])
        st.write(f"Recommended Articles for Customer {customer_id}: {recommendations}")
    else:
        st.write("Error: Could not retrieve recommendations.")
