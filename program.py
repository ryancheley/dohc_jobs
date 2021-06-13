from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd


chrome_options = Options()  
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

url = 'https://careers.mydohc.com/spa/listing'

driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content, "lxml")

table = soup.find('table', class_='table table-striped')
df = pd.read_html(table.prettify())[0]
df.drop(df.tail(1).index,inplace=True)
if df.shape[0] > 0:
    df.to_csv('jobs.csv')

