#Import Librarys
import streamlit
import pandas as pd
import requests
import snowflake.connector

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

#Header 
streamlit.header('Fruityvice Fruit Advice!')
fruit_choise = streamlit.text_input('What Fruit would you like information about?', 'kiwi')
streamlit.write('The user entered', fruit_choise)
#Varible with API response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choise)
fruityvice_response_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_response_normalized )

#Snowflake content
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)

fruit_add = streamlit.text_input('What Fruit would you like add?', 'orange')
streamlit.write('Thanks for adding', fruit_add)

my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('from streamlit')")

