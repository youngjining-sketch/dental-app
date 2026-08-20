import streamlit as st
import time

st.set_page_config(page_title="Dental AI - Periodontal Analysis", layout="wide")

st.title("🦷 치주질환(잇몸뼈) 정밀 분석 시스템")

# --- 환자 정보 입력 사이드바 ---
st.sidebar.header("👤 환자 정보 입력")
patient_name = st.sidebar.text_input("환자 성명", value="이영진")
chart_number = st.sidebar.text_input("차트 번호 (ID)", value="a-011")
patient_age = st.sidebar.number_input("나이", min_value=1, max_value=120, value=100)

st.subheader("파노라마 X-ray를 업로드하여 치조골 소실률 및 치주염 단계를 확인하세요.")

uploaded_file = st.file_uploader("파노라마 이미지 파일을 선택하세요 (예시 파일 권장)", type=["jpg", "png"])

if uploaded_file is not None:
    # 원본 이미지를 먼저 보여줍니다.
    st.image(uploaded_file, caption=f"환자명: {patient_name} (차트: {chart_number}) 파노라마 이미지", use_container_width=True)
    
    if st.button("치주질환 AI 정밀 분석 및 라인 표시 시작"):
        if not patient_name:
            st.warning("⚠️ 환자 성명을 입력해주세요!")
        else:
            with st.spinner(f'{patient_name} 님의 치조골 소실 라인을 분석하여 표시하는 중입니다...'):
                time.sleep(4) # 분석 시뮬레이션 시간
            
            st.success(f"[{patient_name} 환자] 치주 분석 및 시각화가 완료되었습니다.")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"### 📋 {patient_name} 님 진단 리포트")
                st.write(f"- **차트 번호:** {chart_number}")
                st.write("- **상악 구치부 치조골 소실률:** 약 35% (중등도 치주염 의심)")
                st.write("- **하악 전치부 잇몸뼈 상태:** 양호 (소실률 10% 미만)")
                
            with col2:
                st.write("### 💡 AI 권장 조치")
                st.warning("⚠️ **상악 구치부 치주 소파술 및 스케일링 필요**")

            # --- 핵심 기능: 잇몸 라인 비교 시각화 시뮬레이션 ---
            st.write("---")
            st.write("### 🔬 [시뮬레이션] 잇몸뼈 소실 라인 시각화")
            st.write("아래 이미지는 AI가 파노라마상에서 정상적인 치조골 높이와 현재 환자의 치조골 높이를 비교하여 분석한 결과입니다.")
            
            # 실제로는 여기서 AI가 분석한 좌표를 바탕으로 이미지를 그려주지만, 
            # 지금은 시뮬레이션이므로 분석 결과를 글로 자세히 풀어쓰고, 
            # 최종 결과 화면 아래쪽에 가상의 비교 이미지를 띄우는 것으로 대체합니다.
            # (실제 구현 시에는 별도의 이미지 처리 라이브러리가 필요합니다.)
            st.image("https://i.imgur.com/r4t57jK.png", caption="[예시] 정상 잇몸라인(초록색 실선)과 실제 환자 잇몸라인(붉은색 점선) 비교 분석", use_container_width=True)
            st.info("초록색 선은 이상적인 뼈 높이이며, 붉은색 점선이 실제로 낮아진 치조골의 위치를 나타냅니다. 상악 어금니 부위에서 심각한 골소실이 관찰됩니다.")
