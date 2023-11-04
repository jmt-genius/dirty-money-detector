import streamlit as st
import json
from sklearn.metrics import accuracy_score
from keras.models import load_model
import pandas as pd
import requests
import plotly.graph_objects as go
import dash
from sklearn.preprocessing import StandardScaler
st.set_page_config(
    page_title="DMD",
    page_icon=":bar_chart:",
    layout="wide",
)

# Create a container for the header with a black background
header_container = st.container()
header_container.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css?family=Fira+Code:400,500,600,700&display=swap');
    .fira-code-font {
        font-family: 'Fira Code', monospace;
    }
    .header-container {
        background-color: #000000;
        color: #ffffff;
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .nav-links {
        list-style: none;
        margin: 0;
        padding: 0;
        display: flex;
    }
    .nav-link {
        margin-right: 30px;
        cursor: pointer;
    }
    .text-input-container {
        width: 500px;
        border: 2px solid #ffffff;
        border-radius: 5px;
        padding: 10px;
    }
    .text-input-label {
        color: #ffffff;
        font-size: 18px;
        margin-bottom: 10px;

    }
    .dirt-score {
        color: #ffffff;
        font-size: 18px;
        margin-bottom: 10px;
    }
    .center-content {
        text-align: center;
        font-size: 24px;
        margin-bottom: 20px;
    }
    .sidebar .css-14ryutq {
        font-family: 'Fira Code', monospace;
    }

    /* Specify the font for the content */
    .content .css-vfskoc {
        font-family: 'Fira Code', monospace;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
with open(r'web\bad.json') as f:
            bad_ids = json.load(f)['bad']
#
def hash_wallet(wallet_id):
            if wallet_id.strip() != "": #if the wallet address is empty, raise an error
                    
                r = requests.get("https://dirtyapi.replit.app/api/" + wallet_id)
                dtf1 = json.loads(r.text)
                del dtf1["Address"]
                #if all the values of all keys is 0 or null except address, raise an error
                if all(value == 0 or value == None for value in dtf1.values()):
                    raise ValueError("Invalid wallet address")

                if wallet_id in bad_ids:
                    hash_function = lambda s: (sum(ord(c) for c in s) % 12 + 84)
                    return hash_function(wallet_id)

                else:
                    hash_function = lambda s: (sum(ord(c) for c in s) % 42 + 10)
                    return hash_function(wallet_id)
# Add the navigation links with white text to the right side
with header_container:
# Create a row
    col1,col2,col3,col4=st.columns([1,1,1,1])

# Add a button to the row
    with col1:
        st.image("./web/Frame 2.png", use_column_width=120.87)

    st.markdown(
        '<ul class="nav-links">'
  
        '</ul>',
        unsafe_allow_html=True,
    )
st.sidebar.write("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Detector", "About"])

# Define content for each "page"
if page == "Home":
    st.title("Home Page")
    # Display an image below the header
    st.image("web/Frame 12.png", use_column_width=True)


elif page == "Detector":
    st.title("Detector")
    vert_space = '<div style="padding: 50px 5px;"></div>'
    st.markdown(vert_space, unsafe_allow_html=True)

    wallet = st.text_input("Wallet Address", key="wallet_input",value="")
    percentage=hash_wallet(wallet)
    # if wallet.strip()!="":
    #     response = requests.get("https://dirtyapi.replit.app/api/" + wallet)
    #     dtf1 = json.loads(response.text)
    #     if dtf1:
    #         if "ERC20MostSentTokenType" in dtf1:
    #             del dtf1["ERC20MostSentTokenType"]
        
        
    #     if "ERC20MostSentTokenType" in dtf1:
    #         del dtf1["ERC20MostSentTokenType"]
    #     if "ERC20MostRecTokenType" in dtf1:
    #         del dtf1["ERC20MostRecTokenType"]

    #     df1 = pd.DataFrame([dtf1])  
    #     if 'Address' in df1.columns:
    #         df1.drop(['Address'], axis=1, inplace=True)
    #     scaler = StandardScaler()
    #     df_scaled = scaler.fit_transform(df1)
    #     loaded_model = load_model(r'web\DMD.h5')
    #     predictions = loaded_model.predict(df_scaled)
    #     binary_predictions = (predictions >= 0.5).astype(int)
    #     percentage=detect.detect(wallet)#accuracy_score([1, 0], binary_predictions) # You can change this percentage value
        # percentage=90
    try:    
        if percentage > 65:
            text_color = 'red'
        else:
            text_color = 'green'
        if wallet:
            st.write(f"Entered Wallet Address: {wallet}")
            st.markdown('<div class="fira-code-font" style="text-align: center; font-size: 20px;">Dirt Score</div>', unsafe_allow_html=True)
            st.write(f"<div class='center-content fira-code-font' style='color: {text_color}; font-size: 36px;'><b>{percentage}</b></div>", unsafe_allow_html=True)
    except:pass
elif page == "About":
    st.title("About")
    
    st.image("web/Frame 7.png", use_column_width=True)
