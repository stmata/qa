import streamlit as st

# Initialize the list
question_answer_list = []

# Create or load existing
if 'qa_list' in st.session_state:
    question_answer_list = st.session_state.qa_list

# Display existing question and answer
if question_answer_list:
    st.header("Previous Questions and Answers")
    for qa_pair in question_answer_list:
        question, answer = qa_pair
        st.write(f'Question: {question}')
        st.write(f'Answer: {answer}')
        
# Grab new question
with st.form("my-form"):
    # Add input text
    new_question = st.text_input("Enter a new question")
    new_answer = st.text_input("Enter the corresponding answer")
    submit_button = st.form_submit_button("Submit")

# Add new question & answer to the list
if new_question and new_answer:
    if submit_button:
        question_answer_list.append((new_question, new_answer))
        # Persist to the session list
        st.session_state.qa_list = question_answer_list
        
# Display the latest Q&A
if new_question and new_answer:
    st.header("Latest Q & A")
    st.write(f"Question: {new_question}")
    st.write(f"Answer: {new_answer}")                          