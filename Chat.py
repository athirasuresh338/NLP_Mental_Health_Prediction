import streamlit as st
import time
import pickle
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('all')


def show_chat():
    responses = [
        'How have you been?',
        "Okay..How has your energy level been recently?",
        "Well..What is something that has been on your mind a lot lately?",
        'I see..How you want your life to be?',
        "Hmm..Have you been spending time with friends or family lately? How does it feel?",
        'Well..How do you typically spend your free time?',
        'Okk..How do you usually feel at the end of the day?',
        'Alright..What have you been doing to take care of yourself lately?',
        "That's all for now... I hope the best for you🥰"
    ]

    st.title("Let's see how your mood is👀")
    st.write('Please provide answers to the following questions💌')
    st.markdown("Let's chat")
    with st.chat_message("assistant"):
        st.write("Hello 👋")
    # Initialize session state variables
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.current_question = 0

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    # Get user input
    prompt = st.chat_input("Type something")
    if prompt:
        # Display user's message
        with st.chat_message('user'):
            st.markdown(prompt)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        # Generate response
        if st.session_state.current_question < len(responses):
            response = responses[st.session_state.current_question]
            st.session_state.current_question += 1
            with st.chat_message('assistant'):
                message_placeholder = st.empty()
                full_response = ''
                for char in response:
                    full_response += char
                    message_placeholder.markdown(full_response + "|")
                    time.sleep(0.04)  # Simulate typing
                message_placeholder.markdown(full_response)
            st.session_state.messages.append({'role': 'assistant', 'content': response})
        else:
            # Once questions are done, we can start prediction
            if 'prediction' not in st.session_state:  # Ensure we don't repeat predictions
                # Aggregate user responses
                user_responses = ' '.join(
                    [msg['content'] for msg in st.session_state.messages if msg['role'] == 'user'])

                # Check if user_responses is empty before proceeding
                if user_responses.strip():
                        # Load model and vectorizer
                        model = pickle.load(open('MHP.sav', 'rb'))
                        vector = pickle.load(open('Vector.sav', 'rb'))

                        # Preprocess input
                        user_responses = re.sub('[^a-zA-Z0-9 ]', '', user_responses)
                        sw = stopwords.words('english')
                        txt = ' '.join(
                            [word.lower() for word in nltk.word_tokenize(user_responses) if word.lower() not in sw])
                        lemma = WordNetLemmatizer()
                        txt = ' '.join([lemma.lemmatize(word, pos='v') for word in nltk.word_tokenize(txt)])

                        # Perform prediction
                        prediction = model.predict(vector.transform([txt]))[0]

                        # Map prediction to class
                        if prediction == 0:
                            st.session_state['prediction'] = 'Anxious'
                        elif prediction == 1:
                            st.session_state['prediction'] = 'Depressed'
                        elif prediction == 2:
                            st.session_state['prediction'] = 'Stressed'
                        else:
                            st.session_state['prediction'] = 'Normal'


