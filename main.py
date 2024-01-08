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

#Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#---Header---
with st.container():
    st.subheader("Cześć! Jestem Łukasz 👋")
    st.title("Student Informatyki, Programista Pythona, Twórca Aplikacji .NET i Gier w UNITY. ")
    st.write("Moją pasją jest eksplorowanie różnych zastosowań dla Pythona oraz nieustanne poszerzanie swojej wiedzy w obszarze programowania.")
    st.write("[Zapraszam do zapoznania się z moim portfolio na githubie](https://github.com/lmalanczuk?tab=repositories)")

#---WHAT I DO--
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Co robię?")
        st.write('##')
        st.write(
            """
            Jestem studentem drugiego roku Informatyki na Uniwersytecie Ekonomicznym w Katowicach i jestem zafascynowany światem programowania 
            oraz tworzeniem gier i aplikacji. Moja pasja do programowania rozpoczęła się od Pythona, który jest moim głównym językiem programowania. 
            Aktywnie rozwijam się w programowaniu w Pythonie, zdobywając doświadczenie w różnych dziedzinach, takich jak web development, data science czy machine learning.
            Jednak nie ograniczam się tylko do Pythona. Chcę poszerzać swoje umiejętności, dlatego również rozwijam się w C# i UNITY.
            Tworzenie gier i aplikacji za pomocą tych technologii daje mi możliwość wykorzystania swojej kreatywności i umiejętności programistycznych. 
            Moje projekty obejmują zarówno rozrywkowe gry, które dostarczają radość i emocje, jak i praktyczne aplikacje, które mogą być przydatne w codziennym życiu.
        
        Zapraszam do zapoznania się z moimi projektami i do kontaktu, jeśli jesteś zainteresowany współpracą lub masz pytania
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=400, key="initial")

#--PROJECTS--
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write('##')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_pong_unity, caption="Pong w Unity")
    with text_column:
        st.subheader("PONG stworzony w UNITY")
        st.write(
            """
            Pierwsza gra stworzona przeze mnie w UNITY. Jest to klasyczny PONG, w którym można zagrać z komputerem lub z drugą osobą. \n
            Link do repozytorium: [PONG]("https://github.com/lmalanczuk/PongClone")
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_notepad_tkinter, caption="Notatnik w Pythonie")
    with text_column:
        st.subheader("Notatnik stworzony w Pythonie")
        st.write(
            """
            Notatnik stworzony w Pythonie z wykorzystaniem biblioteki Tkinter. \n
            Link do repozytorium: [Notepad]("https://github.com/lmalanczuk/PongClone")
            """
        )

import streamlit as st

# ---CONTACT---
with st.container():
    st.write("---")
    st.header("Skontaktuj się ze mną!")
    st.write('##')

    contact_form = """
    <form action="https://formsubmit.co/l.malanczuk03@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Twoje imie" required>
        <input type="email" name="email" placeholder="Twoj adres email" required>
        <textarea name="Wiadomość" placeholder="Tutaj wpisz swoją wiadomość" required></textarea>
        <button type="submit">Wyślij</button>
    </form>
    """

    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        st.empty()
