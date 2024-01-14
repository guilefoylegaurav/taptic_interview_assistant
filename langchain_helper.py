from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.8, max_tokens=-1)

def generate_rubric(job_role, skills,job_complexity, expectations, organization_type, client_facing, mission_critical, impact_of_design):
    prompt_template_jd = PromptTemplate(
        input_variables=['job_role', 'skills','job_complexity', 'expectations', 'organization_type', 'client_facing', 'mission_critical', 'impact_of_design'],
        template="""
        Pretend that you are a talent-acquisition correspondent of a reputed firm. 
        Given a job role, hiring context and skills list, you have to create a detailed job description.
        Do not mention the hiring context or its title in the resume, but include its contents implicitly in the JD.
        Can you create one for the following:
        JOB ROLE: {job_role}
        SKILLS: {skills}
        HIRING CONTEXT: 
        - Job Complexity - {job_complexity}
        - Application Performance Expectations - {expectations}
        - Organization Type - {organization_type}
        - Client Facing - {client_facing}
        - Mission Critical - {mission_critical}
        - Impact of Design - {impact_of_design}
        Use the following JD for reference:
        Job Description: Frontend Engineer (UI/UX)

        Are you passionate about crafting beautiful and intuitive web UIs? Do you thrive on turning complex datasets into engaging visualizations? Join our mission to revolutionize Dev & Ops by creating impactful UIs that empower users to explore data effortlessly.

        Responsibilities:

        Transform large datasets into visually compelling and usable UIs using React and Redux.
        Collaborate with a close-knit team to solve challenging problems and improve performance.
        Take ownership of meaningful parts of our service, making a significant impact on our projects.
        Requirements:

        Several years of experience designing and engineering UIs.
        Mastery of Javascript, HTML, and CSS with awareness of the latest frontend technologies.
        Proficiency in using design patterns for creating simple and reusable components.
        Familiarity with data structures, algorithms, profiling, and optimization.
        Visible online work or portfolio showcasing your skills.
        Appreciation for code simplicity, performance, and attention to detail.
        Desire to work in a fast-paced, high-growth startup environment.
        Bonus Points:

        Experience with D3.
        Previous work on large applications using React, Angular, Backbone, Ember, Flux, or Redux.
        Comfort with ES6 and Babel for Javascript.
        Enjoyment of writing in Python, Ruby, C++, Rust, or Go.
        If you're excited about transforming complex data into stunning UIs and want to be part of a dynamic startup environment, we invite you to apply and contribute to the future of Dev & Ops.
        """
    )

    jd_chain = LLMChain(llm=llm, prompt=prompt_template_jd, output_key='job_description')

    prompt_template_rubric = PromptTemplate(
        input_variables=['job_description'],
        template="""
        Pretend that you are an interviewer. 
        Suggest interview rubrics for the job description: 
        {job_description}
        Present your findings in the form of a spreadsheet.
        Also mention the job role in the title, for which you are creating the rubrics. 
        Also list down the top required skills for the role.
        """
    )

    rubric_chain = LLMChain(llm=llm, prompt=prompt_template_rubric, output_key="rubric")

    prompt_template_questions = PromptTemplate(
        input_variables=['job_role', 'skills', 'rubric'],
        template="""
        Pretend that you are an interviewer. 
        Provide me with a list of top interview questions for the position of method actor, for the job role {job_role}.
        Generate questions that test the candidate on the skills mentioned: {skills}.
        Please ask deep, technical, medium-hard questions pertaining to the aforementioned skills. Generate a minimum of 40 questions, all deeply technical.
        """
    )

    questions_chain = LLMChain(llm=llm, prompt=prompt_template_questions, output_key="questions")

    chain = SequentialChain(
        chains=[jd_chain, rubric_chain, questions_chain],
        input_variables=['job_role', 'skills','job_complexity', 'expectations', 'organization_type', 'client_facing', 'mission_critical', 'impact_of_design'],
        output_variables=['job_description', 'rubric', 'questions']
    )

    response = chain({'job_role': job_role, 'skills': skills,'job_complexity':job_complexity, 'expectations':expectations, 'organization_type':organization_type, 'client_facing':client_facing, 'mission_critical':mission_critical, 'impact_of_design':impact_of_design})
    return response

