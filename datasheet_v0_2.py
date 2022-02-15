'''
@Modified date : 2022-02-14 (GMT+9)
@Version : 0.2
@Author : King_chobab(Contact Forum or king_chobab@naver.com)

--- Next Update ---
1. Add function to call breed information.
    Breeds with overlapping descriptions cannot be classified normally.
    (Ex-zyumorph, some of Holiday dragons)
2. Make GUI or Create a website to built-in
-------------------

--- Update History ---
1. Error handling for situations in which data cannot be retrieved has been fixed in general.
    - Added a notification for users who don't own a gendered adult dragon,
      or users who cannot retrieve adult dragon information because "Hide adults on scroll(in Account settings)" is enabled.
    - The message displayed when
       "Hide scroll" is activated and data cannot be retrieved
        or
       cannot be found due to incorrect user ID input has been changed.
2. Add function to call Spouse list
    - For dragons with children only, store that spouse and the number of children with the spouse in the Spouse column.
    - ex) GVlJ8's Spouses : ['IQSf2', 8], ['vS6j7', 3], ['AavMD', 1], ['7oipH', 1], ['tzKSx', 1]
    - It is not possible to search for a spouse who actually tried to mate but does not have children.
3. Added a guide to see the progress.
4. Made options for loading generation info and spouse list selectable.
    - Loading the dragon's generation info and spouse list will take much longer.
      So I modified them to be selectable.
5. Added date to the name of the file being saved.
    - Existing: King_chobab.csv
      After change: King_chobab_2022-02-14.csv
6. Added guidance to let you know how long it will take to clean up your scroll data.
    - The unit is seconds.
---------------

※WARNING※
The API key has been removed according to the DC API policy.
Please inserting the API key you have after compile.
'''

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import re
import os
import time

def exthtml(link):
    req = requests.get(link)
    return bs(req.text, 'html.parser')

def removetag(text):
    return re.sub('<.*?>', '', text)

def find_gen(code):
    bshtml = exthtml('https://dragcave.net/lineage/' + str(code))
    gen = bshtml.find('span', attrs={'class' : '_2y_r'})
    gen = str(gen)
    gen = removetag(gen)
    print('[Gen][' + code + '] ' + gen + 'G')
    return int(gen.strip())

def find_spouse(code, key):
    data = requests.get('https://dragcave.net/api/' + key + '/json/children/' + code).json()
    try:
        data = data['dragons']
    except:
        print("[Spause][" + code + "] Can't find Dragon")
        return "Can't find Dragon"
    
    df = pd.DataFrame().from_dict(data, orient='index')
    
    gender = df.loc[code]['gender']
    df = df[['parent_f', 'parent_m']]
    
    if gender == 'Female':
        df = df[df['parent_f'] == code]
        pdf = df['parent_m'].value_counts()
    elif gender == 'Male':
        df = df[df['parent_m'] == code]
        pdf = df['parent_f'].value_counts()
    
    slist = pdf.reset_index().values.tolist()
    print("[Spouse][" + code + "] Add Spouses")
    slist = str(slist)
    if len(slist) > 2:
        return slist[1:len(slist)-1]
    else:
        return ''
    

def ScrollListUp(user, key, gnbool, spbool):
    print("Call data ... ", end='')
    url = 'https://dragcave.net/api/' + key + '/json/user/' + user
    data = requests.get(url).json()
    print("Complete")
    ecode = data['errors']
    print("Error code extraction Complete")
    if len(ecode) == 0:
        data = data['dragons']
        df = pd.DataFrame().from_dict(data, orient='index').reset_index(drop=True)
        df = df[['id', 'name', "start", 'grow', 'death', 'gender', 'parent_f', 'parent_m']]
        print("Dragon data extraction Complete")

        res = df[(df['grow'] != '0') & (df['death'] == '0') & (df['gender'] != '')].reset_index(drop=True)
        print("Filter Complete")
        
        und = ['Update soon!' for i in range(len(res))]
        
        res.insert(2, 'breed', und)
        print("Add Breed column Complete")
        
        if gnbool:
            res['Gen'] = [1 if res['parent_f'][i]=='' else find_gen(res['id'][i]) for i in range(len(res))]
            print("Find Generations Complete")
        else:
            res['Gen'] = ""
            print("Add Generations column Complete")
        if spbool:
            res['Spouse'] = [find_spouse(res['id'][i], key) for i in range(len(res))]
            print("Find Spouses Complete")
        else:
            res['Spouse'] = ""
            print("Add Spouses column Complete")
            
        res.columns = ['ID', 'Name', 'Breed', 'Born', 'grow', 'death', 'Sex', 'Mother', 'Father', 'Gen', 'Spouse']
        if len(res) > 0:
            print("Terminated successfully")
            return res[['ID', 'Name', 'Breed', 'Born', 'Sex', 'Mother', 'Father', 'Gen', 'Spouse']]
        else:
            print("Can't find Dragons")
            return 0
    else:
        print(ecode[0][1])
        return -1

def input_value(question):
    temp = input(question)
    if ((temp == "Y") or (temp == "y")):
        return True
    elif ((temp == "N") or (temp == "n")):
        return False
    else:
        temp = input_value(question)
        return temp
        
uid = input('Enter your ID >> ')
try:
    uid = str(uid)
except:
    print('Please check that the entered ID is correct.(Do not include spaces)')
    os.system('pause')
    exit()
key = input('Enter your API Key >> ')
try:
    uid = str(uid)
except:
    print('Please check that the entered API key is correct.')
    os.system('pause')
    exit()

gen = input_value("Do you want to load Generation?(This option takes more time.)(Y/N) >> ")
sps = input_value("Do you want to load Spouse list?(This option takes more time.)(Y/N) >> ")
t_start = time.time()

df = ScrollListUp(uid, key, gen, sps)
if str(type(df)) == "<class 'pandas.core.frame.DataFrame'>":
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    df.to_csv(uid + '_' + date + '.csv')
    print('The file was saved as "' + uid + '_' + date + '.csv\".')
elif df == 0:
    print("Can't find gendered adult dragons.\nIf this error occurs even though you have an adult dragon, please check if 'Hide adults on scroll' is disabled in dragcave.net under Account > Account Settings > Scroll Settings.")
print("Time Taken :", round(time.time() - t_start, 3), "sec")
os.system('pause')