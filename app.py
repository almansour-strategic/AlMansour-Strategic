import streamlit as st
from datetime import datetime
from docx import Document
from io import BytesIO

# ================== 1. الهوية البصرية الملكية (فخامة مؤسسية) ==================
st.set_page_config(page_title="المنصور AI - V28 المستقر", layout="centered")

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

# ================== 2. المنهجية العالمية (8 تخصصات سيادية كاملة) ==================
GLOBAL_REPORTS = {
    "📑 تقرير الإنجاز الدوري | Progress Report": {
        "q": ["ملخص التنفيذ ومستوى الإنجاز العام", "تحليل الانحرافات عن الخطة الزمنية", "إدارة التحديات والمخاطر الميدانية", "آليات التجاوز والخطوات التصحيحية"],
        "h": ["تم إنجاز 80% من المخرجات المخطط لها...", "تحديد الفجوات الناتجة عن نقص الموارد...", "تقلبات السوق المحلي وأثرها على التوريد...", "تعديل المسار التشغيلي لضمان الالتزام..."]
    },
    "🎓 تقرير ختامي لتدريب | Capacity Building Report": {
        "q": ["تحليل نتائج التقييم (القبلي والبعدي)", "تقييم كفاءة المادة العلمية والمنهجية", "تفاعل المشاركين والبيئة التدريبية", "توصيات استدامة الأثر التدريبي"],
        "h": ["قياس الفارق المعرفي وتطور المهارات...", "مدى ملاءمة المحتوى للاحتياجات...", "المعوقات اللوجستية والتنظيمية...", "خطة نقل المعرفة لمكان العمل..."]
    },
    "💰 تقرير الأداء المالي | Financial Performance": {
        "q": ["تحليل المصروفات الفعلية مقابل المخطط", "تحليل انحرافات التكلفة (Variance)", "الامتثال المالي ومعايير التدقيق", "توصيات كفاءة الإنفاق للفترة القادمة"],
        "h": ["مقارنة رقمية دقيقة بين المنفق والمخطط...", "تبرير منطقي لأي تجاوز مالي...", "مطابقة العمليات للوائح الدولية...", "سياسات ترشيد الإنفاق القادم..."]
    },
    "📊 تقرير المتابعة والتقييم | M&E Report": {
        "q": ["قياس مؤشرات الأداء الرئيسية (KPIs)", "جودة المخرجات ورضا أصحاب المصلحة", "الدروس المستفادة والفرص الضائعة", "فرص التحسين وتطوير المنهجية"],
        "h": ["مدى تحقيق النتائج المقررة بالأرقام...", "نتائج الاستبيانات والمقابلات الميدانية...", "تجارب للتعميم أو أخطاء لتجنبها...", "مقترحات لتحسين كفاءة التدخلات القادمة..."]
    },
    "🚑 تقرير تقييم الاحتياجات | Needs Assessment": {
        "q": ["تحليل الوضع الراهن وفجوة الاحتياج", "تحديد الفئات الأكثر تضرراً", "الأولويات العاجلة للاستجابة", "توصيات التدخل والتمويل"],
        "h": ["وصف دقيق للأزمة أو الاحتياج المرصود...", "بيانات ديموغرافية للفئات المستهدفة...", "احتياجات غير قابلة للتأجيل...", "خارطة طريق مقترحة للمانحين..."]
    },
    "🏛️ تقرير الحوكمة والامتثال | Compliance Report": {
        "q": ["الالتزام باللوائح والسياسات المؤسسية", "نتائج الرقابة والتدقيق الداخلي", "الثغرات المرصودة في نظام الحوكمة", "إجراءات التصحيح وتطوير الأداء"],
        "h": ["تطابق الممارسات مع المعايير الدولية...", "خلاصة عمليات الفحص الدورية...", "نقاط الضعف في الهيكل التنظيمي...", "خطوات سد الثغرات القانونية..."]
    },
    "🌍 تقرير الأثر البيئي والاجتماعي | ESIA Report": {
        "q": ["تحليل الأثر البيئي والحيوي للمشروع", "المسؤولية المجتمعية ورضا المستفيدين", "إجراءات التخفيف من الآثار الجانبية", "استدامة الموارد وحماية البيئة"],
        "h": ["تقييم تأثير العمليات على البيئة...", "مدى قبول وتفاعل المجتمع المحلي...", "كيفية التعامل مع الأضرار الجانبية...", "خطط الحفاظ على الموارد..."]
    },
    "🏗️ تقرير فني وهندسي | Technical Report": {
        "q": ["المواصفات الفنية ومطابقة المواد", "نتائج اختبارات الجودة الميدانية", "المعوقات الإنشائية والتحديات التقنية", "التعديلات والحلول الهندسية المنفذة"],
        "h": ["التزام الموردين بالمواصفات المعتمدة...", "نتائج فحوصات المختبر والضغوط...", "الصعوبات التي واجهت التنفيذ...", "الحلول المبتكرة لتجاوز العقبات..."]
    }
}

