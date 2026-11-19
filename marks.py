import streamlit as st
st.title("Student marks of module -2")
student_detail1 = {"Karthiga":[20,40,5,65],"Dhivya":[27,38,6,77],"Anu":[18,36,5,59],"Meena":[36,38,7,81],"Logitha":[30,45,8,83]}
name = st.selectbox("Select student name" ,student_detail1.keys())
theory = student_detail1[name][0]
practical = student_detail1[name][1]
viva = student_detail1[name][2]
total_marks = student_detail1[name][3]
if total_marks >= 70:
    st.text("PASS")
else:
    st.text("FAIL")    
st.text(f"Theory marks : {theory}")
st.text(f"Practical marks : {practical}")
st.text(f"Viva marks : {viva}")
st.text(f"Total marks: {total_marks}")

