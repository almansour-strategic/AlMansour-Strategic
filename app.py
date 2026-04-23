import streamlit as st
import pandas as pd
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ================== إعدادات الواجهة الملكية وإخفاء الأدوات ==================
st.set_page_config(page_title="المنصور استراتيجي", layout="wide")

hide_style = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    * { font-family: 'Cairo', sans-serif; }
    div[data-testid="stToolbar"], #MainMenu, footer, header {visibility: hidden;}
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f1f5f9;
    }
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid #fbbf24;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    h1, h2, h3 { color: #fbbf24 !important; text-align: right; }
    .stButton>button {
        background: linear-gradient(90deg, #d97706 0%, #fbbf24 100%);
        color: white; border: none; border-radius: 10px; width: 100%;
        font-weight: bold; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 5px 15px rgba(251, 191, 36, 0.4); }
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# ================== المساعد الذكي ووظائف PDF ==================
def create_pdf(title, content):
    file_name = "AlMansour_Report.pdf"
    doc = SimpleDocTemplate(file_name)
    styles = getSampleStyleSheet()
    # إضافة ستايل يدعم التنسيق العربي (تقريبي بدون مكتبات معقدة)
    rtl_style = ParagraphStyle('rtl', parent=styles['Normal'], alignment=TA_RIGHT, fontSize=12)
    
    story = []
    story.append(Paragraph(f"<b>{title}</b>", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(content.replace("\n", "<br/>"), rtl_style))
    doc.build(story)
    return file_name

# ================== واجهة المنصة ==================
with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("🚀 منصة المنصور الاستراتيجية")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col2:
        report_type = st.selectbox("🎯 نوع التقرير", 
            ["تقرير إنجاز ميداني", "تقرير مالي استراتيجي", "محضر اجتماع مجلس إدارة", "تقرير تحليل مخاطر"])
        project_name = st.text_input("📝 اسم المشروع / الجهة")
    
    with col1:
        date_now = st.date_input("📅 التاريخ", datetime.now())
        prepared_by = st.text_input("👨‍💼 إعداد المستشار", "منصور أحمد سعيد")

    st.markdown("### 🔍 تفاصيل التقرير الاستراتيجية")
    
    q1 = st.text_area("1. ما هي الأهداف المحققة في هذه الفترة؟")
    q2 = st.text_area("2. أبرز التحديات التي واجهت سير العمل؟")
    q3 = st.text_area("3. التوصيات والخطوات القادمة؟")

    if st.button("💎 توليد التقرير الماسي"):
        if project_name and q1:
            full_content = f"""
            الجهة: {project_name}
            النوع: {report_type}
            المستشار: {prepared_by}
            تاريخ التقرير: {date_now}
            
            الأهداف المحققة:
            {q1}
            
            التحديات المرصودة:
            {q2}
            
            التوصيات الاستراتيجية:
            {q3}
            """
            
            st.success("✅ تم صياغة التقرير بنجاح")
            st.text_area("📄 المعاينة النهائية", full_content, height=250)
            
            # زر التحميل
            pdf_path = create_pdf(project_name, full_content)
            with open(pdf_path, "rb") as f:
                st.download_button("📥 تحميل التقرير بصيغة PDF", f, file_name=f"{project_name}.pdf")
        else:
            st.error("⚠️ فضلاً املأ البيانات الأساسية أولاً")
            
    st.markdown('</div>', unsafe_allow_html=True)

# ================== تذييل المنصة ==================
st.markdown("<br><center>🛡️ جميع الحقوق محفوظة لشبكة المنصور للاستشارات 2026</center>", unsafe_allow_html=True)
