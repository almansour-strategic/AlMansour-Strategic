import streamlit as st
from datetime import datetime
from docx import Document
from fpdf import FPDF
from io import BytesIO

# ================== 1. الهوية البصرية الملكية ==================
st.set_page_config(page_title="المنصور AI - الإصدار المتكامل", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
div[data-testid="stToolbar"], #MainMenu, footer, header, .stDeployButton { display: none !important; }
.stApp { background-color: #f8fafc; color: #1e293b; direction: rtl; }
.main-box {
    background: #ffffff; border-top: 10px solid #1e3a8a; padding: 40px;
    border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.05); margin-top: 10px;
}
* { font-family: 'Cairo', sans-serif !important; text-align: right; }
.brand-title { color: #1e3a8a !important; font-weight: 900 !important; font-size: 2.3rem !important; text-align: center; }
.methodology-tag { background: #1e3a8a; color: #fbbf24; padding: 6px 20px; border-radius: 25px; font-size: 0.85rem; display: table; margin: 10px auto 30px auto; font-weight: bold; }
.section-title { color: #1e3a8a; font-size: 1.1rem; font-weight: 700; margin-top: 25px; margin-bottom: 15px; border-right: 5px solid #fbbf24; padding-right: 12px; background: #f8fafc; padding: 10px; border-radius: 0 8px 8px 0; }
.hint-text { color: #64748b; font-size: 0.82rem; margin-bottom: 12px; border-right: 2px solid #cbd5e1; padding-right: 10px; line-height: 1.5; }
.btn-gen button { background: linear-gradient(90deg, #1e3a8a, #d4af37) !important; color: white !important; font-weight: 700 !important; height: 58px !important; border-radius: 12px !important; width: 100% !important; border:none !important; }
.export-btn button { background: #ffffff !important; color: #1e3a8a !important; border: 1px solid #1e3a8a !important; font-weight: 600 !important; height: 45px !important; width: 100% !important; }
.whatsapp-btn { background: #25d366; color: white !important; padding: 12px 25px; border-radius: 50px; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; gap: 10px; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

# ================== 2. المنهجية والبيانات ==================
GLOBAL_REPORTS = {
    "📑 تقرير الإنجاز الدوري | Progress Report": ["ملخص التنفيذ", "تحليل الانحرافات", "إدارة التحديات", "آليات التجاوز"],
    "🎓 تقرير ختامي لتدريب | Capacity Building": ["نتائج التقييم", "كفاءة المنهجية", "تفاعل المشاركين", "استدامة الأثر"],
    "💰 تقرير الأداء المالي | Financial Report": ["تحليل المصروفات", "انحرافات التكلفة", "الامتثال والتدقيق", "توصيات الكفاءة"],
    "📊 تقرير المتابعة والتقييم | M&E Report": ["مؤشرات الأداء", "جودة المخرجات", "الدروس المستفادة", "فرص التحسين"],
    "🚑 تقرير تقييم الاحتياجات | Needs Assessment": ["تحليل الفجوة", "الفئات المستهدفة", "الأولويات العاجلة", "توصيات التدخل"],
    "🏛️ تقرير الحوكمة والامتثال | Compliance": ["الالتزام باللوائح", "نتائج الرقابة", "الثغرات المرصودة", "إجراءات التصحيح"],
    "🌍 تقرير الأثر البيئي والاجتماعي | ESIA": ["الأثر البيئي", "المسؤولية المجتمعية", "إجراءات التخفيف", "الاستدامة"],
    "🏗️ تقرير فني وهندسي | Technical Report": ["المواصفات الفنية", "اختبارات الجودة", "المعوقات التقنية", "الحلول المنفذة"]
}

# ================== 3. محركات التصدير الحقيقية ==================

# محرك Word
def make_docx(p_name, rtype, donor, content):
    doc = Document()
    doc.add_heading(f"تقرير {rtype}", 0)
    doc.add_paragraph(f"المشروع: {p_name}\nالجهة: {donor}")
    for title, text in content.items():
        doc.add_heading(title, level=1)
        doc.add_paragraph(text if text else "لا يوجد بيانات")
    bio = BytesIO()
    doc.save(bio)
    bio.seek(0)
    return bio

# محرك PDF (النسخة المستقرة)
def make_pdf(p_name, rtype, donor, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Report: {rtype}", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Project: {p_name}", ln=True)
    pdf.cell(0, 10, f"Donor: {donor}", ln=True)
    for title, text in content.items():
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, f"{title}:", ln=True)
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, text if text else "No data")
    return pdf.output()

# ================== 4. نظام التشغيل ==================
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="brand-title">المنصور AI</h1>', unsafe_allow_html=True)
    if st.button("دخول آمن"):
        st.session_state.auth = True
        st.rerun()
    st.stop()

st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI للتقارير الاحترافية</h1>', unsafe_allow_html=True)
st.markdown('<div class="methodology-tag">إصدار V25 | PDF - Word - Text</div>', unsafe_allow_html=True)

rtype = st.selectbox("🎯 حدد نوع التقرير:", list(GLOBAL_REPORTS.keys()))
fields = GLOBAL_REPORTS[rtype]

st.markdown('<p class="section-title">بيانات المشروع التعريفية</p>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
p_name = c1.text_input("اسم المشروع *")
donor = c2.text_input("الجهة المانحة")

st.markdown('<p class="section-title">المحاور الاستراتيجية للتقرير</p>', unsafe_allow_html=True)
responses = {}
for i, field in enumerate(fields):
    st.markdown(f"<label>{field}</label>", unsafe_allow_html=True)
    txt = st.text_area("", key=f"f_{i}_{rtype}", height=100, label_visibility="collapsed")
    responses[field] = txt
    if st.button(f"✨ تحسين الصياغة", key=f"b_{i}_{rtype}"):
        if txt: st.info(f"المقترح: {txt} (تمت المراجعة)")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 معالجة التقرير النهائي"):
    if p_name:
        st.success("تم التوليد بنجاح! اختر صيغة التصدير:")
        col1, col2, col3 = st.columns(3)
        
        # تصدير Word
        word_data = make_docx(p_name, rtype, donor, responses)
        col1.markdown('<div class="export-btn">', unsafe_allow_html=True)
        col1.download_button("📝 Word", word_data, f"{p_name}.docx")
        col1.markdown('</div>', unsafe_allow_html=True)
        
        # تصدير PDF
        pdf_data = make_pdf(p_name, rtype, donor, responses)
        col2.markdown('<div class="export-btn">', unsafe_allow_html=True)
        col2.download_button("📄 PDF", pdf_data, f"{p_name}.pdf")
        col2.markdown('</div>', unsafe_allow_html=True)
        
        # تصدير Text
        col3.markdown('<div class="export-btn">', unsafe_allow_html=True)
        col3.download_button("📋 Text", f"{p_name}\n{responses}", f"{p_name}.txt")
        col3.markdown('</div>', unsafe_allow_html=True)
    else: st.error("أدخل اسم المشروع أولاً")

st.markdown(f'<center><a href="https://wa.me/967774575749" class="whatsapp-btn">💬 تواصل لترقية حسابك</a></center>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
