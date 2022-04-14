#Import Librarys
import streamlit
import pandas as pd
import requests

#Create a Fruit List Dataframe
fruits_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_list = fruits_list.set_index("Fruit")

#Varible with API response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choise)
fruityvice_response_normalized = pd.json_normalize(fruityvice_response.json())

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
streamlit.dataframe(fruityvice_response_normalized )
