import streamlit as st
import requests

# 1. Update this to your actual live Render URL (do not add a slash at the end)
API_BASE_URL = "https://your-api-name.onrender.com" 

st.title("Industrial Recommender System")
st.write("Enter a user ID to get AI-driven recommendations.")

user_id = st.text_input("Enter User ID", value="1256")
top_k = st.slider("Number of recommendations to return", min_value=1, max_value=20, value=5)

if st.button("Get Recommendations"):
    with st.spinner("Fetching data from the recommendation engine..."):
        try:
            # 2. Construct the exact URL expected by your FastAPI router
            # Format: https://your-url.onrender.com/recommend/1256?top_k=5
            request_url = f"{API_BASE_URL}/recommend/{user_id}?top_k={top_k}"
            
            # 3. Send a GET request (matching @app.get in your backend)
            response = requests.get(request_url)
            
            if response.status_code == 200:
                data = response.json()
                st.success("Recommendations retrieved successfully!")
                
                # Display the 'recommendations' array from the backend response
                st.json(data["recommendations"])
            else:
                st.error(f"API Error {response.status_code}: {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the API. If using Render's free tier, wait 60 seconds for it to wake up and try again.")
