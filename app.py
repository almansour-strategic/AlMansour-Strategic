import streamlit as st
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from io import BytesIO
from datetime import datetime

# ================== 1. الهوية البصرية الملكية (Al-Mansour Luxury) ==================
st.set_page_config(page_title="المنصور AI - الحقيبة الاستشارية", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
* { font-family: 'Cairo', sans-serif !important; direction: rtl; text-align: right; }
.stApp { background: #f4f7f9; }
.main-card { background: white; padding: 40px; border-radius: 25px; border-top: 12px solid #1e3a8a; box-shadow: 0 15px 50px rgba(0,0,0,0.1); }
.brand-title { color: #1e3a8a; font-weight: 900; text-align: center; font-size: 2.8rem; margin-bottom: 0; }
.brand-sub { text-align: center; color: #d4af37; font-weight: 700; margin-bottom: 30px; letter-spacing: 2px; }
.stTextArea textarea { border-radius: 10px; border: 1px solid #e2e8f0; }
.section-head { background: #f1f5f9; padding: 12px; border-radius: 8px; border-right: 6px solid #fbbf24; color: #1e3a8a; font-weight: 700; margin: 20px 0; }
</style>
""", unsafe_allow_html=True)

# ================== 2. مصفوفة التقارير (15 نوعاً تشمل التدريب والفعاليات) ==================
REPORT_MASTER_DB = {
    # --- قسم التدريب والتعليم ---
    "🎓 ختامي لبرنامج تدريبي": ["أهداف البرنامج ومخرجاته", "تحليل التقييم القبلي والبعدي (Impact)", "مستوى تفاعل وانضباط المشاركين", "توصيات استدامة المهارات"],
    "🏫 تقرير ورشة عمل (Workshop)": ["ملخص الأنشطة والتمارين", "الأدوات والمنهجية المستخدمة", "المخرجات المباشرة للورشة", "الدروس المستفادة"],
    "🎤 تقرير مؤتمر / ندوة": ["أوراق العمل والمداخلات الرئيسية", "أبرز التوصيات الصادرة", "إحصائيات الحضور والمشاركة", "الخلاصة والبيان الختامي"],
    "📝 محضر اجتماع رسمي": ["أجندة الاجتماع والبنود", "القرارات المتخذة والمعتمدة", "المهام المكلف بها (Action Plan)", "موعد الاجتماع القادم"],
    
    # --- قسم الإدارة والتنمية ---
    "📊 المتابعة والتقييم (MEAL)": ["تحقيق المؤشرات (KPIs)", "آليات المساءلة وتظلمات المستفيدين", "التعلم المؤسسي والتحسين", "القيمة مقابل المال (VfM)"],
    "🌍 الاستدامة والأثر (ESG)": ["الأثر البيئي والعمليات الخضراء", "المسؤولية المجتمعية والإدماج", "الحوكمة والشفافية المؤسسية", "خطة الاستدامة طويلة الأمد"],
    "🚨 الاستجابة الطارئة (SITREP)": ["تطورات الوضع الميداني", "الاحتياجات العاجلة والفجوات", "العوائق الأمنية واللوجستية", "خطة التدخل السريع"],
    "🏗️ الجودة الفنية (TQA)": ["المطابقة للمواصفات الهندسية", "اختبارات الجودة والمواد", "إدارة الجدول الزمني والإنحرافات", "التوصيات التقنية النهائية"],
    "💰 الأداء المالي والتدقيق": ["تحليل الإنفاق مقابل الميزانية", "إدارة التدفقات النقدية", "مخاطر الامتثال المالي", "كفاءة الموارد والمدخرات"],
    "🚚 سلاسل التوريد واللوجستيات": ["كفاءة المشتريات والتوريد", "إدارة المخزون والتوزيع", "تحديات الموردين والأسعار", "إدارة الأصول اللوجستية"],
    "🏛️ الحوكمة والامتثال": ["الالتزام بالسياسات الداخلية", "نتائج الرقابة والتدقيق الداخلي", "إدارة النزاهة والشفافية", "إجراءات تصحيح المسار"],
    "🚑 تقييم الاحتياجات (Needs)": ["تحليل الفئات المستهدفة", "ترتيب الأولويات العاجلة", "تحليل الفجوة في الخدمات", "توصيات التمويل والتدخل"],
    "📅 التقرير الدوري (Progress)": ["ملخص الإنجاز الحالي", "الأنشطة القادمة", "التحديات والحلول", "الموارد"],
    "🏁 التقرير الختامي (Final)": ["تحقيق الأهداف النهائية", "قصص النجاح والأثر", "التحديات المتجاوزة", "خطة التسليم"],
    "⚙️ تقرير مخصص (وضع حر)": []
}

# ================== 3. محرك التصدير السيادي ==================
def generate_docx(meta, content, risks, custom_axes=[]):
    doc = Document()
    # العنوان
    h = doc.add_heading(f"تقرير استراتيجي: {meta['type']}", 0)
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # جدول البيانات
    table = doc.add_table(rows=4, cols=2)
    table.style = 'Table Grid'
    meta_info = [("الموضوع/المشروع", meta['p_name']), ("الجهة المسؤولة", meta['donor']), ("المكان/النطاق", meta['loc']), ("تاريخ الإصدار", datetime.now().strftime("%Y/%m/%d"))]
    for i, (k, v) in enumerate(meta_info):
        table.cell(i, 0).text = k
        table.cell(i, 1).text = v

    # الأقسام
    for title, text in content.items():
        doc.add_heading(title, level=1)
        doc.add_paragraph(text if text else "لا يوجد بيانات")

    # الأقسام المخصصة (للمدربين والطلبات الخاصة)
    if custom_axes:
        doc.add_heading("محاور إضافية وتخصصية", level=1)
        for c_title, c_text in custom_axes:
            doc.add_heading(c_title, level=2)
            doc.add_paragraph(c_text)

    # جدول المخاطر
    doc.add_page_break()
    doc.add_heading("مصفوفة المخاطر والامتثال", level=1)
    rt = doc.add_table(rows=1, cols=3)
    rt.style = 'Table Grid'
    for i, h_text in enumerate(["الخطر المرصود", "مستوى التأثير", "خطة التخفيف المعالجة"]):
        rt.rows[0].cells[i].text = h_text
    for r in risks:
        row = rt.add_row().cells
        row[0].text, row[1].text, row[2].text = r

    bio = BytesIO()
    doc.save(bio)
    bio.seek(0)
    return bio

# ================== 4. الواجهة التفاعلية ==================
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="brand-sub">إصدار الحقيبة الاستشارية والتدريبية</p>', unsafe_allow_html=True)

# المدخلات الأساسية
with st.container():
    c1, c2 = st.columns(2)
    with c1: 
        report_type = st.selectbox("🎯 اختر تخصص التقرير:", list(REPORT_MASTER_DB.keys()))
        project = st.text_input("📦 العنوان / اسم البرنامج:")
    with c2:
        entity = st.text_input("🏢 الجهة المستفيدة / المانحة:")
        location = st.text_input("📍 مكان التنفيذ:")

# توليد الأسئلة بناءً على النوع
st.markdown('<p class="section-head">١. المحاور التخصصية (تحليل استراتيجي)</p>', unsafe_allow_html=True)
main_data = {}
fields = REPORT_MASTER_DB[report_type]
if fields:
    for f in fields:
        main_data[f] = st.text_area(f"المحور: {f}", placeholder=f"يرجى تقديم تحليل وافٍ حول {f}...")
else:
    st.warning("أنت في (الوضع الحر). يرجى إضافة المحاور الخاصة بك أدناه.")

# قسم الملحقات والمحاور المخصصة (سد الثغرات)
with st.expander("➕ إضافة محاور تخصصية إضافية (اختياري)"):
    st.write("استخدم هذا القسم لإضافة أي محور لم يرد ذكره أعلاه.")
    n_extra = st.number_input("عدد المحاور الإضافية:", 0, 10, 0)
    extra_data = []
    for i in range(n_extra):
        e_t = st.text_input(f"عنوان المحور {i+1}:", key=f"et_{i}")
        e_d = st.text_area(f"محتوى المحور {i+1}:", key=f"ed_{i}")
        if e_t: extra_data.append((e_t, e_d))

# إدارة المخاطر
st.markdown('<p class="section-head">٢. إدارة المخاطر والدروس المستفادة</p>', unsafe_allow_html=True)
risk_list = []
for r_type in ["مخاطر فنية/تدريبية", "مخاطر إدارية/لوجستية"]:
    col_a, col_b, col_c = st.columns([2, 2, 4])
    with col_a: st.write(f"**{r_type}**")
    with col_b: imp = st.select_slider(f"الأثر", ["منخفض", "متوسط", "عالي"], key=r_name+r_type)
    with col_c: mit = st.text_input("خطة المعالجة:", key=f"mit_{r_type}")
    risk_list.append((r_type, imp, mit))

# التصدير النهائي
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 معالجة وتصدير التقرير السيادي النهائي"):
    if not project:
        st.error("خطأ: يجب إدخال عنوان التقرير أو اسم البرنامج.")
    else:
        meta_data = {"type": report_type, "p_name": project, "donor": entity, "loc": location}
        final_doc = generate_docx(meta_data, main_data, risk_list, extra_data)
        st.download_button("📥 تحميل ملف Word المعتمد", final_doc, file_name=f"AlMansour_{project}.docx")
        st.balloons()
        st.success("تم إعداد التقرير وفق أعلى المعايير الاستشارية.")

st.markdown('</div>', unsafe_allow_html=True)
