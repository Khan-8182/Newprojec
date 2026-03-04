import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Cricket Score Predictor", page_icon="🏏", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    .stMetric {
        background-color: #1c1f26;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🏏 AI Powered Cricket Score Predictor")
st.markdown("### Predict Final Score in a 20 Over Match")

# ---------------- DATASET ----------------
data = {
    'current_runs': [50, 80, 120, 30, 100, 70, 150, 60, 90, 110],
    'overs_completed': [6, 10, 15, 5, 12, 8, 18, 7, 11, 14],
    'wickets': [1, 2, 4, 0, 3, 2, 6, 1, 3, 4],
    'final_score': [160, 175, 190, 140, 180, 165, 210, 155, 170, 185]
}

df = pd.DataFrame(data)

X = df[['current_runs', 'overs_completed', 'wickets']]
y = df['final_score']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

# ---------------- SIDEBAR INPUTS ----------------
st.sidebar.header("Match Details")

current_runs = st.sidebar.slider("Current Runs", 0, 300, 80)
overs_completed = st.sidebar.slider("Overs Completed", 0, 20, 10)
wickets_left = st.sidebar.slider("Wickets Left", 0, 10, 7)

# ---------------- MAIN DISPLAY ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Runs", current_runs)

with col2:
    st.metric("Overs Completed", overs_completed)

with col3:
    st.metric("Wickets Left", wickets_left)

st.write("---")

# ---------------- PREDICTION ----------------
if st.button("Predict Final Score 🚀"):

    wickets_down = 10 - wickets_left
    new_data = np.array([[current_runs, overs_completed, wickets_down]])

    predicted_score = model.predict(new_data)

    st.success(f"🏆 Predicted Final Score: {round(predicted_score[0])}")

    st.balloons()

# ---------------- MODEL INFO ----------------
st.write("---")
st.subheader("📊 Model Performance")
st.info(f"Model Accuracy (R² Score): {round(accuracy * 100, 2)}%")
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Cricket Score Predictor", page_icon="🏏", layout="wide")

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
    <style>
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🏏 AI Cricket Score Predictor")
st.markdown("### Predict Final Score in a 20 Over Match")

# ---------------- DATASET ----------------
data = {
    'current_runs': [50, 80, 120, 30, 100, 70, 150, 60, 90, 110],
    'overs_completed': [6, 10, 15, 5, 12, 8, 18, 7, 11, 14],
    'wickets': [1, 2, 4, 0, 3, 2, 6, 1, 3, 4],
    'final_score': [160, 175, 190, 140, 180, 165, 210, 155, 170, 185]
}

df = pd.DataFrame(data)

X = df[['current_runs', 'overs_completed', 'wickets']]
y = df['final_score']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

# ---------------- INPUT METHOD SELECTION ----------------
input_method = st.radio("Choose Input Method:", ["Use Sliders", "Enter Manually"])

# ---------------- INPUT SECTION ----------------
if input_method == "Use Sliders":
    current_runs = st.slider("Current Runs", 0, 300, 80)
    overs_completed = st.slider("Overs Completed", 0, 20, 10)
    wickets_left = st.slider("Wickets Left", 0, 10, 7)

else:
    col1, col2, col3 = st.columns(3)

    with col1:
        current_runs = st.number_input("Current Runs", min_value=0)

    with col2:
        overs_completed = st.number_input("Overs Completed", min_value=0, max_value=20)

    with col3:
        wickets_left = st.number_input("Wickets Left", min_value=0, max_value=10)

st.write("---")

# ---------------- PREDICTION ----------------
if st.button("Predict Final Score 🚀"):

    wickets_down = 10 - wickets_left
    new_data = np.array([[current_runs, overs_completed, wickets_down]])

    predicted_score = model.predict(new_data)

    st.success(f"🏆 Predicted Final Score: {round(predicted_score[0])}")
    st.balloons()

# ---------------- MODEL INFO ----------------
st.write("---")
st.subheader("📊 Model Performance")
st.info(f"Model Accuracy (R² Score): {round(accuracy * 100, 2)}%")
