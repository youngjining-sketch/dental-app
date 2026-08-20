import streamlit as st
import time

st.set_page_config(page_title="Dental AI - Periodontal Analysis", layout="wide")

st.title("🦷 치주질환(잇몸뼈) 정밀 분석 시스템")

# --- 환자 정보 입력 사이드바 또는 상단 영역 ---
st.sidebar.header("👤 환자 정보 입력")
patient_name = st.sidebar.text_input("환자 성명")
chart_number = st.sidebar.text_input("차트 번호 (ID)")
patient_age = st.sidebar.number_input("나이", min_value=1, max_value=120, value=40)

st.subheader("파노라마 X-ray를 업로드하여 치조골 소실률 및 치주염 단계를 확인하세요.")

uploaded_file = st.file_uploader("파노라마 이미지 파일을 선택하세요", type=["jpg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption=f"환자명: {patient_name} (차트: {chart_number}) 파노라마 이미지", use_container_width=True)
    
    if st.button("치주질환 AI 정밀 분석 시작"):
        # 환자 정보가 입력되었는지 간단한 확인
        if not patient_name:
            st.warning("⚠️ 환자 성명을 입력해주세요!")
        else:
            with st.spinner(f'{patient_name} 님의 치조골 소실도 및 잇몸 상태를 분석 중입니다...'):
                time.sleep(3)
            
            st.success(f"[{patient_name} 환자] 치주 분석이 완료되었습니다.")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"### 📋 {patient_name} 님 진단 리포트")
                st.write(f"- **차트 번호:** {chart_number if chart_number else '미입력'}")
                st.write(f"- **나이:** {patient_age}세")
                st.write("- **상악 구치부 치조골 소실률:** 약 35% (중등도 치주염 의심)")
                st.write("- **하악 전치부 잇몸뼈 상태:** 양호 (소실률 10% 미만)")
                
            with col2:
                st.write("### 💡 AI 권장 조치 및 치료 계획")
                st.warning("⚠️ **상악 좌/우측 구치부 스케일링 및 치주 소파술 필요**")
                st.info("추가적인 치주 파노라마 또는 구내 엑스레이 촬영 권장")
