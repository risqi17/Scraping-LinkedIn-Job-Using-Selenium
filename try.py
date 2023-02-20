from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome('chromedriver')
driver.get('https://hoopshype.com/salaries/players/')

players = driver.find_elements("xpath", '//td[@class="name"]')

players_list = []
for p in range(len(players)):
    players_list.append(players[p].text)

salaries = driver.find_elements("xpath",'//td[@class="hh-salaries-sorted"]')

salaries_list = []
for s in range(len(salaries)):
    salaries_list.append(salaries[s].text)

df = pd.DataFrame(columns=['Player','Salary','Year']) # creates master dataframe 

driver = webdriver.Chrome('chromedriver')

for yr in range(1990,2019):
    page_num = str(yr) + '-' + str(yr+1) +'/'
    url = 'https://hoopshype.com/salaries/players/' + page_num
    driver.get(url)
    
    players = driver.find_elements("xpath",'//td[@class="name"]')
    salaries = driver.find_elements("xpath",'//td[@class="hh-salaries-sorted"]') 
    
    players_list = []
    for p in range(len(players)):
        players_list.append(players[p].text)
    
    salaries_list = []
    for s in range(len(salaries)):
        salaries_list.append(salaries[s].text)
    
    data_tuples = list(zip(players_list[1:],salaries_list[1:])) # list of each players name and salary paired together
    temp_df = pd.DataFrame(data_tuples, columns=['Player','Salary']) # creates dataframe of each tuple in list
    temp_df['Year'] = yr # adds season beginning year to each dataframe
    df = df.append(temp_df) # appends to master dataframe
    
driver.close()