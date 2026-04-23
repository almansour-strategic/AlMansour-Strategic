import streamlit as st
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT

# ================== 1. الهوية البصرية الملكية (CSS القوة) ==================
st.set_page_config(page_title="المنصور استراتيجي", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* إخفاء تام لكل أدوات المنصة */
    div[data-testid="stToolbar"], #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #020617; color: #ffffff; direction: rtl; }
    
    /* الحاوية الرئيسية (الكارت الذهبي) */
    .main-card {
        background: linear-gradient(145deg, #0f172a, #1e293b);
        border: 2px solid #fbbf24;
        padding: 50px;
        border-radius: 30px;
        box-shadow: 0 25px 60px rgba(0,0,0,0.8);
        max-width: 1000px;
        margin: auto;
    }

    /* تنسيق الخطوط */
    * { font-family: 'Cairo', sans-serif !important; }
    h1 { color: #fbbf24 !important; font-weight: 900 !important; font-size: 3.5rem !important; text-align: center; text-shadow: 2px 2px 10px rgba(251, 191, 36, 0.3); }
    h3 { color: #fbbf24 !important; font-weight: 700 !important; border-bottom: 2px solid #fbbf24; padding-bottom: 10px; margin-top: 30px; }
    
    /* تنسيق الأزرار */
    .stButton>button {
        background: linear-gradient(90deg, #b45309 0%, #fbbf24 100%);
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        height: 65px !important;
        font-size: 1.4rem !important;
        font-weight: 900 !important;
        width: 100% !important;
        box-shadow: 0 10px 20px rgba(180, 83, 9, 0.3);
        cursor: pointer;
        transition: 0.4s;
    }
    .stButton>button:hover { transform: translateY(-5px); box-shadow: 0 15px 30px #fbbf24; }
    
    /* تنسيق الحقول */
    .stTextInput input, .stTextArea textarea {
        background-color: #0f172a !important;
        color: #ffffff !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        font-size: 1.2rem !important;
        padding: 15px !important;
    }
    label { color: #94a3b8 !important; font-size: 1.1rem !important; font-weight: bold !important; }
    </style>
""", unsafe_allow_html=True)

# ================== 2. وظيفة الـ PDF الاحترافية ==================
def export_to_pdf(data):
    file_name = "AlMansour_Report.pdf"
    doc = SimpleDocTemplate(file_name)
    styles = getSampleStyleSheet()
    # ستايل يدعم اتجاه النص العربي
    arabic_style = ParagraphStyle('Arabic', parent=styles['Normal'], alignment=TA_RIGHT, fontSize=12, leading=18)
    
    story = [Paragraph("<b>المنصور استراتيجي - تقرير رسمي</b>", styles['Title']), Spacer(1, 20)]
    for key, value in data.items():
        story.append(Paragraph(f"<b>{key}:</b>", arabic_style))
        story.append(Paragraph(value if value else "لا يوجد", arabic_style))
        story.append(Spacer(1, 12))
    doc.build(story)
    return file_name

# ================== 3. بوابة الدخول (الهيبة) ==================
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("<h1>🛡️ بوابة الوصول</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#94a3b8;'>منصة المستشار منصور أحمد سعيد - الدخول خاص</p>", unsafe_allow_html=True)
    
    user = st.text_input("اسم المستخدم")
    pwd = st.text_input("كلمة المرور", type="password")
    if st.button("فتح المنصة الاستراتيجية"):
        if user == "mansour" and pwd == "2026": # يمكنك تغييرها لما تريد
            st.session_state.auth = True
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ================== 4. صلب المنصة (الأسئلة الـ 11 كاملة) ==================
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown("<h1>📊 المنصور استراتيجي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#fbbf24; font-size:1.3rem;'>نظام صياغة التقارير الدولية والميدانية</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    p_name = st.text_input("📍 اسم المشروع / المهمة")
with col2:
    p_type = st.selectbox("🗂️ نوع التقرير", ["تقرير إنجاز ميداني", "تقرير تحليل مالي", "محضر اجتماع إدارة", "تقرير استجابة طارئة"])

st.markdown("### 📝 المحاور الاستراتيجية الـ 11")

q1 = st.text_area("1. الملخص التنفيذي (خلاصة الإنجاز):")
q2 = st.text_area("2. تحليل بيئة العمل والظروف الميدانية:")
q3 = st.text_area("3. التحديات والعقبات (بشفافية تامة):")
q4 = st.text_area("4. الموارد البشرية واللوجستية المستخدمة:")
q5 = st.text_area("5. تحليل الميزانية والكفاءة المالية:")
q6 = st.text_area("6. قياس نسبة الإنجاز مقابل الجدول الزمني:")
q7 = st.text_area("7. الجودة والامتثال للمعايير المعتمدة:")
q8 = st.text_area("8. تحليل المخاطر المحتملة (المستقبلية):")
q9 = st.text_area("9. فرص التطوير والتحسين المقترحة:")
q10 = st.text_area("10. التوصيات النهائية لصناع القرار:")
q11 = st.text_area("11. الملاحظات العامة والختام:")

if st.button("🚀 إصدار وتوليد التقرير الماسي"):
    if p_name and q1:
        data_to_save = {
            "المشروع": p_name, "النوع": p_type,
            "1. الملخص": q1, "2. البيئة": q2, "3. التحديات": q3,
            "4. الموارد": q4, "5. المالية": q5, "6. الإنجاز": q6,
            "7. الجودة": q7, "8. المخاطر": q8, "9. الفرص": q9,
            "10. التوصيات": q10, "11. الختام": q11
        }
        
        st.success("✅ تم معالجة البيانات بنجاح استراتيجي")
        
        pdf_path = export_to_pdf(data_to_save)
        with open(pdf_path, "rb") as f:
            st.download_button("📥 تحميل التقرير النهائي (PDF)", f, file_name=f"{p_name}.pdf")
    else:
        st.error("⚠️ يرجى تعبئة اسم المشروع والملخص التنفيذي على الأقل")

st.markdown('</div>', unsafe_allow_html=True)

# زر الخروج
if st.sidebar.button("تسجيل الخروج"):
    st.session_state.auth = False
    st.rerun()

st.markdown("<br><center style='color:#64748b;'>🛡️ المنصور استراتيجي | القوة والتميز في إدارة البيانات 2026</center>", unsafe_allow_html=True)
