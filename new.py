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
    "이산화탄소 CO₂ (ppm)",
    min_value=0.0,
    value=400.0
)

if st.button("AI 환경 위험도 분석하기"):

    prompt = f"""
    다음 환경 데이터를 분석해주세요.

    PM10: {pm10} ㎍/㎥
    PM2.5: {pm25} ㎍/㎥
    CO2: {co2} ppm

    분석 내용:
    1. 현재 위험 수준 (좋음/보통/위험)
    2. 각 수치가 의미하는 환경 상태
    3. 건강 및 환경 보호를 위한 행동建议
    """

    response = ai_client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "당신은 환경 데이터 분석 전문가입니다."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content

    st.subheader("🤖 AI 분석 결과")
    st.write(result)
