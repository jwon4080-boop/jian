import streamlit as st

from openai import OpenAI
ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.title("🌍 AI 환경 오염도 체크 프로그램")
st.write("환경 오염 물질 수치를 입력하면 AI가 위험도를 측정합니다.")

pm10 = st.number_input(
    "미세먼지 PM10 (㎍/㎥)",
    min_value=0.0,
    value=30.0
)
                       
