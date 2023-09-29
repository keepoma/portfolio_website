import streamlit as st
import pandas

summary = """
I've always had a strong passion for helping others. 
From a young age, I found immense satisfaction in extending a helping hand, which ultimately led me to pursue a career in medicine. Yet, I can’t help but wonder: “What if I could combine my other interests with my medical studies?” This question ignited a spark within me to consider exploring the intersection of medicine, technology, and neuroscience. 

During my medical career, I had the invaluable opportunity to immerse myself as a research trainee at a neuroscience laboratory for an entire year. This experience not only deepened my understanding of the field but also reinforced my belief in the potential for groundbreaking discoveries at the nexus of medicine and neuroscience.

As I near the completion of my medical studies, I find myself on the brink of an exciting opportunity. The potential to blend my diverse interests with the field of medicine presents a chance to redefine how we approach healthcare.
"""
content1 = """
Below you can find some of the apps i've built in Python. Feel free to contact me!"""

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/profile_pic.png")

with col2:
    st.title("Hi! I'm Nikita")
    st.text(summary)

st.caption(content1)
st.divider()

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.image(f"images/{index + 1}.png")
        st.markdown(row["description"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.image(f"images/{index + 1}.png")
        st.markdown(row["description"])
        st.write(f"[Source Code]({row['url']})")



