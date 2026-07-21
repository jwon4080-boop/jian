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
pm25 = st.number_input(
    "초미세먼지 PM2.5 (㎍/㎥)",
    min_value=0.0,
    value=15.0
)
co2 = st.number_input(
    "이산화탄소 CO2 (ppm)",
    min_value=300,
    value=600
)
co = st.number_input(
    "일산화탄소 CO (ppm)",
    min_value=0.0,
    value=1.0
)
voc = st.number_input(
    "휘발성 유기 화합물 VOC (ppb)"
    min_value=0.0,
    value=100.0
)
water = st.number_input(
      "수질 오염도 ",
       min_value=0,
       max_value=100,
       value=20
)
