from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Portfolio", page_icon="💻", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#---LOAD ASSETS
lottie_coding = load_lottieurl("https://lottie.host/cd3f099b-ee94-4461-843b-5502215822c7/x9kCY7Cydd.json")
img_pong_unity = Image.open("images/pong_unity.png")
img_notepad_tkinter = Image.open("images/notepad_tkinter.png")
img_OBDII = Image.open("images/OBDII.png")

#Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#---Header---
with st.container():
    st.subheader("Hi! I'm Łukasz 👋")
    st.title("Computer Science Student and Enthusiast of Python, UNITY and Machine Learning")
    st.write("My passion is to explore different usages for Python and to constantly expand my knowledge in the field of programming.")
    st.write("[Feel free to check out my portfolio on github](https://github.com/lmalanczuk?tab=repositories)")

#---WHAT I DO--
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("What do i do?")
        st.write('##')
        st.write(
            """
            I'm a second year student of Computer Science at the University of Economics in Katowice. My passion is programming, application development and machine learning.
            I mainly focus on Python, gaining experience in web development, data science and machine learning. In addition, I am also developing in C# and UNITY, creating both 
            entertaining games and practical applications. My career goals are focused on becoming an experienced Python programmer, using creativity to solve problems. 
            Feel free to check out my projects below and contact me with any questions!
            
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="initial")

#--PROJECTS--
with st.container():
    st.write("---")
    st.header("My projects")
    st.write('##')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_pong_unity, caption="PONG made in UNITY")
    with text_column:
        st.subheader("PONG made in UNITY")
        st.write(
            """
            The game offers the basic features of the original PONG. You can play against a simple artificial intelligence as against a second player. \n
            The project includes the design of graphics, physics and the implementation of basic artificial intelligence based on continuous analysis of the ball's position. \n
            Repository link: [PONG]("https://github.com/lmalanczuk/PongClone")
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_notepad_tkinter, caption="Notepad created in Python")
    with text_column:
        st.subheader("Notepad created in Python")
        st.write(
            """
            A simple notepad created in Python. \n
            I used the tkinter library to implement the basic graphic design. \n
            The program allows you to open a previously saved file or create a new one, edit it and save it to a text file.  \n
            Repository link: [Notepad]("https://github.com/lmalanczuk/PongClone")
            """
        )

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_OBDII, caption="Skaner portu OBDII")
    with text_column:
        st.subheader("Skaner portu OBDII")
        st.write(
            """
            An application that lets you scan DTC errors and analyze the status of your car using the OBD II port. \n
            Programmed in python using obd and tkinter libraries. \n
            The obd library allowed me to communicate with the car, and with the tkinter library I programmed a basic \n
            graphical interface allowing the program to communicate with the user.\n
            Repository link:  [OBDII]("https://github.com/lmalanczuk/OBDReader")
            """
        )

import streamlit as st

# ---CONTACT---
with st.container():
    st.write("---")
    st.header("Contact me!")
    st.write('##')

    contact_form = """
   <form action="https://formsubmit.co/l.malanczuk03@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="Wiadomość" placeholder="Enter your message here" required></textarea>
    <button type="submit" onclick="clearForm()">Send</button>
</form>

<script>
    function clearForm() {
        document.querySelector("form").reset();
    }
</script>
    """

    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        st.empty()
