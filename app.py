import streamlit as st
import random
import time

st.set_page_config(page_title="じゃんけん", page_icon="✊")
st.title("✊✌✋ じゃんけん")

hands = ["✊", "✌", "✋"]

# ===== 初期化 =====
if "player" not in st.session_state:
    st.session_state.player = None
if "computer" not in st.session_state:
    st.session_state.computer = None
if "phase" not in st.session_state:
    st.session_state.phase = "select"

# ===== コールバック =====
def select_hand(hand):
    st.session_state.player = hand
    st.session_state.phase = "janken"

def start_janken():
    st.session_state.phase = "shuffling"

def decide():
    st.session_state.computer = random.choice(hands)
    st.session_state.phase = "result"

def reset():
    st.session_state.player = None
    st.session_state.computer = None
    st.session_state.phase = "select"

# ===== 表示エリア =====
st.markdown("## 相手の手")
display = st.empty()

if st.session_state.phase == "result":
    display.markdown(
        f"<div style='font-size:80px; text-align:center;'>"
        f"{st.session_state.computer}"
        f"</div>",
        unsafe_allow_html=True
    )
elif st.session_state.phase == "shuffling":
    # シャッフル演出
    for _ in range(10):
        display.markdown(
            f"<div style='font-size:80px; text-align:center;'>"
            f"{random.choice(hands)}"
            f"</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.1)
else:
    display.markdown(
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
              on_click=start_janken)

elif st.session_state.phase == "shuffling":
    st.button("ぽん！", use_container_width=True,
              on_click=decide)

elif st.session_state.phase == "result":
    st.markdown("## あなたの手")
    st.markdown(
        f"<div style='font-size:80px; text-align:center;'>"
        f"{st.session_state.player}"
        f"</div>",
        unsafe_allow_html=True
    )

    st.button("もう一回 🔁", use_container_width=True,
              on_click=reset)
