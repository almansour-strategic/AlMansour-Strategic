import streamlit as st
from datetime import datetime

# ================== 1. التنسيق البصري المؤسسي الرصين ==================
st.set_page_config(page_title="المنصور AI - الاستشاري الدولي", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
    div[data-testid="stToolbar"], #MainMenu, footer, header, .stDeployButton { display: none !important; }
    .stApp { background-color: #f4f7f9; color: #1e293b; direction: rtl; }
    .main-box {
        background: #ffffff; border-top: 8px solid #1e3a8a; padding: 35px;
        border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.08); margin-top: 5px;
    }
    * { font-family: 'Cairo', sans-serif !important; text-align: right; }
    .brand-title { color: #1e3a8a !important; font-weight: 900 !important; font-size: 2.2rem !important; text-align: center; }
    .section-title { 
        color: #1e3a8a; font-size: 1.1rem; font-weight: 700; margin-top: 30px; margin-bottom: 15px; 
        border-right: 5px solid #fbbf24; padding-right: 12px; background: #f8fafc; padding: 10px; border-radius: 0 8px 8px 0;
    }
    .hint-text { color: #64748b; font-size: 0.8rem; margin-bottom: 12px; border-right: 2px solid #cbd5e1; padding-right: 8px; line-height: 1.5; }
    .magic-desc { color: #2563eb; font-size: 0.75rem; font-weight: 600; text-align: center; margin-bottom: 5px; line-height: 1.3; }
    
    .btn-gen button { background: linear-gradient(90deg, #1e3a8a, #d4af37) !important; color: white !important; font-weight: 700 !important; height: 55px !important; border-radius: 10px !important; width: 100% !important; border:none !important; }
    .btn-exit button { background: #f1f5f9 !important; color: #64748b !important; border: 1px solid #e2e8f0 !important; height: 55px !important; border-radius: 10px !important; width: 100% !important; }
    
    .export-btn button { background: #ffffff !important; color: #1e3a8a !important; border: 1px solid #1e3a8a !important; font-size: 0.9rem !important; height: 45px !important; width: 100% !important; }
    </style>
""", unsafe_allow_html=True)

# ================== 2. مصفوفة التقارير العالمية ==================
GLOBAL_CONFIG = {
    "📑 تقرير الإنجاز الدوري | Progress Report": {
        "fields": ["ملخص التنفيذ ومستوى الإنجاز العام", "تحليل الانحرافات عن الخطة الزمنية", "إدارة التحديات والمخاطر الميدانية", "آليات التجاوز والخطوات التصحيحية المتبعة"],
        "hints": ["أبرز ما تم تحقيقه مقابل الخطة...", "الأسباب الكامنة وراء أي تأخير مرصود...", "المخاطر التي هددت سير العمل...", "الإجراءات العاجلة المنفذة..."]
    },
    "🎓 تقرير ختامي لتدريب | Capacity Building": {
        "fields": ["تحليل نتائج المشاركين (القبلي والبعدي)", "تقييم كفاءة المادة العلمية والمنهجية", "تفاعل المشاركين والبيئة التدريبية", "توصيات استدامة الأثر وتطبيق المهارات"],
        "hints": ["قياس الفارق المعرفي وتطور مستوى المتدربين...", "مدى ملاءمة المحتوى للاحتياجات الفعلي...", "تحديات القاعة والتجهيزات...", "كيفية ضمان نقل الأثر لمكان العمل..."]
    },
    "💰 تقرير الأداء المالي | Financial Report": {
        "fields": ["تحليل المصروفات الفعلية مقابل الميزانية", "تحليل انحرافات التكلفة (Variance)", "الامتثال المالي ومعايير التدقيق", "توصيات كفاءة الإنفاق للفترة القادمة"],
        "hints": ["مقارنة رقمية بين المخطط والمنفق...", "تبرير منطقي لأي تجاوز أو وفورات...", "مطابقة العمليات مع اللوائح الدولية...", "سياسات ترشيد الإنفاق القادم..."]
    }
}

# ================== 3. نظام الدخول ==================
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="brand-title">بوابة المنصور AI</h1>', unsafe_allow_html=True)
    e = st.text_input("البريد الإلكتروني")
    p = st.text_input("كلمة المرور", type="password")
    if st.button("دخول آمن"):
        if e and p: st.session_state.auth = True; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ================== 4. الواجهة المرنة V16 ==================
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI للتقارير الاحترافية</h1>', unsafe_allow_html=True)

rtype = st.selectbox("🎯 حدد التخصص لضبط المنهجية تلقائياً:", list(GLOBAL_CONFIG.keys()))
cfg = GLOBAL_CONFIG[rtype]

st.markdown('<p class="section-title">📌 البيانات التعريفية (أكمل ما يتوافق مع تقريرك)</p>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
p_name = c1.text_input("اسم المشروع / البرنامج *", placeholder="Project Name (مطلوب)")
donor = c1.text_input("الجهة المانحة", placeholder="Donor Agency")
agency = c2.text_input("الجهة المنفذة", placeholder="Implementing Agency")
loc = c2.text_input("مكان التنفيذ", placeholder="Location")

st.markdown('<p class="section-title">📝 المحاور الاستراتيجية (عبئ الخانات المتوفرة لديك)</p>', unsafe_allow_html=True)

for i in range(4):
    label = cfg["fields"][i]
    hint = cfg["hints"][i]
    key = f"q{i+1}_{rtype}"
    
    st.markdown(f"<label>{label}</label>", unsafe_allow_html=True)
    st.markdown(f"<p class='hint-text'>🔍 مثال احترافي: {hint}</p>", unsafe_allow_html=True)
    
    col_t, col_b = st.columns([5, 1.5])
    with col_t:
        txt = st.text_area("", key=key, height=110, label_visibility="collapsed")
    with col_b:
        st.markdown('<p class="magic-desc">اضغط على زر تحسين لتحويل نصك لصياغة احترافية</p>', unsafe_allow_html=True)
        if st.button("✨ تحسين", key=f"btn_{key}"):
            if txt: st.info(f"المقترح: {txt} (تمت المراجعة)")
            else: st.warning("اكتب نصاً أولاً")

st.markdown("<br>", unsafe_allow_html=True)
cg, ce = st.columns(2)

with cg:
    st.markdown('<div class="btn-gen">', unsafe_allow_html=True)
    # التوليد الآن مرن: يحتاج فقط لاسم المشروع
    generate_trigger = st.button("🚀 توليد خيارات التصدير")
    st.markdown('</div>', unsafe_allow_html=True)

with ce:
    st.markdown('<div class="btn-exit">', unsafe_allow_html=True)
    if st.button("🚪 تسجيل الخروج"):
        st.session_state.auth = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# تظهر خيارات التصدير بمجرد وجود اسم المشروع والضغط على الزر
if generate_trigger:
    if p_name:
        st.markdown("---")
        st.markdown('<p style="text-align:center; font-weight:bold; color:#1e3a8a;">📥 جاهز للتصدير! اختر الصيغة المناسبة:</p>', unsafe_allow_html=True)
        e1, e2, e3 = st.columns(3)
        with e1:
            st.markdown('<div class="export-btn">', unsafe_allow_html=True)
            st.button("📄 PDF رسمي")
            st.markdown('</div>', unsafe_allow_html=True)
        with e2:
            st.markdown('<div class="export-btn">', unsafe_allow_html=True)
            st.button("📝 Word (محرر)")
            st.markdown('</div>', unsafe_allow_html=True)
        with e3:
            st.markdown('<div class="export-btn">', unsafe_allow_html=True)
            st.button("📋 نص Text")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("⚠️ فضلاً أدخل 'اسم المشروع' على الأقل لتتمكن من التصدير.")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<center style='color:#94a3b8; font-size:0.75rem; margin-top:15px;'>🛡️ شبكة المنصور الدولية للاستشارات | 2026</center>", unsafe_allow_html=True)
