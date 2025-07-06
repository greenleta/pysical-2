# app.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="무선 충전 시뮬레이터", layout="centered")

st.title("📱 무선 충전 위치 최적화 시뮬레이터")
st.markdown("""
전자기 유도 기반 무선 충전 시스템에서 **충전 거리**와 **코일 정렬도**가 충전 효율에 어떤 영향을 주는지 시뮬레이션합니다.
""")

# 사용자 입력
distance = st.slider("송신 코일과 수신 코일 간 거리 (cm)", min_value=1, max_value=50, value=10)
alignment = st.slider("코일 정렬도 (완벽 정렬=100%)", min_value=0, max_value=100, value=100)

# 효율 계산 (모델: 효율 ∝ 정렬도 × 1/d^2)
efficiency = (alignment / 100) * (1 / (distance ** 2)) * 100

st.subheader(f"🔋 추정 충전 효율: {efficiency:.2f} %")

# 그래프 출력
x = np.linspace(1, 50, 100)
y = (alignment / 100) * (1 / (x ** 2)) * 100

fig, ax = plt.subplots()
ax.plot(x, y, label=f"정렬도 {alignment}%", color="green")
ax.axvline(distance, color='red', linestyle='--', label=f"현재 거리: {distance} cm")
ax.set_xlabel("거리(cm)")
ax.set_ylabel("충전 효율(%)")
ax.set_title("거리 vs 충전 효율")
ax.legend()
ax.grid(True)
st.pyplot(fig)
