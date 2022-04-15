#Import Librarys
import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

#Create a Fruit List Dataframe
fruits_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_list = fruits_list.set_index("Fruit")

#Title app
streamlit.title('My First Streamlit App')

#Header 
streamlit.header('Breakfast Favorites')

#Menu app
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#We'll add a user interactive widget called a Multi-select that will allow users to pick the fruits they want in their smoothies.
fruit_selected = streamlit.multiselect("Pick some fruit:", list(fruits_list.index),['Avocado', 'Strawberries'])
fruit_to_show = fruits_list.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)

#Add function for repeatable code block
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_response_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_response_normalized

#New section to display API response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choise = streamlit.text_input('What Fruit would you like information about?')
  #streamlit.write('The user entered', fruit_choise)
  if not fruit_choise:
    streamlit.error('Please select a fruit to get information')
  else:
    back_from_function = get_fruityvice_data(fruit_choise)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()
      
#Snowflake content
streamlit.header('The fruit load list contains:')
#Snowflake-Related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
    return my_cur.fetchall()
  
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
 
def insert_rows_into_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('from streamlit prueba 13:30')")
    return "Thanks for adding" + new_fruit
  
fruit_add = streamlit.text_input('What Fruit would you like add?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  #back_from_function = insert_rows_into_snowflake(fruit_add)
  #my_cnx.close()
  #streamlit.text(back_from_function)

streamlit.stop()


