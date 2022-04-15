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

#Header 
streamlit.header('Fruityvice Fruit Advice!')
#New section to display API response
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
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)


fruit_add = streamlit.text_input('What Fruit would you like add?', 'orange')
streamlit.write('Thanks for adding', fruit_add)
streamlit.stop()
my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('from streamlit prueba')")

