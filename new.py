import streamlit as st

from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.title("🌍 AI 환경 오염도 체크 프로그램")
st.write("환경 오염 물질 수치를 입력하면 AI가 위험도를 측정합니다.")
