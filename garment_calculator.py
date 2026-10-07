import streamlit as st

def calculate_productive_time(a,b,c,d):
 total_work_minutes=(a*b)
 theoretical_minutes=total_work_minutes / c
 actual_minutes=theoretical_minutes / (d / 100)
 hours=actual_minutes /60
 return hours

st.title("GARMENTS PRODUCT TIME PRIDICTOR")
quantity=st.number_input("Quantity: ", min_value=0)
minutes=st.number_input("minutes per garment: ", min_value=0.1)
workers=st.number_input("workers: ", min_value=1)
efficiency=st.number_input("efficiency: ", min_value=0.1)


if st.button("calculate production time"):
    calculated_hours=calculate_productive_time(quantity,minutes,workers,efficiency)
    st.write("Estimated production time:", round(calculated_hours,2))