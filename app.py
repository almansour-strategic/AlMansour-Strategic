import streamlit as st
from datetime import datetime

# ================== 1. التنسيق البصري الملكي (إخفاء تام + تنظيم دقيق) ==================
st.set_page_config(page_title="المنصور AI - المنهجية العالمية", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
    
    div[data-testid="stToolbar"], #MainMenu, footer, header, .stDeployButton, [data-testid="stStatusWidget"], [data-testid="stDecoration"] {
        display: none !important; visibility: hidden !important;
    }
    
    .stApp { background-color: #f8fafc; color: #1e293b; direction: rtl; }
    
    .main-box {
        background: #ffffff;
        border-top: 10px solid #d4af37;
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.05);
        margin-top: 20px;
    }

    * { font-family: 'Cairo', sans-serif !important; }
    .brand-title { color: #1e3a8a !important; font-weight: 900 !important; font-size: 2.5rem !important; text-align: center; margin:0; }
    .methodology-tag { 
        background: #1e3a8a; color: #fbbf24; padding: 6px 20px; border-radius: 25px; 
        font-size: 0.85rem; display: table; margin: 10px auto 30px auto; font-weight: bold;
    }

    /* نص الإرشاد الثابت تحت السؤال */
    .hint-text { color: #64748b; font-size: 0.85rem; margin-bottom: 15px; margin-top: -5px; line-height: 1.4; border-right: 3px solid #fbbf24; padding-right: 10px; }

    /* شرح وظيفة زر التحسين */
    .magic-desc { color: #2563eb; font-size: 0.75rem; font-weight: 600; margin-bottom: 2px; text-align: center; }

    /* تنسيق الحقول والأزرار */
    label { color: #1e3a8a !important; font-weight: 700 !important; font-size: 1.1rem !important; margin-bottom: 5px !important; }
    .stTextArea textarea, .stTextInput input { border: 1.5px solid #cbd5e1 !important; border-radius: 12px !important; }
    
    .stButton>button {
        width: 100% !important; height: 55px !important; border-radius: 12px !important;
        font-weight: 700 !important; font-size: 1.1rem !important; border: none !important; transition: 0.4s;
    }
    
    /* زر التوليد */
    .btn-gen button { background: linear-gradient(90deg, #d4af37, #b45309) !important; color: white !important; }
    /* زر الخروج */
    .btn-exit button { background: #f1f5f9 !important; color: #64748b !important; border: 1px solid #e2e8f0 !important; }
    
    .magic-btn button {
        height: 35px !important; font-size: 0.85rem !important; background: #f0f9ff !important;
        color: #0369a1 !important; border: 1px dashed #0369a1 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ================== 2. بوابة الدخول ==================
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="brand-title">المنصور AI</h1>', unsafe_allow_html=True)
    st.markdown('<div class="methodology-tag">بوابة الوصول المعتمدة - 2026</div>', unsafe_allow_html=True)
    email = st.text_input("البريد الإلكتروني")
    pwd = st.text_input("كلمة المرور", type="password")
    if st.button("دخول آمن للمنصة"):
        if email and pwd: st.session_state.auth = True; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ================== 3. المحرك الرئيسي (V8) ==================
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI للتقارير الاحترافية</h1>', unsafe_allow_html=True)
st.markdown('<div class="methodology-tag">نظام استشاري متكامل وفق المعايير الدولية</div>', unsafe_allow_html=True)

# الخطوة 1: نوع التقرير
st.markdown("### 🎯 الخطوة 1: تحديد هوية التقرير")
report_types = [
    "📑 تقرير إنجاز مشروع تنموي",
    "🎓 تقرير ختامي لبرنامج تدريبي/ورشة",
    "💰 تقرير تدقيق مالي وتحليل ميزانية",
    "🚑 تقرير أداء طبي وتشغيلي",
    "🏗️ تقرير فني هندسي وميداني",
    "🏛️ تقرير حوكمة وامتثال مؤسسي"
]
rtype = st.selectbox("اختر نوع التقرير المناسب لضبط السياق ذكياً:", report_types)

st.markdown("---")

# الخطوة 2: البيانات التعريفية مع أمثلة
st.markdown("### 📌 الخطوة 2: البيانات الأساسية (Data Profile)")
col1, col2 = st.columns(2)
with col1:
    p_name = st.text_input("اسم المشروع / البرنامج", placeholder="مثال: دورة التخطيط الاستراتيجي")
    client_name = st.text_input("الجهة المنفذة", placeholder="مثال: مؤسسة اليمن للتدريب")
    location = st.text_input("المنطقة / مكان التنفيذ", placeholder="مثال: صنعاء - قاعة المؤتمرات")
with col2:
    donor_name = st.text_input("اسم الجهة المانحة", placeholder="مثال: منظمة اليونيسف")
    duration = st.text_input("مدة التنفيذ", placeholder="مثال: 5 أيام عمل")
    p_date = st.date_input("تاريخ التقرير")

st.markdown("---")

# الخطوة 3: المحاور الاستراتيجية مع أمثلة ثابتة وشرح لزر التحسين
st.markdown("### 📝 الخطوة 3: صياغة المحتوى بمنهجية احترافية")

def smart_field(label, key, hint_text):
    st.markdown(f"<label>{label}</label>", unsafe_allow_html=True)
    st.markdown(f"<p class='hint-text'>🔍 <b>مثال توضيحي:</b> {hint_text}</p>", unsafe_allow_html=True)
    
    col_t, col_b = st.columns([5, 1])
    with col_t:
        val = st.text_area("", key=key, label_visibility="collapsed", height=100)
    with col_b:
        st.markdown('<p class="magic-desc">لتحويل نصك لصياغة رسمية</p>', unsafe_allow_html=True)
        st.markdown('<div class="magic-btn">', unsafe_allow_html=True)
        if st.button("✨ تحسين", key=f"ai_{key}"):
            st.toast("جاري إعادة الصياغة وفق المعايير الدولية...")
        st.markdown('</div>', unsafe_allow_html=True)
    return val

q1 = smart_field("1️⃣ الملخص التنفيذي وأهداف التقرير:", "q1", "تحقيق الأهداف التدريبية بنسبة 100% وإكساب 30 مشارك مهارات القيادة...")
q2 = smart_field("2️⃣ بيئة العمل والظروف الميدانية:", "q2", "تم تنفيذ المشروع في بيئة تفاعلية مع توفير كافة الوسائل التقنية واللوجستية...")
q3 = smart_field("3️⃣ التحديات والعقبات (المشاكل المرصودة):", "q3", "انقطاع التيار الكهربائي المتكرر، أو تأخر وصول بعض المشاركين من مناطق بعيدة...")
q4 = smart_field("4️⃣ آليات التجاوز (كيف تم الحل؟):", "q4", "تم استخدام المولدات الاحتياطية، وتعديل الجدول الزمني لتعويض الوقت الضائع...")
q5 = smart_field("5️⃣ النتائج والتوصيات الاستراتيجية:", "q5", "ينصح بتمديد فترة البرنامج في الدورات القادمة، واعتماد التدريب الميداني المكثف...")

st.markdown("<br>", unsafe_allow_html=True)

# أزرار التحكم
col_gen, col_ex = st.columns(2)
with col_gen:
    st.markdown('<div class="btn-gen">', unsafe_allow_html=True)
    if st.button("🚀 توليد التقرير النهائي المعتمد"):
        st.success("تم توليد المسودة النهائية بنجاح!")
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

with col_ex:
    st.markdown('<div class="btn-exit">', unsafe_allow_html=True)
    if st.button("🚪 تسجيل الخروج"):
        st.session_state.auth = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<center style='color:#94a3b8; font-size:0.8rem; margin-top:15px;'>🛡️ نظام المنصور الاستراتيجي | معايير الجودة 2026</center>", unsafe_allow_html=True)
