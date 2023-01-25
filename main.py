import streamlit as st
import pandas as pd
import numpy as np
import datetime
from pathlib import Path


st.set_page_config(page_title="Mini Payroll System", layout="wide")
with st.sidebar:
#    st.sidebar.title(":abacus: Mini Payroll System")

    attendance_data = st.sidebar.file_uploader("Upload Data Absensi", type=["xlsx", "xls"])

    start_date = st.date_input(
        "Start Date",
        datetime.date.today())
    end_date = st.date_input(
        "End Date",
        datetime.date.today())
    st.markdown("""---""") 
    employee_master = st.sidebar.file_uploader("Upload Master Data Pegawai", type=["xlsx", "xls"])
    holidays_date = st.sidebar.file_uploader("Upload Data Libur & Cuti Bersama", type=["xlsx", "xls"])   
    denda_scan_masuk = st.number_input('Denda Tidak Scan Masuk',value=25000)
    denda_scan_pulang = st.number_input('Denda Tidak Scan Pulang',value=25000)
    uang_makan = st.number_input('Uang Makan Harian',value=15000)


font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 24px;
  font-weight: bold;
  margin-top: 0%;
}
</style>
"""

st.write(font_css, unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Raw Data ", "Hitung Gaji Harian", "Generate Report Jam Kerja"])

with tab1:   

   st.write("#### Data Absensi")
   if attendance_data is not None:
        attendance_data_df = pd.read_excel(attendance_data)
        st.write(attendance_data_df)
   else:st.warning('Data Absensi belum di-upload', icon="⚠️")

   emp_master_last_updated = Path('webapp/raw_temp_data/emp_master_last_updated.txt').read_text()
   st.write("#### Data Master Pegawai")
   st.write("last update:",emp_master_last_updated)
   if employee_master is not None:
        employee_master_df = pd.read_excel(employee_master)
        employee_master_df.to_csv("webapp/raw_temp_data/temp_employee_master.csv",index=None)
        f = open('webapp/raw_temp_data/emp_master_last_updated.txt','w')
        f.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
        f.close()
        st.write(employee_master_df)
   else:
        my_file = Path("webapp/raw_temp_data/temp_employee_master.csv")
        if my_file.is_file():
            st.write(pd.read_csv(my_file))
        else:st.warning('Data Master Pegawai belum di-upload', icon="⚠️")

   holidays_date_last_updated = Path('webapp/raw_temp_data/holidays_date_last_updated.txt').read_text()
   st.write("#### Data Libur & Cuti Bersama")
   st.write("last update:",holidays_date_last_updated)
   if holidays_date is not None:
        holidays_date_df = pd.read_excel(holidays_date)
        holidays_date_df.to_csv("webapp/raw_temp_data/temp_holidays_date.csv",index=None)
        f = open('webapp/raw_temp_data/holidays_date_last_updated.txt','w')
        f.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
        f.close()
        st.write(holidays_date_df)
   else:
        my_file = Path("webapp/raw_temp_data/temp_holidays_date.csv")
        if my_file.is_file():
            st.write(pd.read_csv(my_file))
        else:st.warning('Data Libur & Cuti Bersama belum di-upload', icon="⚠️")


with tab2:
   st.header("Calculate Daily-worker Salary")
   st.write(denda_scan_masuk)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

