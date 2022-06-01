import streamlit
import pandas
import requests
import snowflake.connector
from  urllib.error import U

Spaces

2

No wrap
1
import streamlit
2
import pandas
3
import requests
4
import snowflake.connector
5
from  urllib.error import URLError
6
​
7
streamlit.title('My parents new healthy dinner');
8
​
9
streamlit.header('Breakfast Menu');
10
streamlit.text('🥣 Omega 3 & blueberry oatmeal');
11
streamlit.text(' 🥗 Kale, spinach & rocket smothie');
12
streamlit.text('🐔 Hard-boiled Free-range egg');
13
streamlit.text('🥑🍞 Avacado toast');
14
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');
15
​
16
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
17
my_fruit_list=my_fruit_list.set_index('Fruit')
18
#streamlit.multiselect("Pick some fruit:" , list(my_fruit_list.index),['Avocado','Strawberries'])
19
fruits_selected=streamlit.multiselect("Pick some fruit:" , list(my_fruit_list.index),['Avocado','Strawberries'])
20
fruits_to_show=my_fruit_list.loc[fruits_selected]
21
streamlit.dataframe(fruits_to_show);
22
​
23
#create a repeatable code block(called function)
24
def get_fruityvice_data(this_fruit_choice):
25
  fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
26
  fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
27
  return fruityvice_normalized
28
​
29
streamlit.header('fruityvice Fruit Advice');
RLError

streamlit.title('My parents new healthy dinner');

streamlit.header('Breakfast Menu');
streamlit.text('🥣 Omega 3 & blueberry oatmeal');
streamlit.text(' 🥗 Kale, spinach & rocket smothie');
streamlit.text('🐔 Hard-boiled Free-range egg');
streamlit.text('🥑🍞 Avacado toast');
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list=my_fruit_list.set_index('Fruit')
#streamlit.multiselect("Pick some fruit:" , list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_selected=streamlit.multiselect("Pick some fruit:" , list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show);

#create a repeatable code block(called function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
  fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header('fruityvice Fruit Advice');
try:
  fruit_choice=streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else: 
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
  
  streamlit.write('The user entered',fruit_choice )



#streamlit.text(fruityvice_response.json());



#streamlit.stop()






streamlit.header("View our Fruit List - Add Your Favorites")
#snowflake related function
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

#add button to load fruit
if streamlit.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

  
 #allow end user to add fruit to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "Thanks for adding " + new_fruit

    
add_my_fruit=streamlit.text_input('what fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    my_cnx.close()
    streamlit.text(back_from_function)
streamlit.write('Thanks for adding',fruit_choice )

