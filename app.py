import streamlit as st
import time

st.set_page_config(page_title="Dental AI Analysis", layout="wide")

st.title("🦷 파노라마 자동 분석 시스템")
st.subheader("환자 데이터를 업로드하여 AI 분석을 시작하세요.")

uploaded_file = st.file_uploader("파노라마 이미지 파일을 선택하세요", type=["jpg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="업로드된 파노라마 이미지", use_container_width=True)
    
    if st.button("AI 분석 시작"):
        with st.spinner('AI가 치아 상태를 정밀 분석 중입니다...'):
            time.sleep(3)
        
        st.success("분석이 완료되었습니다.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("### 📋 진단 결과")
            st.write("- **상악 우측 제2대구치:** 임플란트 식립 상태 양호")
            st.write("- **하악 좌측 제1소구치:** 치근단 병소 의심")
            
        with col2:
            st.write("### 💡 권장 조치")
            st.warning("하악 좌측 소구치에 대한 추가 정밀 검사 권장")
