import streamlit as st
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT

# ================== 1. إعدادات الهوية البصرية الصارمة ==================
st.set_page_config(page_title="المنصور AI", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* منع ظهور أي أدوات خاصة بالمنصة للأبد */
    div[data-testid="stToolbar"], #MainMenu, footer, header, .stDeployButton, [data-testid="stStatusWidget"], [data-testid="stDecoration"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* تنظيف واجهة الجوال */
    .stApp { background-color: #020617; color: #ffffff; direction: rtl; }
    
    .main-card {
        background: #0f172a;
        border: 2px solid #fbbf24;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
        margin-top: 10px;
    }

    * { font-family: 'Cairo', sans-serif !important; }
    h1 { color: #fbbf24 !important; font-weight: 900 !important; font-size: 2.2rem !important; text-align: center; margin-bottom: 5px; }
    .sub-title { color: #94a3b8; text-align: center; font-size: 1rem; margin-bottom: 20px; }
    
    /* تنسيق الحقول لمنع التداخل */
    .stTextInput input, .stTextArea textarea {
        background-color: #1e293b !important;
        color: white !important;
        border-radius: 10px !important;
        border: 1px solid #fbbf24 !important;
        text-align: right !important;
    }
    
    .stButton>button {
        background: linear-gradient(90deg, #b45309 0%, #fbbf24 100%);
        color: white !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        height: 50px !important;
        width: 100% !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# ================== 2. قاعدة البيانات البسيطة والتحقق ==================
ADMIN_USER = "almansoourd@gmail.com"
ADMIN_PASS = "2026"

if "auth" not in st.session_state:
    st.session_state.auth = False
    st.session_state.role = None

# ================== 3. بوابة الدخول (بدون مربعات زائدة) ==================
if not st.session_state.auth:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("<h1>المنصور AI</h1>", unsafe_allow_html=True)
    st.markdown('<p class="sub-title">للتقارير الاحترافية والاستشارية</p>', unsafe_allow_html=True)
    
    email = st.text_input("البريد الإلكتروني")
    pwd = st.text_input("كلمة المرور", type="password")
    
    if st.button("دخول المنصة"):
        if email == ADMIN_USER and pwd == ADMIN_PASS:
            st.session_state.auth = True
            st.session_state.role = "admin"
            st.rerun()
        elif email and pwd:
            st.session_state.auth = True
            st.session_state.role = "client"
            st.rerun()
        else:
            st.error("يرجى إدخال بيانات صحيحة")
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ================== 4. المحتوى بعد الدخول ==================
if st.session_state.role == "admin":
    st.sidebar.success("تم الدخول بصلاحية: مدير")
    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.auth = False
        st.rerun()

st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown("<h1>المنصور AI</h1>", unsafe_allow_html=True)

if st.session_state.role == "admin":
    st.markdown("### 🛡️ لوحة إدارة التقارير")
    st.info("مرحباً بك مستشار منصور. النظام جاهز لاستلام البيانات.")

# الحقول الـ 11 الاستراتيجية
p_name = st.text_input("📍 اسم المشروع")
q1 = st.text_area("1. الملخص التنفيذي:")
q2 = st.text_area("2. تحليل بيئة العمل:")
q3 = st.text_area("3. التحديات والعقبات:")
q4 = st.text_area("4. الموارد البشرية واللوجستية:")
q5 = st.text_area("5. التحليل المالي والميزانية:")
q6 = st.text_area("6. نسبة الإنجاز والجدول الزمني:")
q7 = st.text_area("7. الجودة والامتثال:")
q8 = st.text_area("8. تحليل المخاطر المحتملة:")
q9 = st.text_area("9. فرص التحسين والتطوير:")
q10 = st.text_area("10. التوصيات النهائية:")
q11 = st.text_area("11. الملاحظات والختام:")

if st.button("🚀 توليد التقرير النهائي (PDF)"):
    st.success(f"تم البدء في معالجة تقرير: {p_name}")
    # كود توليد الـ PDF هنا (موجود في النسخ السابقة)

if st.button("تسجيل خروج"):
    st.session_state.auth = False
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
