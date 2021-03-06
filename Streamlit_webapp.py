import streamlit as st
import base64
import pandas as pd
import numpy as np

st.markdown("<h1 style='text-align: center; font-size:400%; color: black;'>Harsh Harsh</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size:200%; color: black;'>Graduate Research Analyst</h1>", unsafe_allow_html=True)


clist = ['Profile', 'Resume', 'Important Links']
condition = st.sidebar.selectbox("Website Sections:",clist)

if condition == "Profile":
    st.markdown("""
        I am a gradute student at the Graduate School of Management, 
        University of California Davis, pursuing Masters of Science 
        in Business Analytics. I write articles about various topics
        in statistics and Python, in general. I am Data-driven and 
        curious analyst with three years of experience working in the 
        analytics with expertise in monitoring user behavior.
        
        You can find my articles [here](https://medium.com/@singhharsh246)
        and if you would like to know when I publish new ones, you can 
        sign up for an email alert on my Medium 
        [page](https://medium.com/@singhharsh246/subscribe).
        Below are a few articles you might find interesting...
    """)


    with st.container():
        image_col, text_col = st.columns((1,2))
        with image_col:
            st.image("https://miro.medium.com/max/1400/0*5zaQ0qT76_AD0EN6")

        with text_col:
            st.subheader("SHAP (SHapley Value exPression)")
            st.write("""Easy to interpret graphs used in calculating importance of features in ML model
                """)
            st.markdown("[Read more...](https://singhharsh246.medium.com/shap-in-python-35d0297d8285)")

    with st.container():
        image_col, text_col = st.columns((1,2))
        with image_col:
            st.image("https://miro.medium.com/max/1400/0*CuJ9XGy_WIr6FUv7")

        with text_col:
            st.subheader("Machine Learning Case Study")
            st.write("""
                A full machine learning case study from start to end. 
                I have tried to cover all the basic steps imvolved while 
                approaching a Machine Learning case study.""")
            st.markdown("[Read more...](https://singhharsh246.medium.com/machine-learning-project-4cdaaca14143)")

if condition == "Resume":

    pdf_file = 'HarshHarsh_Resume.pdf'

    with open(pdf_file,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

if condition == 'Important Links':

    with st.container():
        url = "https://media-exp1.licdn.com/dms/image/D4D35AQEDgM-fJKtnaw/profile-framedphoto-shrink_400_400/0/1635705585331?e=1644595200&v=beta&t=UdaJTdafh92BiJ1ftyhxjyIKZq-WiSbjXLZpiJnQ4vE"
        image_col, text_col = st.columns((1,2))
        with image_col:
            st.image(url)

        with text_col:
            st.subheader("Follow me on LinkedIn")
            st.write("""I post regularly about things I learn everyday.
                        """)
            st.markdown("[here...](https://www.linkedin.com/in/harshharsh/)")

    with st.container():
        url = "data:image/png;base64,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"
        image_col, text_col = st.columns((1,2))
        with image_col:
            st.image(url)

        with text_col:
            st.subheader("Github")
            st.write("""You can follow along with the website project
                        or my other projects on my github profile""")
            st.markdown("[here...](https://github.com/singhharsh246)")
