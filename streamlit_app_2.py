import streamlit as st
import snowflake.connector as sc
import pandas as pd

st.title("Zena's Amazing Athleisure Catalog")
st.text('Pick a sweatsuit colour or style')

#connect to snowflake
my_cnx = sc.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

#run a snowflake query and put it all into a var called my_catalog
my_cur.execute("SELECT color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

#put the data into a df
df = pd.DataFrame(my_catalog)

#put a pick list for people to choose on streamlit
option = st.selectbox('Pick a sweatsuit color or style:', df.loc[:,1])

#write df to page to see what I am working with
st.write(df)


