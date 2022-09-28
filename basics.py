import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="new webpage",page_icon=':tada:',layout='wide')

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
#header

with st.container():
    st.subheader('hi,I am krishna vamshi :wave:')
    st.title('I am machine learnirng enthusiast')
    st.write('I am passioante about ml and dl')

lottie_coding=load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_2glqweqs.json")


with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header('what I do')
        st.write('##')
        st.write(
            """bas"""
        )

with right_column:
    st_lottie(lottie_coding,height=300,key='coding')