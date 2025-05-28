import pandas as pd

# Google Drive의 파일 URL
url = 'https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY'

# CSV 파일 읽어오기
df = pd.read_csv(url)

# 데이터 확인
print(df.head())

import plotly.express as px

# 예시: 'Category'별 'Sales' 합계
fig = px.bar(df, x='Category', y='Sales', title='Category별 Sales 합계', color='Category')

# Plotly 차트 출력 (Jupyter 환경일 때는 fig.show())
fig.show()

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Plotly 시각화 웹앱")

# 데이터 불러오기
url = 'https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY'
df = pd.read_csv(url)

st.subheader("데이터 미리보기")
st.dataframe(df.head())

# 컬럼 선택
x_col = st.selectbox("X축 선택", df.columns)
y_col = st.selectbox("Y축 선택", df.columns)

# 차트 그리기
fig = px.bar(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
st.plotly_chart(fig)

streamlit run app.py
