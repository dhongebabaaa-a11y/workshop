import streamlit as st
st.title("personal details")
name = st.text_input("Enter name")
if name :st.write(f" hello , {name}!")
num=st.slider("pick number", 0,100)
clicked =st.button("calculate")
agree =st.checkbox("I agree to the terms")
fruit =st.selectbox("Favourite fruit",["Apple","Banana","Mango"])
coll, coll2=st.columns(2)
with coll: st.write("Left side")
with coll:
    st.write("left side")
with coll2:
    st.write("Right side")