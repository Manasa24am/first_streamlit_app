import streamlit
streamlit.title('My parents new healthy dinner');

streamlit.header('Breakfast Menu');
streamlit.text('🥣 Omega 3 & blueberry oatmeal');
streamlit.text(' 🥗 Kale, spinach & rocket smothie');
streamlit.text('🐔 Hard-boiled Free-range egg');
streamlit.text('🥑🍞 Avacado toast');
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list=my_fruit_list.set_index('Fruit')
#streamlit.multiselect("Pick some fruit:" , list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_selected=streamlit.multiselect("Pick some fruit:" , list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show);

streamlit.header('fruityvice Fruit Advice');
fruit_choice=streamlit.text_input('what fruit would you like information about?', 'kiwi')
streamlit.write('The user entered',fruit_choice )

import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
#streamlit.text(fruityvice_response.json());

fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load contains:")
#streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

fruit_choice=streamlit.text_input('what fruit would you like to add?', 'jackfruit')
streamlit.write('Thanks for adding',fruit_choice )

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
