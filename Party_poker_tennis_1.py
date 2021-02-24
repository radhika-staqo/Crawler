import time
from datetime import datetime
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as e
from re import search

driver = webdriver.Chrome(executable_path="chromedriver.exe")

url = "https://sports.partypoker.com/en/sports/tennis-5/betting/grand-slam-tournaments-5"
driver.get(url)
time.sleep(10)
#print(driver.title)
#driver.close()
 





#for the playernames
def pl_name(str):
    for j in range(1,5):
        for i in range(1, 3):
            name_game_xpath = '//*[@id="main-view"]/ms-fixture-list/div/div/div/div/ms-grid/ms-event-group['+str(j)+']/ms-event[1]/div/a/ms-event-detail/ms-event-name/ms-inline-tooltip/div/div['+str(i)+']/div/div'
            name_text = driver.find_element_by_xpath(name_game_xpath).text
            print (str)
            return;
       
#for the playerscores
def pl_score(str1):
    for k in range(1,3):
        for l in range(1, 3):
            score_xpath = '//*[@id="main-view"]/ms-fixture-list/div/div/div/div/ms-grid/ms-event-group['+str(m)+']/ms-event/div/div/ms-option-group['+str(k)+']/ms-option['+str(l)+']/ms-event-pick/div/div/ms-font-resizer'
            score_text = driver.find_element_by_xpath(score_xpath).text
            print (str1)
            return;


#for the substring      
substring = "MEN"
substring1 = "WOMEN"

#for the fullstring    
for p in range(1,5):
    match_xpath = '//*[@id="main-view"]/ms-fixture-list/div/div/div/div/ms-grid/ms-event-group['+str(p)+']/div/ms-league-header/div[2]/span'
    fullstring = "driver.find_element_by_xpath(match_xpath).text"



#separating for both men and women
if search(substring, fullstring) :
    pl_name('Men'+ name_text)
    pl_score('Men'+ score_text)
       
elif search(substring1, fullstring) :
    pl_name('Women'+ name_text)
    pl_score('Women'+ score_text)

else :
    pl_name('Doubles'+ name_text)
    pl_score('Doubles'+ score_text)
   
#for file date and time
def file_name_date_time():
    now = datetime.now()
    dt_string = now.strftime("Party_Poker_Tennis_%d-%m-%Y_Time_%H_%M_%S")
    return dt_string

#creation of json file
def create_json(text):
    name = file_name_date_time()
    with open(name+'.json', "w") as outfile:
        json_file = json.dump(text, outfile, indent=5)
    return json_file

#dump into json file
def fun():
    team_list = []
    create_json(team_list)
    
#calling the dump function
fun()

