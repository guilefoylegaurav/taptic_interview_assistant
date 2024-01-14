import streamlit as st
import langchain_helper

st.title("Taptic Interview Assistant")

st.subheader("Job Role")
job_role = st.text_input("Specify job role here (ex: Backend Developer)")

st.subheader("Hiring Context")
job_complexity = st.selectbox("Job Complexity:", ["Low", "Medium", "High"])
expectations = st.selectbox("Performance Expectations:", ["Low", "Medium", "High"])
organization_type = st.selectbox("Organization Type:", ["SI", "GCC", "Product", "Startup"])
client_facing = st.selectbox("Is the role client facing?:", ["Yes", "No"])
mission_critical = st.selectbox("Mission critical/Hiring for immediate joiners?:", ["Yes", "No"])
impact_of_design = st.selectbox("Impact of design:", ["Low", "Medium", "High"])

st.subheader("YOE")
yoe = st.number_input("Specify desired YOE (ex: 0-3 years)", step=1, format="%d")

st.subheader("Skills")
skills = st.text_input("Specify list of desired skills - you can seperate the skill items using commas")


generate_rubric = st.button("Generate rubric")

# Check if the button is clicked
if generate_rubric:
    if (job_role and yoe and skills):
        response = langchain_helper.generate_rubric(job_role, skills,job_complexity, expectations, organization_type, client_facing, mission_critical, impact_of_design)
        print(response)
        st.header('JD')
        st.write(response['job_description'])
        st.header('Interview Rubrics')
        st.write(response['rubric'])
        st.header('Sample Interview Questions')
        st.write(response['questions'])
    else:
        st.write("Please do not leave any field empty. All fields are mandatory.")


