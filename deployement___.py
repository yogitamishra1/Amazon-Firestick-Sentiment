#packages
import streamlit as st
import pandas as pd
import requests
import spacy
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
from spacytextblob.spacytextblob import SpacyTextBlob

nlp=spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

st.set_page_config(page_title="Hello om!",layout="wide",initial_sidebar_state="collapsed")

col1, col2, col3 = st.columns(3)
st.title("Review Sentiment Analyzer")
    #st.title("Review Sentiment Analyzer")
with col2:
    st.image("https://miro.medium.com/max/687/1*FRd4BsrZ2VxKLbvVYJQC6w.png")

#def load_lottieurl(url:str):
    #r=requests.get(url)
    #if r.status_code !=200:
        #return None
    #return r.json()
#lottie_= load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_cYWJg2.json")
#https://assets6.lottiefiles.com/private_files/lf30_pe36bsil.json
#st_lottie(lottie_,key="emo",height=100,width=400)

st.sidebar.subheader("Sentiment Analysis By Group 6th")
st.sidebar.subheader("Our Mentor:")
st.sidebar.info("Varun Vennelaganti")
st.sidebar.subheader("Group Members:")
st.sidebar.info("Omkar Bhagwat")
st.sidebar.info("Chaitravi Angane")
st.sidebar.info("Amrut Vishwaroop")
st.sidebar.info("Yogita Sharma")
st.sidebar.info("Akarsh Bhasi")
st.sidebar.info("Nitin Sharma")
st.sidebar.markdown("""
   <span style='color:blue;'>
   Made by India ??</span>""",
   unsafe_allow_html=True)

def sentiment_analyzer(Review):
    
    docx= nlp(Review)
    sentiment=docx._.polarity
    return sentiment
   
def main():
    
    #st.subheader("Let's check the Sentiment")
    
    #Sentiment_Analysis
    if st.checkbox("Type Review"):
        data=pd.read_csv("/Users/om/Desktop/NLP/Firestick.csv")

        if st.checkbox("Preview Data"):
            st.dataframe(data=data, width=False, height=True)
            
 
        # enter reviews
        #title = st.text_input('title')
        #st.write(title)
        
        review = st.text_area("Enter the Review")
        f=st.file_uploader("Upload file",accept_multiple_files=True)
        if f is not None:
            df=[pd.read_csv(f) for f in f]

        components.html("""
        <script>
        const elements =window.parent.document.querySelectorAll('.stButton > button')
        elements[0].style.backgroundColor = 'skyblue'
        </script>""",height=0,width=0)
        if st.button("Run"):
            #st.header("Result")
            nlp_result= sentiment_analyzer(review)
            if nlp_result > 0:
                st.success("The Review is Positive ??")
                st.button("Clear")
                components.html("""
        <script>
        const elements =window.parent.document.querySelectorAll('.stButton > button'{border-redius 90%;})
        elements[1].style.backgroundColor = 'brown'
        </script>""",height=0,width=0)
            else:
                st.markdown("""
   <span style='color:red;'>
   The Review is Negative ?? </span>""",
   unsafe_allow_html=True)                
                st.button("Clear")
               
if __name__ == '__main__':
    main()

