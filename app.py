import streamlit as st
import random
import time

st.set_page_config(page_title="じゃんけんアプリ", page_icon="✊")

st.title("✊✌✋ じゃんけん")

# セッション初期化
if "computer" not in st.session_state:
    st.session_state.computer = ""

hands = ["✊", "✌", "✋"]

# ===== 相手の手（タイトル直下） =====
if st.session_state.computer:
    st.markdown("## 相手の手")
    st.markdown(
        f"<div style='font-size:80px; text-align:center;'>"
        f"{st.session_state.computer}"
        f"</div>",
        unsafe_allow_html=True
    )
else:
    st.markdown("## 相手の手")
    st.markdown(
        "<div style='font-size:40px; text-align:center; color:gray;'>？？？</div>",
        unsafe_allow_html=True
    )

st.divider()

st.markdown("### じゃんけん、ぽん！")

col1, col2, col3 = st.columns(3)

def play():
    with st.spinner("ぽん！"):
        time.sleep(0.8)
    st.session_state.computer = random.choice(hands)

with col1:
    if st.button("✊", use_container_width=True):
        play()

with col2:
    if st.button("✌", use_container_width=True):
        play()

with col3:
    if st.button("✋", use_container_width=True):
        play()
