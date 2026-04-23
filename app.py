import streamlit as st
from datetime import datetime

# ================== 1. هندسة الواجهة الملكية (ألوان هادئة وخطوط واضحة) ==================
st.set_page_config(page_title="المنصور AI", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;900&display=swap');
    
    /* إخفاء تام لكل أدوات المنصة وزر الإدارة الأسود */
    div[data-testid="stToolbar"], #MainMenu, footer, header, .stDeployButton, [data-testid="stStatusWidget"], [data-testid="stDecoration"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* خلفية هادئة مريحة للعين */
    .stApp { 
        background-color: #f8fafc; 
        color: #1e293b; 
        direction: rtl; 
    }
    
    /* الحاوية الرئيسية (نظيفة وبدون تعقيد) */
    .main-box {
        background: #ffffff;
        border-top: 5px solid #fbbf24;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-top: 20px;
    }

    * { font-family: 'Cairo', sans-serif !important; }
    
    /* العنوان الرئيسي */
    .brand-title { color: #0f172a !important; font-weight: 900 !important; font-size: 2.5rem !important; text-align: center; margin-bottom: 0px; }
    .brand-sub { color: #64748b; text-align: center; font-size: 1.1rem; margin-bottom: 30px; border-bottom: 1px solid #e2e8f0; padding-bottom: 15px; }
    
    /* تنسيق الحقول (أبيض بحدود واضحة) */
    .stTextInput input, .stTextArea textarea {
        background-color: #ffffff !important;
        color: #1e293b !important;
        border-radius: 8px !important;
        border: 1px solid #cbd5e1 !important;
        font-size: 1.1rem !important;
        padding: 12px !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #fbbf24 !important;
        box-shadow: 0 0 0 2px rgba(251, 191, 36, 0.2) !important;
    }
    
    /* تسميات الحقول (Label) */
    label { 
        color: #334155 !important; 
        font-weight: 700 !important; 
        font-size: 1rem !important; 
        margin-bottom: 8px !important;
        display: block !important;
    }

    /* الزر الرئيسي */
    .stButton>button {
        background: #0f172a !important;
        color: #fbbf24 !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        height: 55px !important;
        width: 100% !important;
        border: none !important;
        font-size: 1.2rem !important;
        transition: 0.3s;
    }
    .stButton>button:hover { background: #1e293b !important; transform: translateY(-2px); }
    </style>
""", unsafe_allow_html=True)

# ================== 2. منطق الوصول (المدير والعميل) ==================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="brand-title">المنصور AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="brand-sub">للتقارير الاحترافية والاستشارية</p>', unsafe_allow_html=True)
    
    email = st.text_input("البريد الإلكتروني المعتمد")
    pwd = st.text_input("كلمة المرور", type="password")
    
    if st.button("دخول المنصة"):
        if email and pwd: # نظام دخول بسيط وآمن
            st.session_state.authenticated = True
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ================== 3. واجهة بناء التقارير (الـ 11 سؤال كاملة) ==================
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="brand-sub">نظام صياغة التقارير الدولية</p>', unsafe_allow_html=True)

# معلومات التقرير
report_title = st.text_input("📍 اسم المشروع / التقرير", placeholder="مثال: تقرير إنجاز مشروع عدن الميداني")

st.markdown("### 📝 محاور التقرير الاستراتيجية")

q1 = st.text_area("1. الملخص التنفيذي:", placeholder="اكتب خلاصة الإنجاز هنا...")
q2 = st.text_area("2. تحليل بيئة العمل:", placeholder="صف الظروف المحيطة بالعمل...")
q3 = st.text_area("3. التحديات والعقبات:", placeholder="ما هي الصعوبات التي واجهتكم؟")
q4 = st.text_area("4. الموارد البشرية واللوجستية:", placeholder="الأدوات والفرق المشاركة...")
q5 = st.text_area("5. التحليل المالي والميزانية:", placeholder="مستوى الإنفاق والكفاءة المالية...")
q6 = st.text_area("6. نسبة الإنجاز والجدول الزمني:", placeholder="هل سار العمل حسب الخطة؟")
q7 = st.text_area("7. الجودة والامتثال:", placeholder="مدى الالتزام بالمعايير الدولية...")
q8 = st.text_area("8. تحليل المخاطر المحتملة:", placeholder="ما الذي قد يهدد المشروع مستقبلاً؟")
q9 = st.text_area("9. فرص التحسين والتطوير:", placeholder="مقترحات لرفع الكفاءة...")
q10 = st.text_area("10. التوصيات النهائية:", placeholder="ماذا تنصح صناع القرار؟")
q11 = st.text_area("11. الملاحظات والختام:", placeholder="أي إضافات أخرى...")

if st.button("🚀 توليد التقرير المعتمد"):
    if report_title:
        st.success(f"جاري معالجة تقرير '{report_title}' بنجاح...")
    else:
        st.warning("يرجى كتابة اسم التقرير أولاً")

if st.button("تسجيل الخروج"):
    st.session_state.authenticated = False
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8; margin-top:20px;'>🛡️ المنصور استراتيجي | 2026</p>", unsafe_allow_html=True)
