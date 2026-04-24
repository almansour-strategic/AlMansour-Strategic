import streamlit as st
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from io import BytesIO
from datetime import datetime

# ================== 1. الهوية البصرية (Sovereign Look & Feel) ==================
st.set_page_config(page_title="المنصور AI - المنهجية العالمية", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');
* { font-family: 'Cairo', sans-serif !important; direction: rtl; text-align: right; }
.stApp { background: #f0f2f5; }
.main-card { background: white; padding: 40px; border-radius: 20px; border-top: 12px solid #1e3a8a; box-shadow: 0 10px 30px rgba(0,0,0,0.08); }
.brand-title { color: #1e3a8a; font-weight: 900; text-align: center; font-size: 2.5rem; margin-bottom: 0; }
.methodology-tag { background: #1e3a8a; color: #fbbf24; padding: 4px 15px; border-radius: 20px; font-size: 0.8rem; display: table; margin: 5px auto 25px auto; }
.section-head { background: #f8fafc; padding: 10px; border-radius: 8px; border-right: 6px solid #fbbf24; color: #1e3a8a; font-weight: 700; margin: 20px 0; }
.hint-box { color: #64748b; font-size: 0.85rem; margin-bottom: 8px; background: #fffbeb; padding: 8px; border-radius: 5px; border: 1px solid #fde68a; }
</style>
""", unsafe_allow_html=True)

# ================== 2. قاعدة البيانات (المنهجية العالمية المستخرجة من الويب) ==================
GLOBAL_DB = {
    "🎓 ختامي لبرنامج تدريبي (Kirkpatrick)": [
        ("قياس رد الفعل والتعلم (Learning)", "أبدى 90% من المشاركين استيعاباً كاملاً للمفاهيم التقنية المتقدمة..."),
        ("تعديل السلوك وتطبيق المهارات", "تم رصد تحسن ملحوظ في سرعة أداء المهام الميدانية بنسبة 30%..."),
        ("الأثر النهائي على المؤسسة (Results)", "ساهم التدريب في تقليل الأخطاء الإجرائية بنسبة 20% خلال شهر..."),
        ("توصيات الاستدامة التدريبية", "ضرورة تفعيل نظام 'التوجيه الميداني' لضمان استمرار انتقال المعرفة...")
    ],
    "📊 المتابعة والتقييم (MEAL - RBM)": [
        ("تحقيق النتائج مقابل المخطط (Outcome)", "تم الوصول إلى 95% من المستهدفات الاستراتيجية المحددة في الإطار المنطقي..."),
        ("كفاءة استخدام الموارد (Efficiency)", "تم تحقيق المخرجات بأقل من الميزانية المرصودة بنسبة 5% نتيجة تحسين المشتريات..."),
        ("رضا المستفيدين والمساءلة", "سجلت منصة الشكاوى نسبة رضا بلغت 4.8/5 مع استجابة فورية لكافة الملاحظات..."),
        ("الدروس المستفادة للتدخلات القادمة", "أثبت إشراك المجتمع المحلي في التخطيط نجاحاً باهراً في سرعة التنفيذ...")
    ],
    "🌍 تقرير الاستدامة (ESG Reporting)": [
        ("الأثر البيئي والمسؤولية المناخية", "تبني حلول الطاقة النظيفة أدى لخفض الانبعاثات بمعدل 10 أطنان سنوياً..."),
        ("المسؤولية المجتمعية والنوع الاجتماعي", "تحقيق توازن جندري بنسبة 40% في المناصب القيادية داخل المشروع..."),
        ("الحوكمة والامتثال الأخلاقي", "الالتزام الكامل بمدونة السلوك العالمية وعدم رصد أي مخالفات إجرائية..."),
        ("الرؤية المستقبلية للاستدامة", "خطة التحول الرقمي الكامل لتقليل استهلاك الورق بنسبة 100%...")
    ]
    # يمكن إضافة بقية الـ 15 نوعاً بنفس المنهجية
}

# ================== 3. المحرك الذكي (The Polisher) ==================
def polish_text(text):
    """وظيفة لمحاكاة تحسين النص بكلمات استشارية"""
    if not text: return "لم يتم تقديم بيانات."
    replacements = {
        "عملنا": "تم تنفيذ وتحقيق",
        "صار": "نتج عن ذلك",
        "المشكلة": "التحدي الاستراتيجي",
        "الحل": "إجراء التخفيف والمعالجة",
        "كويس": "وفق المعايير القياسية المعتمدة"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def generate_sovereign_docx(meta, content, risks, custom_axes=[]):
    doc = Document()
    doc.add_heading(f"التقرير الاستراتيجي: {meta['type']}", 0).alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # الجدول التعريفي
    t = doc.add_table(rows=4, cols=2); t.style = 'Table Grid'
    data = [("المشروع", meta['name']), ("الجهة", meta['entity']), ("الإنجاز", f"{meta['progress']}%"), ("التاريخ", datetime.now().strftime("%Y/%m/%d"))]
    for i, (k, v) in enumerate(data):
        t.cell(i, 0).text = k; t.cell(i, 1).text = str(v)

    # المحتويات
    for title, text in content.items():
        doc.add_heading(title, level=1)
        doc.add_paragraph(polish_text(text)) # تطبيق المحسن الذكي

    if custom_axes:
        doc.add_heading("محاور تخصصية إضافية", level=1)
        for ct, cd in custom_axes:
            doc.add_heading(ct, level=2); doc.add_paragraph(polish_text(cd))

    doc.add_page_break()
    doc.add_heading("مصفوفة المخاطر والامتثال (Global Standard)", level=1)
    rt = doc.add_table(rows=1, cols=3); rt.style = 'Table Grid'
    for i, h in enumerate(["الخطر", "الأثر", "المعالجة"]): rt.rows[0].cells[i].text = h
    for r in risks:
        row = rt.add_row().cells
        row[0].text, row[1].text, row[2].text = r

    bio = BytesIO(); doc.save(bio); bio.seek(0)
    return bio

# ================== 4. الواجهة ==================
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown('<h1 class="brand-title">المنصور AI</h1>', unsafe_allow_html=True)
st.markdown('<div class="methodology-tag">المنهجية العالمية القائمة على النتائج (RBM)</div>', unsafe_allow_html=True)

# المدخلات
c1, c2, c3 = st.columns([2, 2, 1])
with c1: 
    rtype = st.selectbox("🎯 التخصص المنهجي:", list(GLOBAL_DB.keys()))
    p_name = st.text_input("📦 اسم المشروع / البرنامج:")
with c2:
    entity = st.text_input("🏢 الجهة المانحة / الشريك:")
    loc = st.text_input("📍 الموقع:")
with c3:
    progress = st.number_input("📊 الإنجاز %", 0, 100, 50)

# الأسئلة المنهجية
st.markdown('<p class="section-head">١. صياغة المحاور (وفق المعايير الدولية المحدثة)</p>', unsafe_allow_html=True)
user_content = {}
for label, hint in GLOBAL_DB[rtype]:
    st.markdown(f"**{label}**")
    st.markdown(f'<div class="hint-box">💡 مثال صياغة خبير: {hint}</div>', unsafe_allow_html=True)
    user_content[label] = st.text_area("", key=f"in_{label}", height=80, label_visibility="collapsed")

# المحاور المخصصة
with st.expander("➕ إضافة محاور إضافية (لتلبية طلبات خاصة)"):
    num = st.number_input("عدد المحاور:", 0, 5, 0)
    c_axes = []
    for i in range(num):
        ca1, ca2 = st.columns([1, 2])
        with ca1: ct = st.text_input(f"العنوان {i+1}", key=f"ct_{i}")
        with ca2: cd = st.text_area(f"المحتوى {i+1}", key=f"cd_{i}")
        if ct: c_axes.append((ct, cd))

# المخاطر
st.markdown('<p class="section-head">٢. مصفوفة المخاطر والتحقق</p>', unsafe_allow_html=True)
risks = []
for r_tag in ["مخاطر استراتيجية", "مخاطر تشغيلية"]:
    cr1, cr2, cr3 = st.columns([2, 1, 3])
    with cr1: st.write(f"**{r_tag}**")
    with cr2: rlvl = st.selectbox("الأثر", ["منخفض", "متوسط", "عالي"], key=f"lv_{r_tag}")
    with cr3: rmit = st.text_input("خطة المعالجة:", key=f"mit_{r_tag}")
    risks.append((r_tag, rlvl, rmit))

if st.button("🚀 معالجة وتوليد التقرير السيادي"):
    if not p_name: st.error("يرجى تسمية المشروع.")
    else:
        meta = {"type": rtype, "name": p_name, "entity": entity, "progress": progress, "loc": loc}
        file = generate_sovereign_docx(meta, user_content, risks, c_axes)
        st.download_button("📥 تحميل التقرير المعتمد (Word)", file, file_name=f"Strategic_Report_{p_name}.docx")
        st.balloons()

st.markdown('</div>', unsafe_allow_html=True)
