import streamlit as st
import random
import time

st.set_page_config(page_title="じゃんけん", page_icon="✊")
st.markdown(
    "<h1 style='font-style: italic; text-align: center;'>✌ jyanken-pon ✌</h1>",
    unsafe_allow_html=True
)


hands = ["✊", "✌", "✋"]

# ===== 初期化 =====
if "player" not in st.session_state:
    st.session_state.player = None
if "computer" not in st.session_state:
    st.session_state.computer = None
if "phase" not in st.session_state:
    st.session_state.phase = "select"
# select → janken → pon → result

# ===== コールバック =====
def select_hand(hand):
    st.session_state.player = hand
    st.session_state.phase = "janken"

def go_janken():
    st.session_state.phase = "pon"

def go_pon():
    st.session_state.computer = random.choice(hands)
    st.session_state.phase = "result"

def reset():
    st.session_state.player = None
    st.session_state.computer = None
    st.session_state.phase = "select"

# ===== 表示エリア =====
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
        st.button("✊", use_container_width=True,
                  on_click=select_hand, args=("✊",))
    with col2:
        st.button("✌", use_container_width=True,
                  on_click=select_hand, args=("✌",))
    with col3:
        st.button("✋", use_container_width=True,
                  on_click=select_hand, args=("✋",))

elif st.session_state.phase == "janken":
    st.markdown("### 準備OK")
    st.button("じゃんけん", use_container_width=True,
              on_click=go_janken)

elif st.session_state.phase == "pon":
    st.button("ぽん！", use_container_width=True,
              on_click=go_pon)

elif st.session_state.phase == "result":
    st.button("もう一回 🔁", use_container_width=True,
              on_click=reset)

