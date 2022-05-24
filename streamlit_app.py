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
streamlit.dataframe(my_fruit_list);
