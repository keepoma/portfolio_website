import streamlit as st

summary = """
I've always had a strong passion for helping others. 
From a young age, I found immense satisfaction in extending a helping hand, which ultimately led me to pursue a career in medicine. Yet, I can’t help but wonder: “What if I could combine my other interests with my medical studies?” This question ignited a spark within me to consider exploring the intersection of medicine, technology, and neuroscience. 

During my medical career, I had the invaluable opportunity to immerse myself as a research trainee at a neuroscience laboratory for an entire year. This experience not only deepened my understanding of the field but also reinforced my belief in the potential for groundbreaking discoveries at the nexus of medicine and neuroscience.

As I near the completion of my medical studies, I find myself on the brink of an exciting opportunity. The potential to blend my diverse interests with the field of medicine presents a chance to redefine how we approach healthcare.
"""

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/profile_pic.png")

with col2:
    st.title("Hi! I'm Nikita")
    st.text(summary)