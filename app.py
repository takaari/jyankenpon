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
if "shuffling" not in st.session_state:
    st.session_state.shuffling = False
if "temp_hand" not in st.session_state:
    st.session_state.temp_hand = "✊"

# ===== コールバック =====
def select_hand(hand):
    st.session_state.player = hand
    st.session_state.phase = "janken"

def start_shuffling():
    st.session_state.phase = "shuffling"
    st.session_state.shuffling = True

def decide():
    st.session_state.shuffling = False
    st.session_state.computer = random.choice(hands)
    st.session_state.phase = "result"

def reset():
    st.session_state.player = None
    st.session_state.computer = None
    st.session_state.phase = "select"
    st.session_state.shuffling = False

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
    # 1フレーム分だけ更新
    st.session_state.temp_hand = random.choice(hands)
    display.markdown(
        f"<div style='font-size:80px; text-align:center;'>"
        f"{st.session_state.temp_hand}"
        f"</div>",
        unsafe_allow_html=True
    )

    # 少し待って自動再実行
    time.sleep(0.12)
    if st.session_state.shuffling:
        st.rerun()

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
    st.button("じゃんけん", use_container_width=True,
              on_click=start_shuffling)

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
