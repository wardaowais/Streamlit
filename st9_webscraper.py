#need to install bs4 use pip install bs4
#need to install lxml use pip install lxml
import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser #with the help of webbrowser we can open a new tab of web 

#page configration to change title or icon
st.set_page_config(page_title="Web Scraper",page_icon=":books:",layout="wide")#icon search from webfx.com #https://www.webfx.com/tools/emoji-cheat-sheet/
with open("designing.css") as  source_des:
         st.markdown(f"<style>{source_des.read()}</style>",unsafe_allow_html=True)      

st.markdown("<h1 style = 'text-align: center;'>Web scraper application</h1>",unsafe_allow_html=True)
with st.form("search"):
         
         keyword= st.text_input("Enter your keyword")
         search = st.form_submit_button("Search")
placeholder = st.empty()
if keyword:
         page= requests.get(f"https://unsplash.com/s/photos/{keyword}")
         soup = BeautifulSoup(page.content,features='lxml')
         rows = soup.find_all("div", class_="ripi6")
         col1,col2 = placeholder.columns(2)
         #enumerate funtion returns 2 values 1st is index of value 2nd is the actual value
         #so here index go in index variable and actual value goes in row variable
         for index,row in enumerate(rows):
                  figures= row.find_all("figure")
                  for i in range(3):
                           #getting image tag with its class
                           img= figures[i].find("img",class_="tB6UZ")
                           list=img["srcset"].split("?")
                           anchor = figures[i].find("a",class_="rEAWd")
                           print(anchor["href"])
                
                           if i==0:
                                   col1.image(list[0])
                                   btn = col1.button("Download",key=str(index)+str(i))
                                   if btn :
                                           webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])
                           else:
                                   col2.image(list[0])
                                   btn = col2.button("Download",key=str(index)+str(i))
                                   if btn :
                                           webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])
                                    




