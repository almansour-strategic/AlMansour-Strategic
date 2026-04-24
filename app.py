import streamlit as st
from datetime import datetime

# ================== 1. التنسيق البصري المؤسسي (رصانة وفخامة) ==================
st.set_page_config(page_title="المنصور AI - الاستشاري الدولي", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
    
    div[data-testid="stToolbar"], #MainMenu, footer, header, .stDeployButton { display: none !important; }
    .stApp { background-color: #f4f7f9; color: #1e293b; direction: rtl; }
    
    .main-box {
        background: #ffffff;
        border-top: 8px solid #1e3a8a;
        padding: 35px;
        border-radius: 15px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.08);
        margin-top: 5px;
    }

    * { font-family: 'Cairo', sans-serif !important; text-align: right; }
    .brand-title { color: #1e3a8a !important; font-weight: 900 !important; font-size: 2.2rem !important; text-align: center; margin-bottom: 0px; }
    
    .section-title { 
        color: #1e3a8a; font-size: 1.1rem; font-weight: 700; 
        margin-top: 30px; margin-bottom: 15px; 
        border-right: 5px solid #fbbf24; padding-right: 12px;
        background: #f8fafc; padding: 10px; border-radius: 0 8px 8px 0;
    }
    
    .hint-text { color: #64748b; font-size: 0.8rem; margin-bottom: 12px; border-right: 2px solid #cbd5e1; padding-right: 8px; line-height: 1.5; }
    .magic-desc { color: #2563eb; font-size: 0.75rem; font-weight: 600; text-align: center; margin-bottom: 5px; line-height: 1.3; }
    
    .btn-gen button { background: linear-gradient(90deg, #1e3a8a, #d4af37) !important; color: white !important; font-weight: 700 !important; height: 55px !important; border-radius: 10px !important; width: 100% !important; border:none !important; }
    .btn-exit button { background: #ffffff !important; color: #64748b !important; border: 1px solid #cbd5e1 !important; height: 55px !important; border-radius: 10px !important; width: 100% !important; }
    
    .package-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.85rem; }
    .package-table th { background: #1e3a8a; color: white; padding: 10px; text-align: center; }
    .package-table td { border: 1px solid #e2e8f0; padding: 10px; text-align: center; background: white; }

    .whatsapp-float {
        background: #25d366; color: white !important; padding: 12px 25px; border-radius: 50px;
        text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ================== 2. المصفوفة العالمية للتقارير (هيكلة دقيقة 100%) ==================
GLOBAL_CONFIG = {
    "📑 تقرير الإنجاز الدوري | Progress Report": {
        "fields": ["ملخص التنفيذ ومستوى الإنجاز العام", "تحليل الانحرافات عن الخطة الزمنية", "إدارة التحديات والمخاطر الميدانية", "آليات التجاوز والخطوات التصحيحية المتبعة"],
        "hints": ["نسبة الإنجاز الفعلي مقابل المخطط...", "الأسباب الكامنة وراء أي تأخير مرصود...", "المخاطر التي هددت سير العمل...", "الإجراءات العاجلة التي ضمنا بها استمرار التنفيذ..."]
    },
    "🎓 تقرير ختامي لبرنامج تدريبي | Capacity Building": {
        "fields": ["تحليل نتائج المشاركين (القبلي والبعدي)", "تقييم كفاءة المادة العلمية والمنهجية", "تفاعل المشاركين والبيئة التدريبية", "توصيات استدامة الأثر وتطبيق المهارات"],
        "hints": ["قياس الفارق المعرفي وتطور مستوى المتدربين...", "مدى ملاءمة المحتوى للاحتياجات الفعلية...", "تحديات القاعة، التجهيزات، والمشاركة الفاعلة...", "كيفية ضمان نقل الأثر لمكان العمل..."]
    },
    "🚑 تقرير تقييم احتياجات | Needs Assessment": {
        "fields": ["تحليل الوضع الراهن وفجوة الاحتياج", "تحديد الفئات المتضررة والأكثر احتياجاً", "الأولويات العاجلة لخطط الاستجابة", "توصيات التدخل الاستراتيجي والتمويل"],
        "hints": ["وصف دقيق للأزمة أو الوضع المراد معالجته...", "بيانات ديموغرافية وإحصائية للفئات المستهدفة...", "ما هي الاحتياجات التي لا تقبل التأجيل؟", "خارطة طريق مقترحة للجهات المانحة..."]
    },
    "💰 تقرير الأداء المالي | Financial Report": {
        "fields": ["تحليل المصروفات الفعلية مقابل الميزانية", "تحليل انحرافات التكلفة (Variance)", "الامتثال المالي ومعايير التدقيق", "توصيات كفاءة الإنفاق للفترة القادمة"],
        "hints": ["مقارنة رقمية دقيقة بين المخطط والمنفق...", "تبرير منطقي لأي تجاوز أو وفورات مالية...", "مطابقة العمليات مع اللوائح المالية الدولية...", "سياسات ترشيد الإنفاق وتعظيم الفائدة..."]
    },
    "🛡️ تقرير الحوكمة والامتثال | Compliance": {
        "fields": ["مستوى الالتزام باللوائح والسياسات", "نتائج الرقابة والتدقيق الداخلي", "الثغرات المرصودة في نظام الحوكمة", "إجراءات التصحيح وتطوير الأداء المؤسسي"],
        "hints": ["مدى تطابق الممارسات مع المعايير والقوانين...", "خلاصة عمليات الفحص والرقابة الدورية...", "نقاط الضعف في الهيكل التنظيمي أو الإداري...", "خطوات سد الثغرات القانونية والإدارية..."]
    },
    "🌍 تقرير الأثر البيئي والاجتماعي | ESIA": {
        "fields": ["تحليل الأثر البيئي للمشروع", "المسؤولية المجتمعية ورضا المستفيدين", "إجراءات التخفيف من الآثار السلبية", "استدامة الموارد وحماية البيئة"],
        "hints": ["تقييم تأثير العمليات على المحيط البيئي...", "مدى قبول وتفاعل المجتمع المحلي مع المشروع...", "كيفية التعامل مع الأضرار الجانبية للمشروع...", "خطط الحفاظ على الموارد للأجيال القادمة..."]
    },
    "🏗️ تقرير فني وهندسي | Technical Report": {
        "fields": ["المواصفات الفنية ومطابقة المواد", "نتائج اختبارات الجودة الميدانية", "المعوقات الإنشائية والتحديات التقنية", "التعديلات والحلول الهندسية المنفذة"],
        "hints": ["مدى التزام الموردين بالمواصفات المعتمدة...", "نتائج فحوصات المختبر والضغوط الهندسية...", "الصعوبات التي واجهت التنفيذ في الموقع...", "الحلول المبتكرة لتجاوز العقبات الإنشائية..."]
    },
    "📊 تقرير المتابعة والتقييم | M&E Report": {
        "fields": ["قياس مؤشرات الأداء (KPIs)", "جودة المخرجات ورضا أصحاب المصلحة", "الدروس المستفادة والفرص الضائعة", "فرص التحسين وتطوير المنهجية المستقبلي"],
        "hints": ["مدى تحقيق النتائج المرجوة بالأرقام...", "تقييم الجهة المانحة والمستفيدين للجودة...", "تجارب ناجحة للتعميم أو أخطاء لتجنبها...", "توصيات لتحديث مسار العمل في المشاريع القادمة..."]
    }
}

# ================== 3. نظام الذاكرة المستمرة والدخول ==================
if "auth" not in st.session_state: st.session_state.auth = False
if "form_data" not in st.session_state: st.session_state.form_data = {}

def sync_data(key):
    st.session_state.form_data[key] = st.session_state[key]

if not st.session_state.auth:
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<h1 class="brand-title">بوابة المنصور AI</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#64748b;">نظام الصياغة الاستراتيجية المعتمد 2026</p>', unsafe_allow_html=True)
    e = st.text_input("البريد الإلكتروني")
    p = st.text_input("كلمة المرور", type="password")
    if st.button("دخول آمن"):
        if e and p: st.session_state.auth = True; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ================== 4. المحرك الرئيسي (السيادة V13) ==================
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI للتقارير الاحترافية</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#64748b; font-size:0.85rem;">صياغة استراتيجية وفق المنهجية العالمية | Global Framework 2026</p>', unsafe_allow_html=True)

# القسم 1: التخصص
st.markdown('<p class="section-title">1. نوع التقرير الدولي | Report Category</p>', unsafe_allow_html=True)
rtype = st.selectbox("حدد التخصص لضبط الأسئلة والمنهجية تلقائياً:", list(GLOBAL_CONFIG.keys()), key="rtype", on_change=sync_data)
cfg = GLOBAL_CONFIG[rtype]

# القسم 2: البيانات التعريفية
st.markdown('<p class="section-title">2. البيانات التعريفية | Metadata</p>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.text_input("اسم المشروع / البرنامج", key="p_name", on_change=sync_data, placeholder="Project Name")
    st.text_input("الجهة المانحة / الممول", key="donor", on_change=sync_data, placeholder="Donor Agency")
    st.text_input("مكان التنفيذ", key="loc", on_change=sync_data, placeholder="Location")
with c2:
    st.text_input("الجهة المنفذة", key="agency", on_change=sync_data, placeholder="Implementing Agency")
    st.text_input("مدة التنفيذ", key="dur", on_change=sync_data, placeholder="Duration")
    st.date_input("تاريخ التقرير", key="r_date")

# القسم 3: المحاور السيادية
st.markdown('<p class="section-title">3. المحاور الاستراتيجية للتقرير | Strategic Pillars</p>', unsafe_allow_html=True)

def render_field(label, key, hint):
    st.markdown(f"<label>{label}</label>", unsafe_allow_html=True)
    st.markdown(f"<p class='hint-text'>🔍 مثال احترافي: {hint}</p>", unsafe_allow_html=True)
    
    col_t, col_b = st.columns([5, 1.5])
    with col_t:
        # استرجاع القيمة من الذاكرة إذا وجدت
        default_val = st.session_state.form_data.get(key, "")
        val = st.text_area("", key=key, value=default_val, on_change=sync_data, height=110, label_visibility="collapsed")
    with col_b:
        st.markdown('<p class="magic-desc">اضغط على زر تحسين لتحويل نصك لصياغة احترافية</p>', unsafe_allow_html=True)
        if st.button("✨ تحسين", key=f"btn_{key}"):
            if st.session_state.get(key):
                # محاكاة تحسين النص وفق المنهجية (سيتم ربطها بـ API لاحقاً)
                improved = f"وفق المنهجية العالمية لـ {rtype}: {st.session_state[key]} (تمت الصياغة الاحترافية بنجاح)"
                st.session_state.form_data[key] = improved
                st.toast("تم تحسين الصياغة!")
                st.rerun()
    return val

# توليد الأسئلة الأربعة الأساسية لكل نوع بدقة
for i in range(4):
    render_field(cfg["fields"][i], f"q{i+1}", cfg["hints"][i])

# الأزرار المتوازية
st.markdown("<br>", unsafe_allow_html=True)
cg, ce = st.columns(2)
with cg:
    st.markdown('<div class="btn-gen">', unsafe_allow_html=True)
    if st.button("🚀 توليد التقرير الماسي"): st.success("تم التوليد وفق المنهجية العالمية")
    st.markdown('</div>', unsafe_allow_html=True)
with ce:
    st.markdown('<div class="btn-exit">', unsafe_allow_html=True)
    if st.button("🚪 تسجيل الخروج"):
        st.session_state.auth = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# القسم 4: الباقات
st.markdown('<p class="section-title">4. باقات الاشتراك والدعم الاستشاري</p>', unsafe_allow_html=True)
st.markdown("""
<table class="package-table">
    <tr><th>الميزة</th><th>الفضية</th><th>الذهبية</th><th>المؤسسات</th></tr>
    <tr><td>عدد التقارير</td><td>5 شهرياً</td><td>غير محدود</td><td>غير محدود</td></tr>
    <tr><td>الصياغة الذكية</td><td>أساسية</td><td>متقدمة</td><td>تخصصية</td></tr>
    <tr><td>الدعم الفني</td><td>إيميل</td><td>واتساب 24/7</td><td>مستشار خاص</td></tr>
</table>
""", unsafe_allow_html=True)

st.markdown(f'<center><a href="https://wa.me/967774575749" class="whatsapp-float">💬 تواصل لترقية حسابك أو طلب دعم فني</a></center>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<center style='color:#94a3b8; font-size:0.7rem; margin-top:15px;'>🛡️ شبكة المنصور الدولية للاستشارات | إدارة البيانات 2026</center>", unsafe_allow_html=True)
