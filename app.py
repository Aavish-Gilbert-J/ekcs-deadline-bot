import streamlit as st
from streamlit_chat import message
import requests
import json



def ask_question(question):
    url = "https://412b-116-75-75-151.ngrok-free.app/chat"
    headers = {"Content-Type": "application/json"}
    data = {"question": question}
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return str(response.json()["response"])
    else:
        return {"error": "Request failed with status code {}".format(response.status_code)}


st.title("EKCS Deadline Bot" )
if 'user_input' not in st.session_state:
	st.session_state['user_input'] = []

if 'openai_response' not in st.session_state:
	st.session_state['openai_response'] = []

def get_text():
	input_text = st.text_input("Write your question here", key="input")
	return input_text

user_input = get_text()

if user_input:
	output = ask_question(user_input)
	output = output.lstrip("\n")

	# Store the output
	st.session_state.openai_response.append(user_input)
	st.session_state.user_input.append(output)

message_history = st.empty()

if st.session_state['user_input']:
	for i in range(len(st.session_state['user_input']) - 1, -1, -1):
		
		# This function displays OpenAI response
		message(st.session_state['openai_response'][i], 
				avatar_style="miniavs", is_user=True,
				key=str(i) + 'data_by_user')
		
		# This function displays user input
		message(st.session_state["user_input"][i], 
				key=str(i), avatar_style="icons")
