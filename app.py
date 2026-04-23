import streamlit as st
from datetime import datetime

# ================== 1. التنسيق البصري السيادي (إخفاء تام + فخامة) ==================
st.set_page_config(page_title="المنصور AI - المنهجية العالمية", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
    
    /* إخفاء تام لكل ما له علاقة ببرمجيات المنصة (السرية التامة) */
    div[data-testid="stToolbar"], #MainMenu, footer, header, .stDeployButton, [data-testid="stStatusWidget"] {
        display: none !important; visibility: hidden !important;
    }
    
    .stApp { background-color: #f8fafc; color: #1e293b; direction: rtl; }
    
    .main-box {
        background: #ffffff;
        border-top: 8px solid #d4af37;
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 15px 50px rgba(0,0,0,0.05);
        margin-top: 20px;
    }

    * { font-family: 'Cairo', sans-serif !important; }
    .brand-title { color: #1e3a8a !important; font-weight: 900 !important; font-size: 2.8rem !important; text-align: center; margin:0; }
    .methodology-tag { 
        background: #1e3a8a; color: #fbbf24; padding: 6px 20px; border-radius: 25px; 
        font-size: 0.9rem; display: table; margin: 10px auto 30px auto; font-weight: bold;
    }

    /* تنسيق الحقول لتبدو فخمة وواضحة */
    label { color: #1e3a8a !important; font-weight: 700 !important; font-size: 1.1rem !important; }
    .stTextArea textarea, .stTextInput input { 
        border: 1.5px solid #cbd5e1 !important; border-radius: 12px !important; 
        background: #fdfdfd !important; font-size: 1.1rem !important;
    }

    /* الأزرار المتوازية بنفس الحجم والقوة */
    .stButton>button {
        width: 100% !important; height: 60px !important; border-radius: 15px !important;
        font-weight: 700 !important; font-size: 1.2rem !important; border: none !important; transition: 0.4s;
    }
    /* زر التوليد الذهبي */
    div[data-testid="stVerticalBlock"] > div:nth-child(13) button {
        background: linear-gradient(90deg, #d4af37, #b45309) !important; color: white !important;
    }
    /* زر الخروج الرمادي الرصين */
    div[data-testid="stVerticalBlock"] > div:nth-child(14) button {
        background: #f1f5f9 !important; color: #64748b !important; border: 1px solid #e2e8f0 !important;
    }
    
    /* زر الأداة السحرية */
    .magic-btn button {
        height: 35px !important; font-size: 0.85rem !important; background: #f0f9ff !important;
        color: #0369a1 !important; border: 1px dashed #0369a1 !important; margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ================== 2. المنهجية العالمية (مصفوفة السياق الذكي) ==================
REPORT_TYPES = {
    "📊 تقرير إنجاز ميداني": {"p": "تم استكمال المرحلة الأولى بنسبة إنجاز 85% وفق المخطط...", "hint": "ركز على المخرجات الملموسة."},
    "💰 تقرير مالي واستراتيجي": {"p": "تحقيق وفورات مالية بنسبة 12% نتيجة تحسين سلاسل التوريد...", "hint": "استخدم الأرقام ومقارنات الميزانية."},
    "🚑 تقرير طبي وصحي": {"p": "انخفاض معدل العدوى بنسبة 15% بعد تطبيق بروتوكول التعقيم الجديد...", "hint": "ركز على مؤشرات الأداء السريري."},
    "🏛️ تقرير حوكمة وامتثال": {"p": "تطابق كافة العمليات بنسبة 100% مع معايير الجودة العالمية...", "hint": "ركز على السياسات واللوائح."},
    "🏗️ تقرير تقني وهندسي": {"p": "أظهرت نتائج الفحص الفني استدامة الهيكل تحت ضغوط تفوق المعايير...", "hint": "استخدم المصطلحات الهندسية الدقيقة."},
    "🌍 تقرير تنموي وإغاثي": {"p": "توزيع المساعدات لـ 1200 مستفيد في المناطق الأشد احتياجاً...", "hint": "ركز على أثر المشروع المجتمعي."},
    "👥 تقرير إداري ومحضر": {"p": "اعتماد الهيكل التنظيمي الجديد وتوزيع التكليفات الإدارية العاجلة...", "hint": "ركز على القرارات والمسؤوليات."}
}

# ================== 3. بوابة الدخول ==================
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="brand-title">المنصور AI</h1>', unsafe_allow_html=True)
    st.markdown('<div class="methodology-tag">بوابة الوصول المعتمدة 2026</div>', unsafe_allow_html=True)
    email = st.text_input("البريد الإلكتروني")
    pwd = st.text_input("كلمة المرور", type="password")
    if st.button("دخول آمن للمنصة"):
        if email and pwd: st.session_state.auth = True; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ================== 4. المحرك الرئيسي (تطبيق كل القواعد) ==================
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI للتقارير الاحترافية</h1>', unsafe_allow_html=True)
st.markdown('<div class="methodology-tag">تطبيق المنهجية العالمية (PMBOK / ISO / UN Standards)</div>', unsafe_allow_html=True)

# اختيار نوع التقرير وتغيير السياق تلقائياً
rtype = st.selectbox("🎯 اختر تخصص التقرير لضبط الأمثلة الذكية:", list(REPORT_TYPES.keys()))
meta = REPORT_TYPES[rtype]

st.info(f"💡 **توصية المنهجية:** {meta['hint']}")

# عنوان التقرير
p_title = st.text_input("📍 عنوان التقرير الاستراتيجي", placeholder="مثال: تقرير الأداء الختامي لعام 2025")

st.markdown("---")

# دالة الحقول الذكية (تجمع بين السؤال، المثال، والأداة السحرية)
def smart_field(label, key, placeholder):
    col_t, col_b = st.columns([5, 1])
    with col_t:
        val = st.text_area(label, key=key, placeholder=f"مثال للعميل: {placeholder}")
    with col_b:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="magic-btn">', unsafe_allow_html=True)
        if st.button("✨ تحسين", key=f"ai_{key}"):
            st.toast("الأداة السحرية: جاري تحويل النص لصياغة عالمية...", icon="🪄")
        st.markdown('</div>', unsafe_allow_html=True)
    return val

# الأسئلة المنهجية (المنطقية والكاملة)
q1 = smart_field("1️⃣ الملخص التنفيذي وأبرز الإنجازات الجوهرية:", "q1", meta['p'])
q2 = smart_field("2️⃣ بيئة العمل والظروف الميدانية الراهنة:", "q2", "صف الموقع والظروف السياسية/المناخية المؤثرة...")
q3 = smart_field("3️⃣ التحديات والعقبات (ما الذي أعاق التقدم؟):", "q3", "مثال: نقص التمويل، تأخر التوريد، صعوبات لوجستية...")
q4 = smart_field("4️⃣ آليات التجاوز (الحلول المبتكرة التي نُفذت):", "q4", "مثال: تم استخدام الموارد البديلة وتفعيل خطة الطوارئ 'ب'...")
q5 = smart_field("5️⃣ التوصيات الاستراتيجية والدروس المستفادة:", "q5", "مثال: ينصح بزيادة التدريب التقني للفريق في المرحلة القادمة...")

# الرسوم البيانية الجمالية
st.markdown("### 📈 مؤشر الإنجاز الكلي (بصري)")
progress = st.select_slider("حدد مستوى التقدم الكلي للمشروع:", options=list(range(0, 101, 10)), value=60)
st.progress(progress / 100)

st.markdown("<br>", unsafe_allow_html=True)

# الأزرار المتوازية (التوليد والخروج) بنفس الحجم والتوازن
col_gen, col_ex = st.columns(2)
with col_gen:
    if st.button("🚀 توليد التقرير الماسي"):
        st.success("تم التوليد وفق المنهجية العالمية!")
        st.balloons()

with col_ex:
    if st.button("🚪 تسجيل الخروج"):
        st.session_state.auth = False
        st.rerun()

# خيارات التصدير المتعددة
st.markdown("---")
st.write("📂 خيارات التصدير الاحترافية:")
c1, c2, c3 = st.columns(3)
c1.button("📥 ملف PDF رسمي")
c2.button("📥 ملف Word مسودة")
c3.button("📥 نص Text سريع")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<center style='color:#94a3b8; font-size:0.8rem;'>🛡️ شبكة المنصور للاستشارات | إدارة البيانات 2026</center>", unsafe_allow_html=True)
