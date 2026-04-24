import streamlit as st
from datetime import datetime
from docx import Document
from io import BytesIO

# ================== 1. الهوية البصرية الملكية (إخفاء تام + رصانة) ==================
st.set_page_config(page_title="المنصور AI - V22 المستقر", layout="centered")

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
.section-title { color: #1e3a8a; font-size: 1.1rem; font-weight: 700; margin-top: 25px; margin-bottom: 15px; border-right: 5px solid #fbbf24; padding-right: 12px; background: #f8fafc; padding: 10px; border-radius: 0 8px 8px 0; }
.hint-text { color: #64748b; font-size: 0.82rem; margin-bottom: 12px; border-right: 2px solid #cbd5e1; padding-right: 10px; line-height: 1.5; }
.btn-gen button { background: linear-gradient(90deg, #1e3a8a, #d4af37) !important; color: white !important; font-weight: 700 !important; height: 58px !important; border-radius: 12px !important; width: 100% !important; border:none !important; }
.btn-ai button { background: #f0f9ff !important; color: #1e3a8a !important; border: 1px dashed #1e3a8a !important; height: 35px !important; font-size: 0.8rem !important; font-weight: bold !important; width: 100% !important; }
</style>
""", unsafe_allow_html=True)

# ================== 2. المنهجية العالمية (8 تخصصات سيادية كاملة) ==================
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

# ================== 3. المحركات التشغيلية (الحقيقية) ==================
def get_formal_text(text):
    if not text: return ""
    # محرك معالجة صياغة استشارية
    replacements = {"مشكلة": "تحدي استراتيجي", "حل": "معالجة منهجية", "تأخير": "انحراف في الجدول الزمني", "سوينا": "تم إنجاز"}
    for k, v in replacements.items(): text = text.replace(k, v)
    return f"بناءً على المنهجية المعتمدة: {text}. تم تنقيح النص لضمان المهنية العالية."

def generate_word(p_name, rtype, donor, content_dict):
    doc = Document()
    doc.add_heading(f"تقرير {rtype}", 0)
    doc.add_paragraph(f"المشروع: {p_name}")
    doc.add_paragraph(f"الجهة: {donor}")
    doc.add_paragraph(f"تاريخ الإصدار: {datetime.now().strftime('%Y-%m-%d')}")
    for title, text in content_dict.items():
        doc.add_heading(title, level=1)
        doc.add_paragraph(text if text else "بيانات غير متوفرة")
    bio = BytesIO()
    doc.save(bio)
    bio.seek(0)
    return bio

# ================== 4. نظام الدخول والواجهة المستقرة ==================
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.title("بوابة المنصور AI - دخول آمن")
    if st.button("اضغط للدخول إلى المنصة"):
        st.session_state.auth = True
        st.rerun()
    st.stop()

st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI - المحرك الاستراتيجي</h1>', unsafe_allow_html=True)

rtype = st.selectbox("🎯 حدد تخصص التقرير لضبط المنهجية:", list(GLOBAL_REPORTS.keys()))
fields = GLOBAL_REPORTS[rtype]

st.markdown('<p class="section-title">بيانات التعريف</p>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
p_name = c1.text_input("اسم المشروع *")
donor = c2.text_input("الجهة المانحة")

st.markdown('<p class="section-title">المحاور الاستراتيجية</p>', unsafe_allow_html=True)
user_data = {}

for i, field in enumerate(fields):
    st.markdown(f"<label>{field}</label>", unsafe_allow_html=True)
    txt = st.text_area("", key=f"area_{rtype}_{i}", height=120, label_visibility="collapsed")
    user_data[field] = txt
    
    col_empty, col_btn = st.columns([3, 1])
    with col_btn:
        st.markdown('<div class="btn-ai">', unsafe_allow_html=True)
        if st.button("✨ تحسين الصياغة", key=f"btn_{rtype}_{i}"):
            if txt:
                st.success("✅ الصياغة المقترحة:")
                st.code(get_formal_text(txt))
            else: st.warning("اكتب نصاً أولاً")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 توليد ومعالجة ملف Word النهائي"):
    if p_name:
        word_io = generate_word(p_name, rtype, donor, user_data)
        st.download_button(
            label="📥 تحميل ملف Word المعتمد",
            data=word_io,
            file_name=f"{p_name}_Strategic_Report.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    else: st.error("⚠️ يرجى إدخال اسم المشروع")

st.markdown('</div>', unsafe_allow_html=True)
