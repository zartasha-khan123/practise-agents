# # app.py


# import streamlit as st

# st.set_page_config(page_title="🏦 Bank Assistant", page_icon="🏦", layout="centered")
# st.title("🏦 Welcome to Bank Helpdesk Assistant")

# st.markdown("Ask anything related to accounts, transfers, loans, etc.")

# # Initialize chat history
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Show chat history
# for chat in st.session_state.chat_history:
#     with st.chat_message(chat["role"]):
#         st.markdown(chat["content"])

# # Input box
# user_input = st.chat_input("How can I help you today?")

# if user_input:
#     # Show user message
#     st.session_state.chat_history.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Agent processing
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             response =user_input
#             st.markdown(response)

#     st.session_state.chat_history.append({"role": "assistant", "content": response})


# app.py

import streamlit as st
from main import run_my_agent  # Import function from your main.py

st.set_page_config(page_title="🏦 Bank Assistant", page_icon="🏦", layout="centered")
st.title("🏦 Welcome to Bank Helpdesk Assistant")

st.markdown("Ask anything related to accounts, transfers, loans, etc.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show chat history
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# Input box
user_input = st.chat_input("How can I help you today?")

if user_input:
    # Show user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Agent processing
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_my_agent(user_input)
            st.markdown(response)

    st.session_state.chat_history.append({"role": "assistant", "content": response})
