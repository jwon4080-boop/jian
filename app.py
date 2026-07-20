import streamlit as st

st.markdown("# 앱UI만들기")
user_id = st.text_input("이름", placeholder="이름")
ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)
cls = st.number_input("반", value="1")
user_id = st.text_input("아이디(ID)를 입력하세요", placeholder="example_user")
age = st.number_input("나이를 입력하세요", min_value=1, max_value=100, value=17)
