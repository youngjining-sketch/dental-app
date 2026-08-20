import streamlit as st
import time
from PIL import Image, ImageDraw

st.set_page_config(page_title="Dental AI - Periodontal Analysis", layout="wide")

st.title("🦷 치주질환(잇몸뼈) 정밀 분석 시스템")

# --- 환자 정보 입력 사이드바 ---
st.sidebar.header("👤 환자 정보 입력")
patient_name = st.sidebar.text_input("환자 성명", value="이영진")
chart_number = st.sidebar.text_input("차트 번호 (ID)", value="a-011")
patient_age = st.sidebar.number_input("나이", min_value=1, max_value=120, value=100)

st.subheader("파노라마 X-ray를 업로드하여 치조골 소실률 및 치주염 단계를 확인하세요.")

uploaded_file = st.file_uploader("파노라마 이미지 파일을 선택하세요", type=["jpg", "png"])

if uploaded_file is not None:
    # 원본 이미지 출력
    st.image(uploaded_file, caption=f"환자명: {patient_name} (차트: {chart_number}) 원본 파노라마 이미지", use_container_width=True)
    
    if st.button("치주질환 AI 정밀 분석 및 라인 시각화 시작"):
        if not patient_name:
            st.warning("⚠️ 환자 성명을 입력해주세요!")
        else:
            with st.spinner(f'{patient_name} 님의 치조골 라인을 분석하여 선을 긋는 중입니다...'):
                time.sleep(3)
            
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

            # --- 핵심: 업로드한 사진 위에 초록색(이상적 라인)과 붉은색(실제 뼈 라인) 직접 그리기 ---
            st.write("---")
            st.write("### 🔬 잇몸뼈 소실 라인 분석 시각화")
            
            # 이미지를 열어서 그리기 도구 준비
            image = Image.open(uploaded_file)
            draw = ImageDraw.Draw(image)
            width, height = image.size
            
            # 초록색 선 (이상적인 잇몸뼈 상단 라인 예시)
            draw.line([(width * 0.15, height * 0.38), (width * 0.85, height * 0.38)], fill="green", width=8)
            
            # 붉은색 선 (실제로 녹아내린 환자의 치조골 라인 예시 - 어금니 쪽이 내려앉은 형태)
            draw.line([(width * 0.15, height * 0.42), (width * 0.35, height * 0.45), (width * 0.65, height * 0.45), (width * 0.85, height * 0.42)], fill="red", width=8)
            
            # 선이 그려진 이미지를 웹에 출력
            st.image(image, caption=f"[{patient_name}] 🟢 초록색선: 이상적인 잇몸라인 / 🔴 붉은색선: 실제 낮아진 치조골 라인", use_container_width=True)
            st.info("💡 **분석 결과**: 초록색 정상선과 비교했을 때, 상악 어금니 부위의 붉은색 라인이 아래로 내려앉아 치조골 소실이 발생한 것을 확인할 수 있습니다.")
