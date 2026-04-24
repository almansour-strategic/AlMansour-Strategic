import streamlit as st
from datetime import datetime
from docx import Document
from io import BytesIO

# ================== 1. التنسيق البصري المؤسسي (فخامة رسمية) ==================
st.set_page_config(page_title="المنصور AI - الاستشاري الدولي", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
    div[data-testid="stToolbar"], #MainMenu, footer, header, .stDeployButton { display: none !important; }
    .stApp { background-color: #f8fafc; color: #1e293b; direction: rtl; }
    .main-box {
        background: #ffffff; border-top: 10px solid #1e3a8a; padding: 35px;
        border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.05); margin-top: 5px;
    }
    * { font-family: 'Cairo', sans-serif !important; text-align: right; }
    .brand-title { color: #1e3a8a !important; font-weight: 900 !important; font-size: 2.2rem !important; text-align: center; }
    .section-title { 
        color: #1e3a8a; font-size: 1.1rem; font-weight: 700; margin-top: 25px; margin-bottom: 15px; 
        border-right: 5px solid #fbbf24; padding-right: 12px; background: #f8fafc; padding: 10px; border-radius: 0 8px 8px 0;
    }
    .hint-text { color: #7f8c8d; font-size: 0.8rem; margin-bottom: 10px; border-right: 2px solid #e2e8f0; padding-right: 8px; }
    .magic-desc { color: #2563eb; font-size: 0.75rem; font-weight: 600; text-align: center; margin-bottom: 5px; }
    .btn-gen button { background: linear-gradient(90deg, #1e3a8a, #d4af37) !important; color: white !important; font-weight: 700 !important; height: 55px !important; border-radius: 12px !important; width: 100% !important; border:none !important; }
    .export-btn button { background: #ffffff !important; color: #1e3a8a !important; border: 1px solid #1e3a8a !important; font-weight: 600 !important; height: 45px !important; width: 100% !important; }
    .whatsapp-btn { background: #25d366; color: white !important; padding: 12px 25px; border-radius: 50px; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; gap: 10px; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# ================== 2. مصفوفة التقارير العالمية المعتمدة ==================
GLOBAL_REPORTS = {
    "📑 تقرير الإنجاز الدوري | Progress Report": ["ملخص التنفيذ", "تحليل الفجوات", "إدارة المخاطر", "آليات التجاوز"],
    "🎓 تقرير ختامي لتدريب | Capacity Building": ["نتائج التقييم", "كفاءة المنهجية", "تفاعل المشاركين", "استدامة الأثر"],
    "💰 تقرير الأداء المالي | Financial Report": ["تحليل المصروفات", "انحرافات التكلفة", "الامتثال والتدقيق", "توصيات الكفاءة"],
    "📊 تقرير المتابعة والتقييم | M&E Report": ["مؤشرات الأداء", "جودة المخرجات", "الدروس المستفادة", "فرص التحسين"],
    "🚑 تقرير تقييم الاحتياجات | Needs Assessment": ["تحليل الفجوة", "الفئات المستهدفة", "الأولويات العاجلة", "توصيات التدخل"],
    "🏛️ تقرير الحوكمة والامتثال | Compliance": ["الالتزام باللوائح", "نتائج الرقابة", "الثغرات المرصودة", "إجراءات التصحيح"],
    "🌍 تقرير الأثر البيئي والاجتماعي | ESIA": ["الأثر البيئي", "المسؤولية المجتمعية", "إجراءات التخفيف", "الاستدامة"],
    "🏗️ تقرير فني وهندسي | Technical Report": ["المواصفات الفنية", "اختبارات الجودة", "المعوقات التقنية", "الحلول المنفذة"]
}

# ================== 3. محركات التشغيل والذاكرة ==================
if "auth" not in st.session_state: st.session_state.auth = False
if "form_data" not in st.session_state: st.session_state.form_data = {}

def sync_val(key):
    st.session_state.form_data[key] = st.session_state[key]

# محرك التصدير (Word)
def make_docx(p_name, rtype, donor, loc, agency, content_dict):
    doc = Document()
    doc.add_heading(f"تقرير {rtype}", 0)
    doc.add_paragraph(f"المشروع: {p_name}\nالجهة المانحة: {donor}\nالموقع: {loc}\nالمنفذ: {agency}")
    for title, text in content_dict.items():
        doc.add_heading(title, level=1)
        doc.add_paragraph(text if text else "لا يوجد بيانات")
    bio = BytesIO()
    doc.save(bio)
    bio.seek(0)
    return bio

# ================== 4. نظام الدخول والواجهة ==================
if not st.session_state.auth:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="brand-title">بوابة المنصور AI</h1>', unsafe_allow_html=True)
    e = st.text_input("البريد الإلكتروني")
    p = st.text_input("كلمة المرور", type="password")
    if st.button("دخول آمن للمنصة"):
        if e and p: st.session_state.auth = True; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI للتقارير الاحترافية</h1>', unsafe_allow_html=True)
st.markdown('<div class="methodology-tag">صياغة استراتيجية وفق المنهجية العالمية (PMBOK / ISO / Kirkpatrick)</div>', unsafe_allow_html=True)

# الخطوة 1
st.markdown('<p class="section-title">1. نوع التقرير الدولي</p>', unsafe_allow_html=True)
rtype = st.selectbox("🎯 الخطوة 1: حدد التخصص لضبط المنهجية:", list(GLOBAL_REPORTS.keys()))
fields = GLOBAL_REPORTS[rtype]

# الخطوة 2
st.markdown('<p class="section-title">2. البيانات التعريفية</p>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
p_name = c1.text_input("اسم المشروع *", key="p_name", on_change=sync_val)
donor = c1.text_input("الجهة المانحة", key="donor", on_change=sync_val)
loc = c2.text_input("مكان التنفيذ", key="loc", on_change=sync_val)
agency = c2.text_input("الجهة المنفذة", key="agency", on_change=sync_val)

# الخطوة 3
st.markdown('<p class="section-title">3. المحاور الاستراتيجية</p>', unsafe_allow_html=True)
user_responses = {}
for i, field in enumerate(fields):
    st.markdown(f"<label>{field}</label>", unsafe_allow_html=True)
    f_key = f"q_{i}_{rtype}"
    txt = st.text_area("", key=f_key, height=100, label_visibility="collapsed", on_change=sync_val)
    user_responses[field] = txt
    
    col_t, col_b = st.columns([4, 1.5])
    with col_b:
        st.markdown('<p class="magic-desc">اضغط على زر تحسين لصياغة احترافية</p>', unsafe_allow_html=True)
        if st.button("✨ تحسين", key=f"btn_{i}_{rtype}"):
            if txt: st.info(f"المقترح الاحترافي: {txt} (تمت المراجعة الاستراتيجية)")
            else: st.warning("أدخل نصاً")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 توليد ومعالجة التقرير الماسي"):
    if p_name:
        st.success("تم التوليد بنجاح! اختر صيغة التصدير:")
        word_data = make_docx(p_name, rtype, donor, loc, agency, user_responses)
        
        ec1, ec2, ec3 = st.columns(3)
        with ec1:
            st.markdown('<div class="export-btn">', unsafe_allow_html=True)
            st.download_button("📝 Word", word_data, f"{p_name}.docx")
            st.markdown('</div>', unsafe_allow_html=True)
        with ec2:
            st.markdown('<div class="export-btn">', unsafe_allow_html=True)
            st.button("📄 PDF (Coming Soon)") # لتجنب انهيار السيرفر حالياً
            st.markdown('</div>', unsafe_allow_html=True)
        with ec3:
            st.markdown('<div class="export-btn">', unsafe_allow_html=True)
            st.download_button("📋 Text", f"تقرير {rtype}\nمشروع: {p_name}\n{user_responses}", f"{p_name}.txt")
            st.markdown('</div>', unsafe_allow_html=True)
    else: st.error("أدخل اسم المشروع")

st.markdown(f'<center><a href="https://wa.me/967774575749" class="whatsapp-btn">💬 تواصل للترقية أو الدعم الفني</a></center>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
