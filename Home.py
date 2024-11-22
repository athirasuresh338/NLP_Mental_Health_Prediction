import streamlit as st
from streamlit_option_menu import option_menu
import Chat
from streamlit_lottie import st_lottie
import requests
st.set_page_config(page_title='Mood Prediction',page_icon='💭',layout='wide')

def lottie_url(url):
    r= requests.get(url)
    if r.status_code!=200:
        return  None
    return r.json()

lottie_coding=lottie_url('https://lottie.host/b14b03a5-db99-47ff-bd74-574a50b49c6d/tCp2uv9hZf.json')

selected=option_menu(
    menu_title=None,
    options=['Home','Make Prediction','How this works?','More Information'],
    icons=['home','chat','book','info'],
    #menu_icon='cast',
    orientation='horizontal',
    default_index=0,
    styles={
        "container": { "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "left", "margin": "2px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#a38ac4"},
    }
)

if selected=='Home':
    with st.container():
        st.subheader('👋 Welcome to Your ')
        st.header('Mental Health Assistant App!🥰')
    with st.container():
        st.write(
            'Mental health is a crucial aspect of overall well-being, and taking care of it is more important than ever. Sometimes, expressing how we feel can be difficult, and knowing when to seek help can be even harder. That’s where our app comes in.'

            'Our goal is to provide a safe, supportive space where you can share your thoughts and emotions. This application is designed to assist in recognizing patterns of stress, anxiety, depression, or normal emotional states based on the words you use. With the help of advanced AI models, we aim to offer insights into your mental health based on your responses, helping you better understand your emotional state.'
        )
    with st.container():
        st.write('-----')
        left_column, right_column = st.columns(2)
        with left_column:
            st_lottie(lottie_coding, height=350, key='coding')
        with right_column:
            st.write('##')
            st.write('Why Use This App?.')
            st.write('🤝Confidential and Private: Your responses are only processed by the AI model and not stored or shared with anyone.')
            st.write('🫶Self-awareness: By interacting with the chatbot, you may discover patterns in your emotions that could be helpful in managing your mental well-being.')
            st.write('🫂Convenient and Non-intrusive: You can use this app whenever you feel like expressing your emotions, without feeling judged.')
    with st.container():
        st.write('We’re here to support you, and this application is just one step toward better understanding and managing your mental health. Take your time, and when you’re ready, we’re here to listen.😊')
        st.write('⭕Note: This application does not provide clinical diagnoses. If you are feeling severely distressed, we recommend reaching out to a healthcare professional or a therapist for personalized support.')

if selected == 'Make Prediction':
    Chat.show_chat()  # Call the chat function to initiate the chat and prediction

    if 'prediction' in st.session_state and st.session_state['prediction'] is not None:
        st.write("## Your predicted mood is:")
        st.write(f"### {st.session_state['prediction']}")

if selected=='How this works?':
    st.write('# How It Works👇')
    st.markdown('💠Our app will engage you in a conversation, asking you questions about your current feelings, thoughts, and daily experiences.')
    st.markdown('💠Based on your answers, the AI model will analyze the text and provide an indication of whether you might be feeling stressed, anxious, depressed, or emotionally balanced.')
    st.markdown("💠The insights provided are not a substitute for professional help, but they can give you a better understanding of how you're feeling and suggest if it might be beneficial to reach out for further support.")
    with st.container():
        st_lottie(lottie_coding, height=350, key='coding')

if selected=='More Information':
    st.title('Details')
    left_column, right_column = st.columns(2)
    with right_column:
        st.markdown('To Know more about the app, refer these👇')
        st.write('[🔗Click here to see Data used for training the model ](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health)')
        
    with left_column:
        st_lottie(lottie_coding, height=350, key='coding')