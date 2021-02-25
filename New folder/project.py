import time
from datetime import datetime
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as e
from re import search

# functions

def get_xpath_value(xpath):
    return driver.find_element_by_xpath(xpath)


def get_title(group):
    title_xpath = '//*[@id="main-view"]/ms-fixture-list/div/div/div/div/ms-grid-list/ms-event-group['+str(group)+']/ms-compact-event/div/a/div'
    return get_xpath_value(title_xpath).text
    
    
def get_winner(group,event):
    winner_xpath ='//*[@id="main-view"]/ms-fixture-list/div/div/div/div/ms-grid-list/ms-event-group['+str(group)+']/ms-compact-event/ms-option-panel/ms-regular-option-group/div/ms-option['+str(event)+']/ms-event-pick/div/div[1]'
    return get_xpath_value(winner_xpath).text


def get_score(group,event):
    score_xpath = '//*[@id="main-view"]/ms-fixture-list/div/div/div/div/ms-grid-list/ms-event-group['+str(group)+']/ms-compact-event/ms-option-panel/ms-regular-option-group/div/ms-option['+str(event)+']/ms-event-pick/div/div[2]'
    return get_xpath_value(score_xpath).text


def press_button(group):
    button_xpath = '//*[@id="main-view"]/ms-fixture-list/div/div/div/div/ms-grid-list/ms-event-group['+str(group)+']/ms-compact-event/ms-option-panel/ms-regular-option-group/div/div/span/span'
    click = driver.find_element_by_xpath(button_xpath).click()
    time.sleep(5)
    return
    
def get_group():
    group_xpath = '//*[@id="main-content"]/ms-main/ms-column/div[1]/ms-competition-navigation/ms-competition-tree/ms-item-tree[2]/ms-item-tree/ms-item-tree/ms-item[1]/a/div[3]'
    return int(driver.find_element_by_xpath(group_xpath).text)


def create_dict(group,event):
#     print(get_winner(group,event))
#     print(get_score(group,event))
    data = {'name': get_winner(group,event), 'score': get_score(group,event)}
    return data
    
def get_data(group,title):
    winner_list = []
    for event in range(1,60):
        try:
            winner_data = create_dict(group,event)
            winner_list.append(winner_data)
        except e:
            pass
    return winner_list
        
def run():
    data = {'men_data': [], 'women_data': []}
    for group in range(1,get_group()+1):
        press_button(group)
        try:
            if 'Men' in get_title(group):
                men_dict = {'title': get_title(group), 'winner_list': get_data(group,get_title(group))}
                data['men_data'].append(men_dict)
            elif 'Women' in get_title(group):
                women_dict = {'title': get_title(group), 'winner_list': get_data(group,get_title(group))}
                data['women_data'].append(women_dict)
        except e:
            pass
    print(data)
    create_json(data)


# Getting date and time 
def file_name_date_time():
    now = datetime.now()
    dt_string = now.strftime("Party_Poker_Grandslam_men_women_sep_%d-%m-%Y_Time_%H_%M_%S")
    return dt_string


# creating json
def create_json(text):
    name = file_name_date_time()
    with open(name+'.json', "w") as outfile:
        json_file = json.dump(text, outfile, indent=4)
            

#driver
driver = webdriver.Chrome(executable_path="chromedriver.exe")
url = "https://sports.partypoker.com/en/sports/tennis-5/betting/grand-slam-tournaments-5"
driver.get(url)
driver.maximize_window()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(10)
run()