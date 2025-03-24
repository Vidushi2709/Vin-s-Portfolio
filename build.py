import streamlit as st  
import pandas as pd 
import random

st.set_page_config(page_title="Vin's Portfolio", page_icon="🚀", layout="wide")

#title
st.markdown(
    "<h1 style='text-align: center; color: #A020F0;'>Hey! I am Vidushi</h1>", 
    unsafe_allow_html=True
)

st.subheader("🧠 Building neural networks and hoping they don’t ghost me after a few epochs 🤖")

#image + text abt me
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True) 
    st.image("vin.jpg", width= 300)

with col2:
    st.markdown(
        "<div style='margin-top: 50px;'>"
        "<h4>Hey there! 👋</h4>"
        "<p>I'm a Machine Learning enthusiast who spends most of my time training AI models and making them smarter (or at least trying to 🤖). "
        "From building neural networks to experimenting with OpenCV, I love working on real-world AI solutions.</p>"
        "<p>When I'm not debugging, you'll find me optimizing algorithms, tackling DSA problems, or exploring new AI trends. "
        "<b>Teaching machines today, so they can do the hard work tomorrow. 🚀</b></p>"
        "</div>", 
        unsafe_allow_html=True
    )

st.divider()
st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)

st.markdown("## 🚀 SKILLs ")

col1, col2 = st.columns(2)  # Two-column layout

with col1:
   st.markdown("### 💻 **Programming**")
   st.markdown("- Python, Java, C")
   st.markdown("- Data Structures & Algorithms")

st.markdown("---")  

with col2:
    st.markdown("### 🤖 **MACHINE LEARNING AND AI**")
    st.markdown("- TensorFlow, PyTorch, OpenCV")
    st.markdown("- MediaPipe, Kalman Filters, HMM")
    st.markdown("- Model Training & Optimization")

st.markdown("<br>", unsafe_allow_html=True)
col3, col4= st.columns(2)

with col3:
    st.markdown("### 📊 **Data Science & Analysis**")
    st.markdown("- NumPy, Pandas, Matplotlib")
    st.markdown("- Data Cleaning & Preprocessing")
    st.markdown("- Statistical Analysis & Feature Engineering")

st.divider()

with col4:
    st.markdown("### 🛠️ **Development & Tools**")
    st.markdown("- Git, Streamlit, Jupyter, VS Code")
    st.markdown("- Computer Vision & Gesture Recognition")
    st.markdown("- AI Model Deployment & APIs")

st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)

st.markdown("## 🏆 Cool Projects I've Built")
            
# Image paths (Ensure images are in the same folder or provide correct paths)
img1 = "brain.jpeg"  # Replace with actual image path
img2 = "air.jpeg"  # Replace with actual image path
img3 = "rev.png"  # Replace with actual image path

# Creating a structured table layout using Markdown + Columns
projects = [
    {
        "title": "🧠 Brain Tumor Detection",
        "desc": "An AI-powered second opinion for MRI scans! This deep learning model analyzes brain scans to detect tumors with high accuracy. Built using Convolutional Neural Networks (CNN), it helps in early diagnosis, making healthcare more efficient and accessible.",
        "tech": "Pytorch, OpenCV, CNN",
        "img": img1,
    },
    {
        "title": "🎨 AirBrush: Virtual Painter",
        "desc": "Who needs a canvas when you have the air? This project lets you draw and erase with just hand gestures using OpenCV and MediaPipe. Whether you want to doodle or sketch mid-air, AirBrush transforms your movements into creative strokes!",
        "tech": "Python, OpenCV, MediaPipe, numpy",
        "img": img2,
    },
    {
        "title": "📝 Review Analyzer (NLP)",
        "desc": "Ever read a super long review and wished for a summary? This NLP-powered tool automatically classifies product and movie reviews into positive, neutral, or negative sentiments. Uses deep learning to understand customer feedback better!",
        "tech": "Python, NLTK, Transformers",
        "img": img3,
    }
]

for project in projects:
    col1, col2 = st.columns([1, 2])  

    with col1:
        st.image(project["img"], width=300)  

    with col2:
        st.markdown(f"### {project['title']}")
        st.write(project["desc"])
        st.markdown(f"**🛠️ Tech Stack:** {project['tech']}")

    st.markdown("---")  

st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)

#now the suprise element, hehe
# we will make a button and when u press it, you get random +ve affirmation

st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #A020F0;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

#affirmations
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

st.title("Sunshine in a Button 🌼")
if st.button("✨ CLICK FOR A SURPRISE ✨", key="big_button"):
    st.write(f"{random.choice(affirmations)}")

#the end cuties 