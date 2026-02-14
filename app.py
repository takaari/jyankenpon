import streamlit as st
import random
import time

st.set_page_config(page_title="じゃんけん", page_icon="✊")
st.title("✊✌✋ じゃんけん")

hands = ["✊", "✌", "✋"]

# ===== セッション初期化 =====
if "player" not in st.session_state:
    st.session_state.player = None
if "computer" not in st.session_state:
    st.session_state.computer = None
if "phase" not in st.session_state:
    st.session_state.phase = "select"
# select → janken → pon → result

# ===== 表示エリア（上） =====
st.markdown("## 相手の手")

if st.session_state.phase == "result":
    st.markdown(
        f"<div style='font-size:80px; text-align:center;'>"
        f"{st.session_state.computer}"
        f"</div>",
        unsafe_allow_html=True
    )

    st.markdown("## あなたの手")
    st.markdown(
        f"<div style='font-size:80px; text-align:center;'>"
        f"{st.session_state.player}"
        f"</div>",
        unsafe_allow_html=True
    )
else:
    st.markdown(
        "<div style='font-size:40px; text-align:center; color:gray;'>？？？</div>",
        unsafe_allow_html=True
    )

st.divider()

# ===== フェーズ別UI =====
if st.session_state.phase == "select":
    st.markdown("### 手を選んでください")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✊", use_container_width=True):
            st.session_state.player = "✊"
            st.session_state.phase = "janken"
    with col2:
        if st.button("✌", use_container_width=True):
            st.session_state.player = "✌"
            st.session_state.phase = "janken"
    with col3:
        if st.button("✋", use_container_width=True):
            st.session_state.player = "✋"
            st.session_state.phase = "janken"

elif st.session_state.phase == "janken":
    st.markdown("### 準備OK")
    if st.button("じゃんけん", use_container_width=True):
        with st.spinner("……"):
            time.sleep(0.6)
        st.session_state.phase = "pon"

elif st.session_state.phase == "pon":
    if st.button("ぽん！", use_container_width=True):
        with st.spinner("ぽん！"):
            time.sleep(0.4)
        st.session_state.computer = random.choice(hands)
        st.session_state.phase = "result"

elif st.session_state.phase == "result":
    if st.button("もう一回 🔁", use_container_width=True):
        st.session_state.player = None
        st.session_state.computer = None
        st.session_state.phase = "select"