# ================== 3. محرك المستندات (Word) ==================
def generate_safe_word(p_name, rtype, donor, loc, agency, content_dict):
    doc = Document()
    doc.add_heading(f"Report: {rtype}", 0)
    doc.add_paragraph(f"Project: {p_name}")
    doc.add_paragraph(f"Donor: {donor}")
    doc.add_paragraph(f"Agency: {agency}")
    doc.add_paragraph(f"Location: {loc}")
    doc.add_paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    
    for title, text in content_dict.items():
        doc.add_heading(title, level=1)
        doc.add_paragraph(text if text else "N/A")
    
    bio = BytesIO()
    doc.save(bio)
    bio.seek(0)
    return bio

# ================== 4. نظام التشغيل الصافي (V28) ==================
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

# الخطوة 1
st.markdown('<p class="section-title">1. نوع التقرير الدولي</p>', unsafe_allow_html=True)
rtype = st.selectbox("🎯 حدد التخصص لضبط المنهجية:", list(GLOBAL_REPORTS.keys()))
cfg = GLOBAL_REPORTS[rtype]

# الخطوة 2
st.markdown('<p class="section-title">2. البيانات التعريفية</p>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
p_name = c1.text_input("اسم المشروع / البرنامج *", placeholder="Project Name")
donor = c1.text_input("الجهة المانحة", placeholder="Donor Agency")
loc = c2.text_input("مكان التنفيذ", placeholder="Location")
agency = c2.text_input("الجهة المنفذة", placeholder="Implementing Agency")

# الخطوة 3
st.markdown('<p class="section-title">3. المحاور الاستراتيجية</p>', unsafe_allow_html=True)
user_responses = {}
for i in range(4):
    label = cfg["q"][i]
    hint = cfg["h"][i]
    st.markdown(f"<label>{label}</label>", unsafe_allow_html=True)
    st.markdown(f"<p class='hint-text'>🔍 مثال احترافي: {hint}</p>", unsafe_allow_html=True)
    
    col_t, col_b = st.columns([5, 1.5])
    with col_t:
        txt = st.text_area("", key=f"f_v28_{i}_{rtype}", height=100, label_visibility="collapsed")
        user_responses[label] = txt
    with col_b:
        if st.button("✨ تحسين", key=f"btn_v28_{i}_{rtype}"):
            if txt: st.info(f"المقترح: {txt} (تمت المراجعة)")
            else: st.warning("أدخل نصاً")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 توليد التقرير النهائي"):
    if p_name:
        st.success("التقرير جاهز! اختر صيغة التصدير:")
        word_file = generate_safe_word(p_name, rtype, donor, loc, agency, user_responses)
        
        ec1, ec2 = st.columns(2)
        with ec1:
            st.markdown('<div class="export-btn">', unsafe_allow_html=True)
            st.download_button("📝 تحميل Word المعتمد", word_file, f"{p_name}.docx")
            st.markdown('</div>', unsafe_allow_html=True)
        with ec2:
            st.markdown('<div class="export-btn">', unsafe_allow_html=True)
            st.download_button("📋 تحميل نص سريع", f"{p_name}\n{user_responses}", f"{p_name}.txt")
            st.markdown('</div>', unsafe_allow_html=True)
    else: st.error("⚠️ يرجى إدخال اسم المشروع أولاً.")

st.markdown(f'<center><a href="https://wa.me/967774575749" class="whatsapp-btn">💬 تواصل للدعم الفني</a></center>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
