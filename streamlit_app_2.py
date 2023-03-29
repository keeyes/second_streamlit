import streamlit as st
import snowflake.connector as sc

st.title("Zena's Amazing Athleisure Catalog")
st.text('Pick a sweatsuit colour or style')

my_cnx = sc.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

my_data_row = my_cur.fetchall()

st.text("Hello from Snowflake:")
st.text(my_data_row)
