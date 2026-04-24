import streamlit as st
from datetime import datetime
from docx import Document
from io import BytesIO

# ================== 1. الهوية البصرية الملكية ==================
st.set_page_config(page_title="المنصور AI - V21 التشغيلي", layout="centered")

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
.magic-desc { color: #2563eb; font-size: 0.72rem; font-weight: 600; text-align: center; margin-bottom: 4px; }
.btn-gen button { background: linear-gradient(90deg, #1e3a8a, #d4af37) !important; color: white !important; font-weight: 700 !important; height: 58px !important; border-radius: 12px !important; width: 100% !important; border:none !important; }
.btn-ai button { background: #eff6ff !important; color: #1e3a8a !important; border: 1px dashed #1e3a8a !important; height: 35px !important; font-size: 0.8rem !important; }
</style>
""", unsafe_allow_html=True)

# ================== 2. المنهجية العالمية (8 تخصصات سيادية) ==================
GLOBAL_REPORTS = {
    "📑 تقرير الإنجاز الدوري | Progress Report": ["ملخص التنفيذ", "تحليل الانحرافات", "إدارة التحديات", "آليات التجاوز"],
    "🎓 تقرير ختامي لتدريب | Capacity Building": ["نتائج التقييم", "كفاءة المنهجية", "تفاعل المشاركين", "استدامة الأثر"],
    "💰 تقرير الأداء المالي | Financial Report": ["تحليل المصروفات", "انحرافات التكلفة", "الامتثال والتدقيق", "توصيات الكفاءة"],
    "📊 تقرير المتابعة والتقييم | M&E Report": ["مؤشرات الأداء", "جودة المخرجات", "الدروس المستفادة", "فرص التحسين"],
    "🚑 تقرير تقييم الاحتياجات | Needs Assessment": ["تحليل الفجوة", "الفئات المستهدفة", "الأولويات العاجلة", "توصيات التدخل"],
    "🏛️ تقرير الحوكمة والامتثال | Compliance": ["الالترام باللوائح", "نتائج الرقابة", "الثغرات المرصودة", "إجراءات التصحيح"],
    "🌍 تقرير الأثر البيئي والاجتماعي | ESIA": ["الأثر البيئي", "المسؤولية المجتمعية", "إجراءات التخفيف", "الاستدامة"],
    "🏗️ تقرير فني وهندسي | Technical Report": ["المواصفات الفنية", "اختبارات الجودة", "المعوقات التقنية", "الحلول المنفذة"]
}

# ================== 3. وظائف التشغيل الحقيقية ==================

# محرك تحسين النص (Logic-based Enhancement)
def enhance_text(text, context):
    if not text: return ""
    # هنا قمنا ببرمجة محرك صياغة رسمي يحول الكلمات العادية إلى مصطلحات استشارية
    formal_words = {
        "سوينا": "قمنا بتنفيذ", "مشكلة": "تحدي استراتيجي", "حل": "معالجة جذرية",
        "تأخرنا": "حدث انحراف زمني", "كويس": "وفق معايير الجودة"
    }
    for word, formal in formal_words.items():
        text = text.replace(word, formal)
    return f"بناءً على منهجية {context}: {text}. تم ضبط المخرجات لتتوافق مع المعايير الدولية."

# محرك توليد Word الفعلي
def generate_docx(report_data):
    doc = Document()
    doc.add_heading(f"تقرير {report_data['type']}", 0)
    doc.add_paragraph(f"المشروع: {report_data['p_name']}")
    doc.add_paragraph(f"الجهة المانحة: {report_data['donor']}")
    doc.add_paragraph(f"تاريخ التقرير: {datetime.now().strftime('%Y-%m-%d')}")
    
    for key, value in report_data['content'].items():
        doc.add_heading(key, level=1)
        doc.add_paragraph(value if value else "لا يوجد بيانات متوفرة لهذا المحور")
        
    bio = BytesIO()
    doc.save(bio)
    bio.seek(0)
    return bio

# ================== 4. الواجهة والمنطق التشغيلي ==================
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.title("المنصور AI - دخول")
    u = st.text_input("البريد")
    p = st.text_input("كلمة المرور", type="password")
    if st.button("دخول"):
        st.session_state.auth = True
        st.rerun()
    st.stop()

st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI - المحرك الاستراتيجي</h1>', unsafe_allow_html=True)

rtype = st.selectbox("🎯 اختر تخصص التقرير:", list(GLOBAL_REPORTS.keys()))
fields = GLOBAL_REPORTS[rtype]

st.markdown('<p class="section-title">بيانات المشروع</p>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
p_name = c1.text_input("اسم المشروع *")
donor = c2.text_input("الجهة المانحة")

st.markdown('<p class="section-title">المحاور الاستراتيجية</p>', unsafe_allow_html=True)
user_responses = {}

for i, field in enumerate(fields):
    st.markdown(f"<label>{field}</label>", unsafe_allow_html=True)
    col_t, col_b = st.columns([4, 1.5])
    
    # الذاكرة المستمرة لكل حقل
    key_name = f"input_{rtype}_{i}"
    txt = col_t.text_area("", key=key_name, height=100, label_visibility="collapsed")
    user_responses[field] = txt
    
    with col_b:
        st.markdown('<p class="magic-desc">تحسين الصياغة</p>', unsafe_allow_html=True)
        if st.button("✨ تحسين", key=f"ai_btn_{i}"):
            if txt:
                improved = enhance_text(txt, rtype)
                st.session_state[key_name] = improved
                st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 توليد ومعالجة ملف Word النهائي"):
    if p_name:
        report_data = {
            "type": rtype,
            "p_name": p_name,
            "donor": donor,
            "content": user_responses
        }
        word_file = generate_docx(report_data)
        st.success("تم تجهيز التقرير بنجاح!")
        st.download_button(
            label="📥 تحميل ملف Word المعتمد",
            data=word_file,
            file_name=f"{p_name}_Report.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    else:
        st.error("⚠️ يرجى إدخال اسم المشروع")

st.markdown('</div>', unsafe_allow_html=True)
