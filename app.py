import streamlit as st
import nltk
from PIL import Image
import random
import datetime
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

st.set_page_config(page_title="🩺 HealthCare Assistant Chatbot", page_icon="🏥", layout="wide")
    

# Hide Streamlit branding
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Initialize AI model for text generation
chatbot_model = pipeline("text-generation", model="distilgpt2")

def main():
    
    st.markdown(
        """
        <style>
        body {background-color: #FFFFFF; color: #000000;}
        .stApp {background-color: #FFFFFF; color: #000000;}
        .stTextInput>div>div>input {color: #000000;}
        .stButton>button {background-color: #007BFF; color: #FFFFFF; border-radius: 10px;}
        .stHeader {color: #000000;}
        .stSidebar {background-color: #F8F9FA; color: #000000;}
        .stRadio label {color: #000000 !important;}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Sidebar navigation menu
    st.sidebar.title("🔹 Navigation")
    page = st.sidebar.radio("Go to", ["💬 Chatbot", "❓ FAQ", "📞 Contact", "💡 Health Tips", "📅 Appointment Scheduler"])
    
    # Route user to the selected page
    if page == "💬 Chatbot":
        chatbot_page()
    elif page == "❓ FAQ":
        faq_page()
    elif page == "📞 Contact":
        contact_page()
    elif page == "💡 Health Tips":
        health_tips_page()
    elif page == "📅 Appointment Scheduler":
        appointment_scheduler()

def chatbot_page():
    st.markdown("""
        <h2 style='text-align: center;'>💬 Healthcare Assistant Chatbot</h2>
        <p style='text-align: center;'>Ask me anything about your health! 🏥</p>
    """, unsafe_allow_html=True)
    
    col1 = st.columns([1])[0]
    with col1:
        user_input = st.text_input("📝 Type your question:")
    
    if st.button("Search 🔍"):
        with st.spinner("⏳ Processing your request..."):
            response = healthcare_chatbot(user_input)
            st.success(response)

def healthcare_chatbot(user_input):
    responses = {
        "symptom": "🩺 Please consult a doctor for accurate advice.",
        "appointment": "📅 Would you like to schedule an appointment with the doctor?",
        "medication": "💊 It's important to take prescribed medicines regularly. If you have concerns, consult your doctor.",
    }
    for keyword, response in responses.items():
        if keyword in user_input.lower():
            return response
    ai_response = chatbot_model(user_input, max_length=500, num_return_sequences=1)
    return ai_response[0]['generated_text']

def faq_page():
    st.header("❓ Common Symptoms and Conditions")
    st.write("""
    - 🤒 Fever
    - 🤧 Cough
    - 🤕 Headache
    - 😮‍💨 Shortness of breath
    - 🤢 Nausea and vomiting
    - 🤒 Chills and body aches
    - 🤯 Dizziness and fatigue
    - 💔 High blood pressure
    - 🍽️ Eating disorders
    - 🤰 Pregnancy-related concerns
    
    **General FAQs:**
    - **What should I do if I have a fever?** Stay hydrated, rest, and take fever-reducing medication if necessary. Consult a doctor if fever persists.
    - **How can I improve my immunity?** Eat a balanced diet, exercise, get enough sleep, and reduce stress.
    - **When should I see a doctor for a cough?** If your cough lasts more than 2 weeks, produces blood, or is accompanied by shortness of breath, see a doctor immediately.
    """)

def contact_page():
    st.header("📞 Emergency Contacts")
    st.write("""
    - 🚒 *Fire Department*: 101
    - 🚔 *Police*: 100
    - 🚑 *Ambulance*: 102
    - 🏥 *Nearest Hospital*: Check your local directory for emergency services.
    - 💊 *Poison Control*: 1800-222-1222 (For immediate poisoning-related help)
    """)

def health_tips_page():
    st.header("💡 Daily Health Tips")
    tips = [
        "💧 Stay hydrated – drink at least 8 glasses of water daily.",
        "😴 Get at least 7-8 hours of sleep every night.",
        "🏃‍♂️ Exercise regularly – at least 30 minutes of activity a day.",
        "🥗 Eat a balanced diet rich in fruits and vegetables.",
        "🧘‍♂️ Practice mindfulness or meditation to reduce stress.",
        "👐 Wash your hands frequently to prevent infections.",
        "📵 Reduce screen time before bed to improve sleep quality.",
        "🚶‍♀️ Take short breaks and stretch during long working hours.",
        "🍏 Avoid excessive sugar intake for better overall health.",
        "🚭 Quit smoking and limit alcohol consumption for a healthier life.",
    ]
    if "tip_index" not in st.session_state:
        st.session_state.tip_index = 0  # Default first tip

    st.info(tips[st.session_state.tip_index])

    if st.button("🔄 Show Another Tip"):
        st.session_state.tip_index = (st.session_state.tip_index + 1) % len(tips)

def appointment_scheduler():
    st.header("📅 Schedule an Appointment")
    name = st.text_input("👤 Enter your name:")
    date = st.date_input("📆 Select appointment date:", min_value=datetime.date.today())
    time = st.time_input("⏰ Select appointment time:")
    
    if st.button("📌 Schedule Appointment"):
        st.success(f"✅ Appointment booked for {name} on {date} at {time}.")

if __name__ == "__main__":
    main()
