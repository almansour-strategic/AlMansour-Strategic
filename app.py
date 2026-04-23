import streamlit as st
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT

# ================== 1. إعدادات الهوية البصرية وإخفاء الأدوات ==================
st.set_page_config(page_title="المنصور AI", layout="wide")

# كود CSS لإخفاء زر الإدارة، القوائم، وتنسيق الواجهة الملكية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* إخفاء زر إدارة التطبيق وأي أدوات لـ Streamlit بشكل نهائي */
    div[data-testid="stToolbar"], #MainMenu, footer, header, .stDeployButton, [data-testid="stStatusWidget"] {
        visibility: hidden;
        display: none !important;
    }
    
    .stApp { background-color: #020617; color: #ffffff; direction: rtl; }
    
    .main-card {
        background: linear-gradient(145deg, #0f172a, #1e293b);
        border: 2px solid #fbbf24;
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 25px 60px rgba(0,0,0,0.8);
        max-width: 900px;
        margin: auto;
    }

    * { font-family: 'Cairo', sans-serif !important; }
    h1 { color: #fbbf24 !important; font-weight: 900 !important; font-size: 3rem !important; text-align: center; margin-bottom: 5px; }
    .sub-title { color: #94a3b8; text-align: center; font-size: 1.2rem; margin-bottom: 30px; }
    
    .stButton>button {
        background: linear-gradient(90deg, #b45309 0%, #fbbf24 100%);
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        height: 55px !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# ================== 2. وظائف النظام ==================
ADMIN_EMAIL = "almansoourd@gmail.com"

if "auth_status" not in st.session_state:
    st.session_state.auth_status = None
    st.session_state.user_role = None

def export_to_pdf(data):
    file_name = "AlMansour_AI_Report.pdf"
    doc = SimpleDocTemplate(file_name)
    styles = getSampleStyleSheet()
    arabic_style = ParagraphStyle('Arabic', parent=styles['Normal'], alignment=TA_RIGHT, fontSize=12, leading=18)
    story = [Paragraph("<b>المنصور AI - تقرير رسمي</b>", styles['Title']), Spacer(1, 20)]
    for key, value in data.items():
        story.append(Paragraph(f"<b>{key}:</b>", arabic_style))
        story.append(Paragraph(value if value else "لا يوجد", arabic_style))
        story.append(Spacer(1, 12))
    doc.build(story)
    return file_name

# ================== 3. بوابة الدخول الذكية ==================
if st.session_state.auth_status is None:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("<h1>المنصور AI</h1>", unsafe_allow_html=True)
    st.markdown('<p class="sub-title">للتقارير الاحترافية والاستشارية</p>', unsafe_allow_html=True)
    
    email = st.text_input("البريد الإلكتروني")
    pwd = st.text_input("كلمة المرور", type="password")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("دخول المستشارين"):
            if email == ADMIN_EMAIL and pwd == "2026":
                st.session_state.auth_status = True
                st.session_state.user_role = "admin"
                st.rerun()
            else:
                st.error("بيانات المدير غير صحيحة")
    with col2:
        if st.button("دخول العملاء"):
            if email and pwd: # نظام دخول مرن للعملاء
                st.session_state.auth_status = True
                st.session_state.user_role = "client"
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ================== 4. لوحة الإدارة (تفتح لك أنت فقط) ==================
if st.session_state.user_role == "admin":
    st.sidebar.markdown("### ⚙️ لوحة التحكم")
    st.sidebar.write(f"مرحباً بك مستشار منصور")
    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.auth_status = None
        st.rerun()
    
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("🛡️ إدارة النظام")
    st.write("هنا يمكنك رؤية إحصائيات الاستخدام والتقارير الصادرة (سيتم ربطها بقاعدة البيانات لاحقاً).")
    st.markdown('</div>', unsafe_allow_html=True)

# ================== 5. واجهة التقارير (الأسئلة الـ 11) ==================
if st.session_state.user_role in ["client", "admin"]:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("<h1>المنصور AI</h1>", unsafe_allow_html=True)
    st.markdown('<p class="sub-title">نظام صياغة التقارير الدولية</p>', unsafe_allow_html=True)

    p_name = st.text_input("📍 اسم المشروع / التقرير")
    
    # الأسئلة الاستراتيجية كاملة
    st.markdown("### 📝 محاور التقرير الـ 11")
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

    if st.button("🚀 إصدار التقرير النهائي (PDF)"):
        report_data = {"المشروع": p_name, "الملخص": q1, "التوصيات": q10}
        pdf_path = export_to_pdf(report_data)
        with open(pdf_path, "rb") as f:
            st.download_button("📥 تحميل PDF المعتمد", f, file_name=f"{p_name}.pdf")
    
    if st.button("خروج"):
        st.session_state.auth_status = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
