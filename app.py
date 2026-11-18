import streamlit as st
import requests

# Replace this with your actual Render URL once deployed, or use your local testing URL
API_URL = "https://your-api-name.onrender.com/predict" 

st.title("Industrial Recommender System")
st.write("Enter a user or item ID to get AI-driven recommendations.")

# Create the user interface elements
user_id = st.text_input("Enter User ID", value="12345")
top_k = st.slider("Number of recommendations to return", min_value=1, max_value=20, value=5)

if st.button("Get Recommendations"):
    with st.spinner("Fetching data from the recommendation engine..."):
        try:
            # Package the user input into a JSON format expected by your API
            payload = {
                "user_id": user_id, 
                "top_k": top_k
            }
            
            # Send the request to your backend API
            response = requests.post(API_URL, json=payload)
            
            # Display the results
            if response.status_code == 200:
                data = response.json()
                st.success("Recommendations retrieved successfully!")
                
                # Streamlit automatically formats dictionaries/JSON as clean tables or drop-downs
                st.json(data)
            else:
                st.error(f"API Error {response.status_code}: {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the API. If using Render's free tier, wait 60 seconds for it to wake up and try again.")
