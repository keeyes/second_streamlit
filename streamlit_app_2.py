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
option = st.selectbox('Pick a sweatsuit color or style:', df.iloc[:,0])

#Build image caption
product_caption = 'Our most amazing, ' +option + ' outfit!'

#Use the option selected to go back and get all the info from the database
my_cur.execute(("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where \
               color_or_style = '" + option + "';")
df2 = my_cur.fetchone()

st.image(df2[0], width = 400, caption = product_caption)

#write df to page to see product details
st.write('Price: ', df2[1])
st.write('Sizes Available: ',df2[2])
st.write(df2[3])



