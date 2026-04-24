
import streamlit as st
from datetime import datetime

# ================== 1. التنسيق البصري الملكي (إخفاء تام + تنظيم دقيق) ==================
st.set_page_config(page_title="المنصور AI - المنهجية العالمية", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
    
    /* إخفاء تام لكل أدوات المنصة */
    div[data-testid="stToolbar"], #MainMenu, footer, header, .stDeployButton, [data-testid="stStatusWidget"] {
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

    /* تنسيق الحقول */
    label { color: #1e3a8a !important; font-weight: 700 !important; font-size: 1.1rem !important; margin-bottom: 5px !important; }
    .stTextArea textarea, .stTextInput input { 
        border: 1.5px solid #cbd5e1 !important; border-radius: 12px !important; 
        background: #ffffff !important; font-size: 1.1rem !important;
    }
    
    /* نص الإرشاد الثابت تحت السؤال */
    .hint-text { color: #64748b; font-size: 0.85rem; margin-bottom: 15px; margin-top: -5px; line-height: 1.4; border-right: 3px solid #fbbf24; padding-right: 10px; }

    /* الأزرار المتوازية */
    .stButton>button {
        width: 100% !important; height: 60px !important; border-radius: 15px !important;
        font-weight: 700 !important; font-size: 1.2rem !important; border: none !important; transition: 0.4s;
    }
    div[data-testid="stVerticalBlock"] > div:nth-child(16) button {
        background: linear-gradient(90deg, #d4af37, #b45309) !important; color: white !important;
    }
    div[data-testid="stVerticalBlock"] > div:nth-child(17) button {
        background: #f1f5f9 !important; color: #64748b !important; border: 1px solid #e2e8f0 !important;
    }
    
    .magic-btn button {
        height: 35px !important; font-size: 0.85rem !important; background: #f0f9ff !important;
        color: #0369a1 !important; border: 1px dashed #0369a1 !important; margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ================== 2. مصفوفة التقارير المتعمقة (منهجية المستشارين) ==================
REPORT_TYPES = {
    "📑 تقرير إنجاز مشاريع تنموية": {"hint": "نموذج الـ (LogFrame). ركز على المخرجات المباشرة والأثر المجتمعي المستدام."},
    "🎓 تقرير ختامي لبرامج تدريبية": {"hint": "نموذج (Kirkpatrick). ركز على تفاعل المشاركين، المهارات المكتسبة، وتقييم المدرب."},
    "💰 تقرير تدقيق مالي واستراتيجي": {"hint": "معايير (IFRS). ركز على الميزانية الفعلية مقابل المخطط وتحليل الانحرافات."},
    "🚑 تقرير طبي وتشغيلي": {"hint": "معايير (JCI). ركز على كفاءة الخدمة، سلامة المرضى، وإحصائيات الاستجابة."},
    "🏗️ تقرير فني وهندسي": {"hint": "معايير (FIDIC). ركز على المواصفات الفنية، الجداول الزمنية، واختبارات الجودة."},
    "🏛️ تقرير حوكمة وامتثال": {"hint": "ركز على مصفوفة المخاطر، والالتزام باللوائح والشفافية المؤسسية."}
}

# ================== 3. بوابة الدخول ==================
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="brand-title">المنصور AI</h1>', unsafe_allow_html=True)
    st.markdown('<div class="methodology-tag">بوابة الوصول المعتمدة - شبكة المستشارين</div>', unsafe_allow_html=True)
    email = st.text_input("البريد الإلكتروني")
    pwd = st.text_input("كلمة المرور", type="password")
    if st.button("دخول آمن للمنصة"):
        if email and pwd: st.session_state.auth = True; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ================== 4. المحرك الرئيسي ==================
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI للتقارير الاحترافية</h1>', unsafe_allow_html=True)
st.markdown('<div class="methodology-tag">نظام صياغة التقارير وفق المنهجية العالمية (PMBOK / ISO / Kirkpatrick)</div>', unsafe_allow_html=True)

# القسم الأول: البيانات التعريفية (حجر الزاوية)
st.markdown("### 📌 البيانات التعريفية للمشروع")
col1, col2 = st.columns(2)
with col1:
    p_name = st.text_input("اسم المشروع / البرنامج التدريبي")
    client_name = st.text_input("الجهة المنفذة / العميل")
    start_date = st.date_input("تاريخ بدء التنفيذ")
with col2:
    donor_name = st.text_input("اسم الجهة المانحة / الممول")
    location = st.text_input("مكان التنفيذ / المنطقة المستهدفة")
    duration = st.text_input("مدة التنفيذ (بالأيام/الأسابيع)")

rtype = st.selectbox("🎯 اختر تخصص التقرير لضبط المعايير:", list(REPORT_TYPES.keys()))
st.info(f"💡 **توصية المنهجية:** {REPORT_TYPES[rtype]['hint']}")

st.markdown("---")

# دالة الحقول المنهجية (تجمع بين السؤال، المثال الثابت، والأداة السحرية)
def smart_field(label, key, hint_text):
    st.markdown(f"<label>{label}</label>", unsafe_allow_html=True)
    st.markdown(f"<p class='hint-text'>🔍 <b>مثال توضيحي:</b> {hint_text}</p>", unsafe_allow_html=True)
    col_t, col_b = st.columns([5, 1])
    with col_t:
        val = st.text_area("", key=key, label_visibility="collapsed")
    with col_b:
        st.markdown('<div class="magic-btn">', unsafe_allow_html=True)
        if st.button("✨ تحسين", key=f"ai_{key}"):
            st.toast("جاري تحويل النص لصياغة عالمية...")
        st.markdown('</div>', unsafe_allow_html=True)
    return val

# الأسئلة المنهجية المكتملة
q1 = smart_field("1️⃣ الملخص التنفيذي وأهداف التقرير:", "q1", "تحقيق الأهداف الاستراتيجية للربع الأول بنسبة 95% وتعزيز قدرات 50 متدرب...")
q2 = smart_field("2️⃣ بيئة العمل والقيود الميدانية:", "q2", "تم العمل في ظروف جوية متقلبة مع الالتزام التام بمعايير السلامة المهنية...")
q3 = smart_field("3️⃣ التحديات والعقبات المرصودة:", "q3", "نقص في الكادر الفني المتخصص، وتأخر وصول الشحنة اللوجستية لمدة 3 أيام...")
q4 = smart_field("4️⃣ آليات التجاوز (الحلول المنفذة):", "q4", "تم استدعاء فريق الدعم الطارئ وتفعيل مخازن الاحتياط لضمان استمرارية العمل...")
q5 = smart_field("5️⃣ التوصيات والدروس المستفادة:", "q5", "ينصح بتبني نظام التوريد المسبق لتجنب التأخير في المشاريع القادمة...")

# عنصر الجماليات
st.markdown("### 📈 مؤشر الإنجاز الكلي")
progress = st.select_slider("حدد مستوى التقدم الكلي:", options=list(range(0, 101, 10)), value=60)
st.progress(progress / 100)

st.markdown("<br>", unsafe_allow_html=True)

# الأزرار المتوازية
col_gen, col_ex = st.columns(2)
with col_gen:
    if st.button("🚀 توليد التقرير الماسي"):
        st.success("تم التوليد بنجاح!")
        st.balloons()

with col_ex:
    if st.button("🚪 تسجيل الخروج"):
        st.session_state.auth = False
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<center style='color:#94a3b8; font-size:0.8rem; margin-top:15px;'>🛡️ شبكة المنصور للاستشارات | إدارة البيانات 2026</center>", unsafe_allow_html=True)
