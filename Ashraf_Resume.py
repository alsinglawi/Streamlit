import streamlit as st
import pandas as pd
import numpy as np

st.markdown('''
# **Hello World!**
 
This is my first streamlit App

## Heading 2

Ashraf

### Heading 3

Medical Supply Chain Analyst

#### Heading 4

Data Scientist

##### Heading 5

& Pharmacist

###### Heading 6

MBA

---

Normal text

*Italic*

**Bold**

***Bold and Italic***

''')

st.header('Data')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')

df

df2 = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df2)

st.header('Movie Title')

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)   
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    dataframe = pd.read_csv(uploaded_file)
    st.header('Data')
    st.write(dataframe)
    
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")
   
st.header('What do you want to listen to!')
   
st.video('https://youtu.be/g27BoCH5Yxw', start_time=0)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")








