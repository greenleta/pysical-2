# wireless_charging_efficiency.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📱 무선 충전 위치 최적화 시뮬레이터")
distance = st.slider("송신 코일과 수신 코일 간 거리 (cm)", 1, 50, 10)
alignment = st.slider("코일 중심 정렬도 (%)", 0, 100, 100)

efficiency = (alignment / 100) * (1 / (distance ** 2)) * 100

st.write(f"충전 효율(추정): {efficiency:.2f} %")

x = np.linspace(1, 50, 100)
y = (alignment / 100) * (1 / (x ** 2)) * 100
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("거리(cm)")
ax.set_ylabel("효율(%)")
ax.set_title("거리-충전 효율 관계")
st.pyplot(fig)
