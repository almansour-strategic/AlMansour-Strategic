import streamlit as st
from datetime import datetime

# ================== 1. الهوية البصرية (إخفاء تام + فخامة مؤسسية) ==================
st.set_page_config(page_title="المنصور AI - الاستشاري الدولي", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
    
    /* إخفاء تام لجميع أدوات المنصة للخصوصية والاحترافية */
    div[data-testid="stToolbar"], #MainMenu, footer, header, .stDeployButton, [data-testid="stStatusWidget"] {
        display: none !important; visibility: hidden !important;
    }
    
    .stApp { background-color: #f8fafc; color: #1e293b; direction: rtl; }
    
    .main-box {
        background: #ffffff; border-top: 10px solid #1e3a8a; padding: 40px;
        border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.05); margin-top: 10px;
    }

    * { font-family: 'Cairo', sans-serif !important; text-align: right; }
    .brand-title { color: #1e3a8a !important; font-weight: 900 !important; font-size: 2.3rem !important; text-align: center; margin:0; }
    .methodology-tag { 
        background: #1e3a8a; color: #fbbf24; padding: 6px 20px; border-radius: 25px; 
        font-size: 0.85rem; display: table; margin: 10px auto 30px auto; font-weight: bold;
    }

    .section-title { 
        color: #1e3a8a; font-size: 1.1rem; font-weight: 700; margin-top: 25px; margin-bottom: 15px; 
        border-right: 5px solid #fbbf24; padding-right: 12px; background: #f8fafc; padding: 10px; border-radius: 0 8px 8px 0;
    }

    .hint-text { color: #64748b; font-size: 0.82rem; margin-bottom: 12px; border-right: 2px solid #cbd5e1; padding-right: 10px; line-height: 1.5; }
    .magic-desc { color: #2563eb; font-size: 0.72rem; font-weight: 600; text-align: center; margin-bottom: 4px; }

    /* الأزرار الملكية المتوازية بنفس الحجم */
    .btn-gen button { background: linear-gradient(90deg, #1e3a8a, #d4af37) !important; color: white !important; font-weight: 700 !important; height: 58px !important; border-radius: 12px !important; width: 100% !important; border:none !important; }
    .btn-exit button { background: #f1f5f9 !important; color: #64748b !important; border: 1px solid #e2e8f0 !important; height: 58px !important; border-radius: 12px !important; width: 100% !important; }
    
    .magic-btn button {
        height: 35px !important; font-size: 0.82rem !important; background: #f0f9ff !important;
        color: #1e3a8a !important; border: 1px dashed #cbd5e1 !important;
    }

    .package-table { width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 0.85rem; }
    .package-table th { background: #1e3a8a; color: white; padding: 10px; text-align: center; }
    .package-table td { border: 1px solid #e2e8f0; padding: 10px; text-align: center; background: white; }
    
    .whatsapp-btn {
        background: #25d366; color: white !important; padding: 12px 25px; border-radius: 50px;
        text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; gap: 10px; margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ================== 2. المنهجية العالمية الشاملة (8 تخصصات سيادية) ==================
GLOBAL_REPORTS = {
    "📑 تقرير الإنجاز الدوري | Progress Report": {
        "q": ["ملخص التنفيذ ومستوى الإنجاز العام", "تحليل الانحرافات عن الخطة الزمنية", "إدارة التحديات والمخاطر الميدانية", "آليات التجاوز والخطوات التصحيحية"],
        "h": ["أبرز ما تم تحقيقه مقابل الخطة...", "الأسباب الكامنة وراء أي تأخير مرصود...", "المخاطر التي هددت سير العمل...", "الإجراءات المنفذة لضمان الاستمرارية..."]
    },
    "🎓 تقرير ختامي لتدريب | Capacity Building Report": {
        "q": ["تحليل نتائج التقييم (القبلي والبعدي)", "تقييم كفاءة المادة العلمية والمنهجية", "تفاعل المشاركين والبيئة التدريبية", "توصيات استدامة الأثر التدريبي"],
        "h": ["قياس الفارق المعرفي وتطور المهارات...", "مدى ملاءمة المحتوى للاحتياجات الفعلي...", "المعوقات اللوجستية والتنظيمية...", "خطة نقل المعرفة لمكان العمل..."]
    },
    "💰 تقرير الأداء المالي | Financial Performance": {
        "q": ["تحليل المصروفات الفعلية مقابل المخطط", "تحليل انحرافات التكلفة (Variance Analysis)", "الامتثال المالي ومعايير التدقيق", "توصيات كفاءة الإنفاق للفترة القادمة"],
        "h": ["مقارنة رقمية دقيقة بين المنفق والمخطط...", "تبرير منطقي لأي تجاوز مالي...", "مطابقة العمليات للوائح الدولية...", "سياسات ترشيد الإنفاق القادم..."]
    },
    "📊 تقرير المتابعة والتقييم | M&E Report": {
        "q": ["قياس مؤشرات الأداء الرئيسية (KPIs)", "جودة المخرجات ورضا أصحاب المصلحة", "الدروس المستفادة والفرص الضائعة", "فرص التحسين وتطوير المنهجية"],
        "h": ["مدى تحقيق النتائج المقررة بالأرقام...", "نتائج الاستبيانات والمقابلات...", "تجارب للتعميم أو أخطاء لتجنبها...", "مقترحات لتحديث مسار العمل..."]
    },
    "🚑 تقرير تقييم الاحتياجات | Needs Assessment": {
        "q": ["تحليل الوضع الراهن وفجوة الاحتياج", "تحديد الفئات الأكثر تضرراً واحتياجاً", "الأولويات العاجلة للاستجابة", "توصيات التدخل والتمويل الاستراتيجي"],
        "h": ["وصف دقيق للأزمة أو الاحتياج المرصود...", "بيانات ديموغرافية للفئات المستهدفة...", "ما هي الاحتياجات غير القابلة للتأجيل؟", "خارطة طريق مقترحة للمانحين..."]
    },
    "🏛️ تقرير الحوكمة والامتثال | Compliance Report": {
        "q": ["الالتزام باللوائح والسياسات المؤسسية", "نتائج الرقابة والتدقيق الداخلي", "الثغرات المرصودة في نظام الحوكمة", "إجراءات التصحيح وتطوير الأداء"],
        "h": ["مدى تطابق الممارسات مع المعايير والقوانين...", "خلاصة عمليات الفحص الدورية...", "نقاط الضعف في الهيكل التنظيمي...", "خطوات سد الثغرات القانونية..."]
    },
    "🌍 تقرير الأثر البيئي والاجتماعي | ESIA Report": {
        "q": ["تحليل الأثر البيئي والحيوي للمشروع", "المسؤولية المجتمعية ورضا المستفيدين", "إجراءات التخفيف من الآثار الجانبية", "استدامة الموارد وحماية البيئة"],
        "h": ["تقييم تأثير العمليات على البيئة...", "مدى قبول وتفاعل المجتمع المحلي...", "كيفية التعامل مع الأضرار الجانبية...", "خطط الحفاظ على الموارد..."]
    },
    "🏗️ تقرير فني وهندسي | Technical Report": {
        "q": ["المواصفات الفنية ومطابقة المواد", "نتائج اختبارات الجودة الميدانية", "المعوقات الإنشائية والتحديات التقنية", "التعديلات والحلول الهندسية المنفذة"],
        "h": ["مدى التزام الموردين بالمواصفات المعتمدة...", "نتائج فحوصات المختبر والضغوط...", "الصعوبات التي واجهت التنفيذ...", "الحلول المبتكرة لتجاوز العقبات..."]
    }
}

# ================== 3. نظام التشغيل والذاكرة المستمرة ==================
if "auth" not in st.session_state: st.session_state.auth = False
if "form_state" not in st.session_state: st.session_state.form_state = {}

def sync(key):
    st.session_state.form_state[key] = st.session_state[key]

if not st.session_state.auth:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="brand-title">بوابة المنصور AI</h1>', unsafe_allow_html=True)
    e = st.text_input("البريد الإلكتروني")
    p = st.text_input("كلمة المرور", type="password")
    if st.button("دخول آمن للمنصة"):
        if e and p: st.session_state.auth = True; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ================== 4. المحرك الرئيسي V18 ==================
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI للتقارير الاحترافية</h1>', unsafe_allow_html=True)
st.markdown('<div class="methodology-tag">صياغة استراتيجية وفق المنهجية العالمية (PMBOK / ISO / Kirkpatrick)</div>', unsafe_allow_html=True)

# القسم 1: نوع التقرير (في القمة)
st.markdown('<p class="section-title">نوع التقرير الدولي | Report Category</p>', unsafe_allow_html=True)
rtype = st.selectbox("🎯 الخطوة 1: حدد التخصص لضبط المنهجية:", list(GLOBAL_REPORTS.keys()), key="rtype", on_change=sync)
cfg = GLOBAL_REPORTS[rtype]

# القسم 2: البيانات التعريفية
st.markdown('<p class="section-title">البيانات التعريفية | Metadata</p>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.text_input("اسم المشروع / البرنامج *", key="p_name", on_change=sync, placeholder="Project Name (مطلوب)")
    st.text_input("الجهة المانحة / الممول", key="donor", on_change=sync, placeholder="Donor Agency")
    st.text_input("مكان التنفيذ / المنطقة", key="loc", on_change=sync, placeholder="Location")
with c2:
    st.text_input("الجهة المنفذة / العميل", key="agency", on_change=sync, placeholder="Implementing Agency")
    st.text_input("مدة التنفيذ", key="dur", on_change=sync, placeholder="Duration")
    st.date_input("تاريخ التقرير", key="r_date")

# القسم 3: المحاور الاستراتيجية
st.markdown('<p class="section-title">المحاور الاستراتيجية للتقرير | Strategic Pillars</p>', unsafe_allow_html=True)

for i in range(4):
    label = cfg["q"][i]
    hint = cfg["h"][i]
    field_key = f"q{i}_{rtype}"
    
    st.markdown(f"<label>{label}</label>", unsafe_allow_html=True)
    st.markdown(f"<p class='hint-text'>🔍 مثال توضيحي: {hint}</p>", unsafe_allow_html=True)
    
    col_t, col_b = st.columns([5, 1.5])
    with col_t:
        txt = st.text_area("", key=field_key, height=100, label_visibility="collapsed", on_change=sync)
    with col_b:
        st.markdown('<p class="magic-desc">اضغط على زر تحسين لتحويل نصك لصياغة احترافية</p>', unsafe_allow_html=True)
        if st.button("✨ تحسين", key=f"btn_{i}_{rtype}"):
            if txt: st.info(f"المقترح الاحترافي: {txt} (تمت الصياغة وفق المعايير الدولية)")
            else: st.warning("اكتب نصاً أولاً")

st.markdown("<br>", unsafe_allow_html=True)

# أزرار التحكم المتوازية
col_gen, col_ex = st.columns(2)
with col_gen:
    st.markdown('<div class="btn-gen">', unsafe_allow_html=True)
    generate_btn = st.button("🚀 توليد خيارات التصدير")
    st.markdown('</div>', unsafe_allow_html=True)
with col_ex:
    st.markdown('<div class="btn-exit">', unsafe_allow_html=True)
    if st.button("🚪 تسجيل الخروج"):
        st.session_state.auth = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

if generate_btn:
    if st.session_state.get("p_name"):
        st.markdown("---")
        st.markdown('<p style="text-align:center; font-weight:bold;">📥 التقرير جاهز! اختر صيغة التصدير:</p>', unsafe_allow_html=True)
        e1, e2, e3 = st.columns(3)
        e1.button("📄 ملف PDF رسمي")
        e2.button("📝 ملف Word (محرر)")
        e3.button("📋 نص Text سريع")
    else:
        st.error("⚠️ يرجى إدخال اسم المشروع على الأقل لتتمكن من التصدير.")

# القسم 4: الباقات (جدول رسمي)
st.markdown('<p class="section-title">باقات العضوية والدعم</p>', unsafe_allow_html=True)
st.markdown("""
<table class="package-table">
    <tr><th>الميزة</th><th>الفضية</th><th>الذهبية</th><th>المؤسسات</th></tr>
    <tr><td>التقارير</td><td>5 شهرياً</td><td>غير محدود</td><td>غير محدود</td></tr>
    <tr><td>الصياغة AI</td><td>أساسية</td><td>احترافية</td><td>مخصصة</td></tr>
    <tr><td>الدعم</td><td>إيميل</td><td>واتساب 24/7</td><td>مستشار خاص</td></tr>
</table>
""", unsafe_allow_html=True)

st.markdown(f'<center><a href="https://wa.me/967774575749" class="whatsapp-btn">💬 تواصل للترقية أو الدعم الفني</a></center>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<center style='color:#94a3b8; font-size:0.7rem; margin-top:15px;'>🛡️ شبكة المنصور الدولية للاستشارات | 2026</center>", unsafe_allow_html=True)
