import streamlit as st
from datetime import datetime

# ================== 1. التنسيق البصري المؤسسي (هوية استشارية) ==================
st.set_page_config(page_title="المنصور AI - المنصة الدولية", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
    
    /* إخفاء الأدوات التقنية للخصوصية */
    div[data-testid="stToolbar"], #MainMenu, footer, header, .stDeployButton { display: none !important; }
    
    .stApp { background-color: #fcfcfc; color: #1e293b; direction: rtl; }
    
    .main-box {
        background: #ffffff;
        border-top: 5px solid #1e3a8a;
        padding: 35px;
        border-radius: 12px;
        box-shadow: 0 4px 30px rgba(0,0,0,0.05);
        margin-top: 5px;
    }

    * { font-family: 'Cairo', sans-serif !important; text-align: right; }
    .brand-title { color: #1e3a8a !important; font-weight: 900 !important; font-size: 2.1rem !important; text-align: center; }
    .methodology-tag { 
        color: #64748b; font-size: 0.8rem; text-align: center; margin-bottom: 20px; border-bottom: 1px solid #f1f5f9; padding-bottom: 10px;
    }

    /* عناوين الأقسام */
    .section-title { color: #1e3a8a; font-size: 1rem; font-weight: 700; margin-top: 25px; margin-bottom: 10px; border-right: 4px solid #1e3a8a; padding-right: 10px; }
    
    /* نص الإرشاد الثابت */
    .hint-text { color: #7f8c8d; font-size: 0.78rem; margin-bottom: 10px; margin-top: -5px; border-right: 2px solid #fbbf24; padding-right: 8px; }

    /* زر التحسين والوصف المكتمل */
    .magic-desc { color: #2563eb; font-size: 0.68rem; font-weight: 600; margin-bottom: 3px; text-align: center; line-height: 1.3; }
    .magic-btn button {
        height: 32px !important; font-size: 0.78rem !important; background: #f8fafc !important;
        color: #1e3a8a !important; border: 1px dashed #cbd5e1 !important;
    }

    /* الحقول */
    label { color: #334155 !important; font-weight: 600 !important; font-size: 0.9rem !important; }
    .stTextArea textarea, .stTextInput input { border: 1px solid #d1d5db !important; border-radius: 6px !important; background: #fafafa !important; font-size: 0.95rem !important; }

    /* الأزرار الرئيسية المتوازية */
    .btn-gen button { background: #1e3a8a !important; color: #ffffff !important; border: none !important; font-weight: 700 !important; height: 50px !important; border-radius: 8px !important; }
    .btn-exit button { background: #ffffff !important; color: #64748b !important; border: 1px solid #cbd5e1 !important; height: 50px !important; border-radius: 8px !important; }
    
    /* زر الواتساب */
    .whatsapp-btn {
        background: #25d366; color: white !important; padding: 10px 20px; border-radius: 50px;
        text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 0.9rem;
    }
    
    /* باقات العضوية */
    .package-card { border: 1px solid #e2e8f0; padding: 12px; border-radius: 10px; text-align: center; background: #f8fafc; font-size: 0.85rem; }
    </style>
""", unsafe_allow_html=True)

# ================== 2. مصفوفة التقارير الدولية باللغتين (المعيار الرسمي) ==================
GLOBAL_REPORTS = {
    "📑 تقرير الإنجاز الدوري | Progress Report": {
        "q1": "الملخص التنفيذي ومستوى التقدم (Milestones):", "h": "تحقيق 80% من المخرجات المخطط لها للفترة الحالية...",
        "q2": "تحليل الفجوات والقيود الميدانية (Gap Analysis):", "h": "تحديد الفجوات الناتجة عن نقص الموارد البشرية المتخصصة...",
        "q3": "إدارة المخاطر والتحديات (Risk Management):", "h": "تقلبات السوق المحلي وأثرها على كفاءة التوريد...",
        "q4": "آليات التجاوز والخطوات التصحيحية:", "h": "تعديل المسار التشغيلي لضمان الالتزام بالجدول الزمني..."
    },
    "🎓 تقرير ختامي للتدريب | Capacity Building Report": {
        "q1": "نتائج التقييم القبلي والبعدي (Pre/Post Test Analysis):", "h": "قياس الفارق المعرفي وتطور مهارات المشاركين بنسبة ملموسة...",
        "q2": "تقييم كفاءة المنهجية والمدرب:", "h": "مدى ملامسة المحتوى للاحتياجات الميدانية الفعلية...",
        "q3": "تحديات البيئة التدريبية واللوجستية:", "h": "المعوقات التقنية أو التنظيمية التي واجهت سير الورشة...",
        "q4": "توصيات استدامة الأثر (Sustainability Plan):", "h": "خطوات عملية لضمان تطبيق المشاركين لما تم تعلمه..."
    },
    "💰 تقرير الأداء المالي | Financial Performance Report": {
        "q1": "تحليل المصروفات مقابل الميزانية (Actual vs Budget):", "h": "مقارنة الإنفاق الفعلي بالخطط المعتمدة وتبرير الوفورات...",
        "q2": "تحليل انحرافات الميزانية (Variance Analysis):", "h": "الأسباب الكامنة وراء تجاوز أو انخفاض الإنفاق في بنود محددة...",
        "q3": "المخاطر المالية والامتثال (Compliance):", "h": "مدى توافق العمليات المالية مع معايير التدقيق واللوائح...",
        "q4": "التوجيهات المالية للفترة القادمة:", "h": "مقترحات إعادة الهيكلة المالية لتحسين كفاءة الإنفاق..."
    },
    "📊 تقرير المتابعة والتقييم | M&E Report": {
        "q1": "قياس مؤشرات الأداء الرئيسية (KPIs):", "h": "مدى مطابقة التنفيذ الفعلي مع مصفوفة النتائج المقررة...",
        "q2": "جودة المخرجات ورضا المستفيدين (Quality Assurance):", "h": "نتائج الاستبيانات والمقابلات الميدانية مع الفئات المستهدفة...",
        "q3": "الدروس المستفادة (Lessons Learned):", "h": "التجارب التي يمكن البناء عليها أو تجنبها في المشاريع المستقبلية...",
        "q4": "التوصيات الاستراتيجية للتطوير:", "h": "مقترحات لتحسين كفاءة التدخلات القادمة بناءً على النتائج..."
    }
}

# ================== 3. بوابة الوصول ==================
if "auth" not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="brand-title">المنصور AI</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#64748b; font-size:0.9rem;">نظام الصياغة الاستراتيجية المعتمد</p>', unsafe_allow_html=True)
    email = st.text_input("البريد الإلكتروني")
    pwd = st.text_input("كلمة المرور", type="password")
    if st.button("دخول"):
        if email and pwd: st.session_state.auth = True; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ================== 4. الواجهة الاحترافية (V11) ==================
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI للتقارير الاحترافية</h1>', unsafe_allow_html=True)
st.markdown('<p class="methodology-tag">صياغة استراتيجية وفق المعايير الدولية | Global Reporting Standards</p>', unsafe_allow_html=True)

# 1. النوع
st.markdown('<p class="section-title">نوع التقرير الدولي | Report Category</p>', unsafe_allow_html=True)
rtype = st.selectbox("اختر التخصص لضبط الأسئلة والسياق ذكياً:", list(GLOBAL_REPORTS.keys()), label_visibility="collapsed")
cfg = GLOBAL_REPORTS[rtype]

# 2. البيانات
st.markdown('<p class="section-title">البيانات التعريفية | Metadata</p>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.text_input("اسم المشروع / البرنامج", placeholder="Project Name")
    st.text_input("الجهة المنفذة", placeholder="Implementing Agency")
    st.text_input("مكان التنفيذ", placeholder="Location / Region")
with c2:
    st.text_input("الجهة المانحة / الممول", placeholder="Donor / Funding Agency")
    st.text_input("مدة التنفيذ", placeholder="Duration")
    st.date_input("تاريخ التقرير")

# 3. المحاور
st.markdown('<p class="section-title">المحاور الاستراتيجية | Strategic Pillars</p>', unsafe_allow_html=True)

def smart_field(label, key, hint):
    st.markdown(f"<label>{label}</label>", unsafe_allow_html=True)
    st.markdown(f"<p class='hint-text'>🔍 مثال احترافي: {hint}</p>", unsafe_allow_html=True)
    c_t, c_b = st.columns([5, 1.5])
    with c_t:
        val = st.text_area("", key=key, label_visibility="collapsed", height=90)
    with c_b:
        st.markdown('<p class="magic-desc">اضغط على زر تحسين لتحويل نصك لصياغة احترافية</p>', unsafe_allow_html=True)
        st.markdown('<div class="magic-btn">', unsafe_allow_html=True)
        if st.button("✨ تحسين", key=f"ai_{key}"): st.toast("جاري التحسين...")
        st.markdown('</div>', unsafe_allow_html=True)
    return val

q1 = smart_field(cfg["q1"], "q1", cfg["h"])
q2 = smart_field(cfg["q2"], "q2", cfg["h"])
q3 = smart_field(cfg["q3"], "q3", cfg["h"])
q4 = smart_field(cfg["q4"], "q4", cfg["h"])

st.markdown("<br>", unsafe_allow_html=True)

# الأزرار
col_gen, col_ex = st.columns(2)
with col_gen:
    st.markdown('<div class="btn-gen">', unsafe_allow_html=True)
    if st.button("🚀 توليد التقرير النهائي"): st.success("تم التوليد بنجاح")
    st.markdown('</div>', unsafe_allow_html=True)
with col_ex:
    st.markdown('<div class="btn-exit">', unsafe_allow_html=True)
    if st.button("🚪 تسجيل الخروج"):
        st.session_state.auth = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 4. الباقات والواتساب
st.markdown("---")
st.markdown('<p class="section-title">باقات الاشتراك | Membership Plans</p>', unsafe_allow_html=True)
b1, b2, b3 = st.columns(3)
with b1: st.markdown('<div class="package-card"><b>الباقة الفضية</b><br>Silver Plan</div>', unsafe_allow_html=True)
with b2: st.markdown('<div class="package-card" style="border-color:#fbbf24;"><b>الباقة الذهبية</b><br>Gold Plan</div>', unsafe_allow_html=True)
with b3: st.markdown('<div class="package-card"><b>باقة المؤسسات</b><br>Enterprise Plan</div>', unsafe_allow_html=True)

st.markdown("<center>", unsafe_allow_html=True)
st.markdown(f'<a href="https://wa.me/967774575749" class="whatsapp-btn">💬 تواصل عبر الواتساب لترقية حسابك</a>', unsafe_allow_html=True)
st.markdown("</center>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<center style='color:#94a3b8; font-size:0.7rem; margin-top:15px;'>🛡️ شبكة المنصور للاستشارات الدولية | 2026</center>", unsafe_allow_html=True)
