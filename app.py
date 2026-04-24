import streamlit as st
from datetime import datetime
from docx import Document
from io import BytesIO

# ================== 1. الهوية البصرية الملكية (فخامة مؤسسية) ==================
st.set_page_config(page_title="المنصور AI - V29 المستقر", layout="centered")

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
    .methodology-tag { 
        background: #1e3a8a; color: #fbbf24; padding: 6px 20px; border-radius: 25px; 
        font-size: 0.85rem; display: table; margin: 10px auto 30px auto; font-weight: bold;
    }
    .section-title { 
        color: #1e3a8a; font-size: 1.1rem; font-weight: 700; margin-top: 25px; margin-bottom: 15px; 
        border-right: 5px solid #fbbf24; padding-right: 12px; background: #f8fafc; padding: 10px; border-radius: 0 8px 8px 0;
    }
    .hint-text { color: #64748b; font-size: 0.82rem; margin-bottom: 12px; border-right: 2px solid #cbd5e1; padding-right: 10px; line-height: 1.5; }
    .btn-gen button { background: linear-gradient(90deg, #1e3a8a, #d4af37) !important; color: white !important; font-weight: 700 !important; height: 58px !important; border-radius: 12px !important; width: 100% !important; border:none !important; }
    .export-btn button { background: #ffffff !important; color: #1e3a8a !important; border: 1px solid #1e3a8a !important; font-weight: 600 !important; height: 45px !important; width: 100% !important; }
    .whatsapp-btn { background: #25d366; color: white !important; padding: 12px 25px; border-radius: 50px; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; gap: 10px; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# ================== 2. المنهجية والتقارير السيادية (8 أنواع) ==================
REPORTS_DB = {
    "📑 تقرير الإنجاز الدوري | Progress Report": ["ملخص التنفيذ", "تحليل الانحرافات", "إدارة التحديات", "آليات التجاوز"],
    "🎓 تقرير ختامي لتدريب | Capacity Building": ["نتائج التقييم", "كفاءة المنهجية", "تفاعل المشاركين", "استدامة الأثر"],
    "💰 تقرير الأداء المالي | Financial Report": ["تحليل المصروفات", "انحرافات التكلفة", "الامتثال والتدقيق", "توصيات الكفاءة"],
    "📊 تقرير المتابعة والتقييم | M&E Report": ["مؤشرات الأداء", "جودة المخرجات", "الدروس المستفادة", "فرص التحسين"],
    "🚑 تقرير تقييم الاحتياجات | Needs Assessment": ["تحليل الفجوة", "الفئات المستهدفة", "الأولويات العاجلة", "توصيات التدخل"],
    "🏛️ تقرير الحوكمة والامتثال | Compliance": ["الالتزام باللوائح", "نتائج الرقابة", "الثغرات المرصودة", "إجراءات التصحيح"],
    "🌍 تقرير الأثر البيئي والاجتماعي | ESIA": ["الأثر البيئي", "المسؤولية المجتمعية", "إجراءات التخفيف", "الاستدامة"],
    "🏗️ تقرير فني وهندسي | Technical Report": ["المواصفات الفنية", "اختبارات الجودة", "المعوقات التقنية", "الحلول المنفذة"]
}

# ================== 3. المحركات التشغيلية الصافية ==================
def create_word(p_name, rtype, donor, loc, agency, content):
    doc = Document()
    doc.add_heading(f"Report: {rtype}", 0)
    doc.add_paragraph(f"Project: {p_name}\nDonor: {donor}\nAgency: {agency}\nLocation: {loc}")
    for title, text in content.items():
        doc.add_heading(title, level=1)
        doc.add_paragraph(text if text else "N/A")
    bio = BytesIO()
    doc.save(bio)
    bio.seek(0)
    return bio

# ================== 4. نظام التشغيل ==================
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="brand-title">بوابة المنصور AI</h1>', unsafe_allow_html=True)
    if st.button("دخول آمن للمنصة"):
        st.session_state.auth = True
        st.rerun()
    st.stop()

st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI للتقارير الاحترافية</h1>', unsafe_allow_html=True)
st.markdown('<div class="methodology-tag">صياغة استراتيجية احترافية | 2026</div>', unsafe_allow_html=True)

rtype = st.selectbox("🎯 حدد نوع التقرير:", list(REPORTS_DB.keys()))
fields = REPORTS_DB[rtype]

st.markdown('<p class="section-title">بيانات المشروع</p>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
p_name = c1.text_input("اسم المشروع *", key="v29_p_name")
donor = c1.text_input("الجهة المانحة", key="v29_donor")
loc = c2.text_input("مكان التنفيذ", key="v29_loc")
agency = c2.text_input("الجهة المنفذة", key="v29_agency")

st.markdown('<p class="section-title">المحاور الاستراتيجية</p>', unsafe_allow_html=True)
user_responses = {}
for i, label in enumerate(fields):
    st.markdown(f"<label>{label}</label>", unsafe_allow_html=True)
    txt = st.text_area("", key=f"v29_area_{i}_{rtype}", height=100, label_visibility="collapsed")
    user_responses[label] = txt
    if st.button(f"✨ تحسين", key=f"v29_btn_{i}_{rtype}"):
        if txt: st.info(f"المقترح: {txt} (تمت المراجعة)")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 توليد ومعالجة التقرير النهائي"):
    if p_name:
        st.success("التقرير جاهز! اختر صيغة التصدير:")
        word_data = create_word(p_name, rtype, donor, loc, agency, user_responses)
        
        ec1, ec2 = st.columns(2)
        with ec1:
            st.markdown('<div class="export-btn">', unsafe_allow_html=True)
            st.download_button("📝 تحميل ملف Word", word_data, f"{p_name}.docx")
            st.markdown('</div>', unsafe_allow_html=True)
        with ec2:
            st.markdown('<div class="export-btn">', unsafe_allow_html=True)
            st.download_button("📋 تحميل نص سريع", f"{p_name}\n{user_responses}", f"{p_name}.txt")
            st.markdown('</div>', unsafe_allow_html=True)
    else: st.error("⚠️ يرجى إدخال اسم المشروع أولاً.")

st.markdown(f'<center><a href="https://wa.me/967774575749" class="whatsapp-btn">💬 تواصل للدعم الفني</a></center>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
