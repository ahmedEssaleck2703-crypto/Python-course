import streamlit as st
import pandas as pd

# 1. عنوان التطبيق
st.title("🚀 Advanced Analytics & ML Studio")

# 2. أداة رفع الملفات (CSV أو Excel)
uploaded_file = st.file_uploader("Upload CSV/Excel to start", type=["csv", "xlsx"])

if uploaded_file is not None:
    # قراءة البيانات
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
    
    # عرض جزء من البيانات
    st.subheader("معاينة البيانات")
    st.write(df.head())
    
    # 3. مثال لمعالجة البيانات (تنظيف البيانات)
    if st.button("بدء المعالجة الذكية"):
        # حذف القيم المفقودة كمثال
        df_cleaned = df.dropna()
        st.success("تم تنظيف البيانات بنجاح!")
        st.write(df_cleaned)
        
        # 4. إضافة تحليل بسيط أو رسم بياني
        st.subheader("تحليل سريع")
        st.bar_chart(df_cleaned.iloc[:, 0:2]) # رسم أول عمودين