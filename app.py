import streamlit as st

st.markdown("# 앱UI만들기")
user_id = st.text_input("이름", placeholder="이름")
ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)
user_id = st.text_input("반", value="1")

