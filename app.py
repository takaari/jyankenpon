import streamlit as st
import random
import time

st.set_page_config(page_title="じゃんけんアプリ", page_icon="✊")

st.title("✊✌✋ じゃんけんアプリ")
st.write("ボタンを押して「じゃんけん、ぽん！」")

hands = {
    "✊": "グー",
    "✌": "チョキ",
    "✋": "パー"
}

def judge(player, computer):
    if player == computer:
        return "あいこ 🤝"
    elif (
        (player == "✊" and computer == "✌") or
        (player == "✌" and computer == "✋") or
        (player == "✋" and computer == "✊")
    ):
        return "あなたの勝ち！🎉"
    else:
        return "あなたの負け…😢"

# セッション初期化
if "result" not in st.session_state:
    st.session_state.result = ""
    st.session_state.player = ""
    st.session_state.computer = ""

st.subheader("あなたの手を選んでください")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✊", use_container_width=True):
        st.session_state.player = "✊"

with col2:
    if st.button("✌", use_container_width=True):
        st.session_state.player = "✌"

with col3:
    if st.button("✋", use_container_width=True):
        st.session_state.player = "✋"

# 勝負処理
if st.session_state.player:
    with st.spinner("じゃんけん……ぽん！"):
        time.sleep(1)

    st.session_state.computer = random.choice(list(hands.keys()))
    st.session_state.result = judge(
        st.session_state.player,
        st.session_state.computer
    )

    st.divider()
    st.subheader("結果")

    st.write(f"### あなた：{st.session_state.player}")
    st.write(f"### コンピューター：{st.session_state.computer}")
    st.success(st.session_state.result)

    if st.button("もう一回やる 🔁"):
        st.session_state.player = ""
        st.session_state.result = ""
