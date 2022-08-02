import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import pyautogui as py
#image = Image.open('dna-logo.jpg')
#st.image(image, use_column_width=True)
st.write("""
# DNA Nucleotide Count Web App
 This app counts the nucleotide composition
 ***
 """)
sequence_input ="DNA Query \n\n\n" 
sequence = st.text_area("Sequence input", sequence_input, height=280)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)
st.write("""
***
***
""")
if st.button('Draw Chart'):
    py.keyDown("Ctrl")
    py.press("Enter")
    py.keyUp("Ctrl")
    

def DNA_count(seq):
    d=dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d


X=DNA_count(sequence)
st.subheader('Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)
st.subheader('Composition')
p=alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p=p.properties(
    width=alt.Step(80)
)
st.write(p)