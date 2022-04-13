#Import Librarys
import streamlit
import pandas as pd

#Create a Fruit List Dataframe
fruits_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.title('My First Streamlit App')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#We'll add a user interactive widget called a Multi-select that will allow users to pick the fruits they want in their smoothies.
streamlit.multiselect("Pick some fruit:", list(fruits_list.index))
streamlit.dataframe(fruits_list)
