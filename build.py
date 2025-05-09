import streamlit as st  
import pandas as pd 
import random
import base64
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()


st.set_page_config(page_title="Vin's Portfolio", page_icon="🚀", layout="wide")

# Add custom CSS for futuristic vibes
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap');
        body {
            font-family: 'Orbitron', sans-serif;
        }
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Orbitron', sans-serif;
        }
        .stButton > button:first-child {
            background-color: #FF61A6;
            color: white;
            font-size: 18px;
            font-family: 'Orbitron', sans-serif;
            border-radius: 10px;
            padding: 10px 20px;
            box-shadow: 0px 5px 20px rgba(255, 97, 166, 0.5);
            transition: 0.3s;
        }
        .stButton > button:first-child:hover {
            background-color: #FF30A1;
            box-shadow: 0px 5px 30px rgba(255, 97, 166, 0.7);
        }
        .stApp {
            background-color: #282c34;
            color: #ffffff;
        }
        h1 {
            color: #FF61A6;
        }
        h2, h3, h4 {
            color: #00D4FF;
        }
        p, li {
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

#title
st.markdown(
    "<h1 style='text-align: center;'>Hey! I am Vidushi 🚀</h1>", 
    unsafe_allow_html=True
)
def get_base64_of_bin_file(bin_file_path):
    with open(bin_file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(image_path):
    base64_img = get_base64_of_bin_file(image_path)
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{base64_img}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
# Add custom background with a futuristic theme
set_background("backie.jpg")  # Update your background image path

st.markdown(
    "<h2 style='font-size: 18px; text-align: center;'>🧠 Building neural networks and hoping they don’t ghost me after a few epochs 🤖</h2>", 
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 2])

with col1:
    st.image("vin.jpg", width= 300)

with col2:
    st.markdown("<div style='margin-top: 50px;'>"
                "<h4>Hey there! 👋</h4>"
                "<p>I'm a Machine Learning enthusiast who spends most of my time training AI models and making them smarter (or at least trying to 🤖). "
                "From building neural networks to experimenting with OpenCV, I love working on real-world AI solutions.</p>"
                "<p>When I'm not debugging, you'll find me optimizing algorithms, tackling DSA problems, or exploring new AI trends. "
                "<b>Teaching machines today, so they can do the hard work tomorrow. 🚀</b></p>"
                "</div>", unsafe_allow_html=True
                )

st.divider()

# Skills section with futuristic font style
st.markdown("<h2 style='text-align: center; font-size: 40px;'>SKILLS</h2>", unsafe_allow_html=True)

# Skills layout
col1, col2 = st.columns(2)
col1, col2 = st.columns(2)  # Two-column layout

with col1:
   st.markdown("### 💻 **Programming**")
   st.markdown("- Python, Java, C")
   st.markdown("- Data Structures & Algorithms")

st.markdown("---")  

with col2:
    st.markdown("### 🤖 **MACHINE LEARNING AND AI**")
    st.markdown("- TensorFlow, PyTorch, OpenCV")
    st.markdown("- Transformers, Fine-tuning LLMs")
    st.markdown("- Model Training & Optimization")

st.markdown("<br>", unsafe_allow_html=True)

col3, col4= st.columns(2)

with col3:
    st.markdown("### 📊 **Data Science & Analysis**")
    st.markdown("- NumPy, Pandas, Matplotlib")
    st.markdown("- Data Cleaning & Preprocessing")
    st.markdown("- Statistical Analysis & Feature Engineering")


with col4:
    st.markdown("### 🛠️ **Development & Tools**")
    st.markdown("- Git, Streamlit, Jupyter, VS Code")
    st.markdown("- Computer Vision & Gesture Recognition")
    st.markdown("- AI Model Deployment & APIs")
st.divider()

# Projects section with futuristic style
st.markdown("<h2 style='text-align: center; font-size: 40px;'>PROJECTS</h2>", unsafe_allow_html=True)

# Projects layout
projects = [
        {
        "title": "🗣️ Debatable: Debate with LLMs",
        "desc": "Debatable is a fun, interactive project where you debate with LLMs powered by the Gemini model. Choose from various debate styles, face off against the AI, and let the built-in judge decide the winner. It’s an engaging mix of entertainment and learning—where every argument counts!",
        "tech": "Gemini Model, Natural Language Processing (NLP)",
        "img": "deb.jpg",
    },

    {
        "title": "🌍 German to English Translator (Transformer)",
        "desc": "German to English Translator is an end-to-end implementation of the Transformer model from the *Attention Is All You Need* paper. Built with PyTorch and Hugging Face, it showcases self-attention-based translation from German to English with high accuracy.",
        "tech": "PyTorch, Hugging Face Transformers, Attention Is All You Need",
        "img": "tra.jpg",  
},
{
        "title": "🎨 AirBrush: Virtual Painter",
        "desc": "Who needs a canvas when you have the air? This project lets you draw and erase with just hand gestures using OpenCV and MediaPipe. Whether you want to doodle or sketch mid-air, AirBrush transforms your movements into creative strokes!",
        "tech": "Python, OpenCV, MediaPipe, numpy",
        "img": "air.jpeg",
    }

]

for project in projects:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(project["img"], width=300)

    with col2:
        st.markdown(f"### {project['title']}")
        st.write(project["desc"])
        st.markdown(f"🛠️ Tech Stack: {project['tech']}")

    st.markdown("---")

def send_email(subject, body, to):
    # Replace these with your Gmail credentials
    sender = os.getenv('GMAIL_USER')
    password = os.getenv('GMAIL_PASSWORD')

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

# Contact Form UI
st.markdown("<h2 style='text-align: center; font-size: 40px;'>📬 CONTACT ME</h2>", unsafe_allow_html=True)

with st.form(key='contact_form'):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    submit_button = st.form_submit_button(label='Send Message')

    if submit_button:
        subject = f"New message from {name}"
        body = f"From: {name} <{email}>\n\nMessage:\n{message}"

        if send_email(subject, body, "vidushianand09@gmail.com"):  
            st.success("Your message was sent successfully!")
        else:
            st.error("Failed to send your message. Please try again later.")

# Footer contact info
st.markdown("""
<hr style="margin-top: 30px; margin-bottom: 20px;">

<div style='text-align: center; font-size: 18px'>
    <p>Feel free to reach out for collaborations, projects, or just to say hello! 😊</p>
    📧 <a href="mailto:vidushianand09@gmail.com">vidushianand09@gmail.com</a> <br>
    🔗 <a href="https://www.linkedin.com/in/vidushi-anand-49420928a/" target="_blank">LinkedIn</a> <br>
    🐙 <a href="https://github.com/Vidushi2709" target="_blank">GitHub</a>
</div>
""", unsafe_allow_html=True)


affirmations = [
    "🌟 You are capable of amazing things! Keep going",
    "🚀 Keep pushing forward – Today might be tough but tomorrow will be good!!",
    "💡 Your ideas matter, and so do you! I believe in you",
    "🔥 Stay strong, stay focused, and keep going! You got this gurl",
    "🌈 Believe in yourself – you're doing great!",
    "✨ Every challenge is an opportunity to grow!",
    "💪 You have everything it takes to succeed! Just trust the process",
    "🌱 Small progress is still progress – keep going!",
    "💖 You are enough, not for someone else but for yourself",
    "🎯 Your hard work will pay off – trust the process!",
    "⚡ You radiate confidence and strength!",
    "🌞 Today is a fresh start, make the most of it!",
    "🎶 Your energy is contagious – spread the good vibes!",
    "📚 Every mistake is a lesson in disguise!",
    "🦁 You are braver than you think, stronger than you feel!",
    "🌻 You bring positivity wherever you go!",
    "🌞 If you can't trust yourself right now, I'll trust you for the time being",
    "💖 You are the most beautiful person inside and outside, Don't let small things hinder you"
    "✨ It's just a bad day, not a bad life",
    "🌈 The world is funny, peculiar and bizzare, no one cares who share this baazar, with me, with you",
    "🌱 People will come and go, You matter in the end. Don't let their small thoughts hidner your big ideas",
    "🌞Sunshine, you are my sunshine, you make my happy when skies are blueeee",
    "You’re a firework, let your colors burst!🎆",
    "You shine like a golden sunset, don’t let anyone dim your light! 🌅",
    "You got that James Dean daydream confidence – own it! 😎",
    "You are not just surviving, you are thriving! 🌟",
    "You are the 1, and don’t let anyone tell you otherwise!🎆"  
]

st.markdown("<br><br>", unsafe_allow_html=True)

# Adding space before the "Click Me for Surprise" button
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Adds more space

# Custom styled button with larger size
st.markdown("""
    <style>
    .big-button {
        width: 300px;  /* Make the button wider */
        height: 50px;  /* Make the button taller */
        font-size: 20px;  /* Adjust the text size */
        background-color: #4CAF50;  /* Button color */
        color: white;  /* Text color */
        border: none;  /* Remove border */
        border-radius: 10px;  /* Rounded corners */
    }
    </style>
""", unsafe_allow_html=True)

# Creating the button with the custom style
if st.button("SUNSHINE BUTTON", key="surprise_button", use_container_width=True):
    st.write(f"{random.choice(affirmations)}")

