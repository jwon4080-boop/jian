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
    "휘발성 유기 화합물 VOC (ppb)",
    min_value=0.0,
    value=100.0
)
water = st.number_input(
      "수질 오염도 ",
       min_value=0,
       max_value=100,
       value=20
)
if st.button("🤖 오염도 분석하기"):

    data = f"""
환경 측정 데이터

PM10: {pm10} ㎍/㎥
PM2.5: {pm25} ㎍/㎥
CO₂: {co2} ppm
CO: {co} ppm
VOC: {voc} ppb
수질 오염도: {water}/100
"""

    prompt = f"""
너는 환경 분석 전문가 AI이다.

다음 데이터를 분석해라.

{data}

다음 형식으로 답변해라.

1. 전체 환경 상태 평가
2. 각 오염 물질별 위험도
3. 가장 문제가 되는 오염 물질
4. 건강 및 생태계 영향
5. 환경 개선 방법
6. 종합 환경 점수 (100점 기준)
"""

    with st.spinner("AI가 환경 데이터를 분석 중입니다."):

         response = client.responses.create(
            model="gpt-5.5",
            input=prompt
        )

    st.subheader("🌱 AI 환경 분석 결과")
    st.write(response.output_text)
