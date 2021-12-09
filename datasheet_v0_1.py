'''
@Modified date : 2021-12-09 (GMT+9)
@Version : 0.1
@Author : King_chobab(Contact Forum or king_chobab@naver.com)

--- Next Update ---
1. Add function to call breed information.
    Breeds with overlapping descriptions cannot be classified normally.
    (Ex-zyumorph, some of Holiday dragons)
2. Add function to call Spouse list
-------------------
※WARNING※
The API key has been removed according to the DC API policy.
Please inserting the API key you have after compile.
'''

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import re
import os

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
    print(code + ' : ' + gen)
    return int(gen.strip())

def ScrollListUp(user, key):
    url = 'https://dragcave.net/api/' + key + '/json/user/' + user
    data = requests.get(url).json()
    data = data['dragons']
    df = pd.DataFrame().from_dict(data, orient='index').reset_index(drop=True)
    df = df[['id', 'name', "start", 'grow', 'death', 'gender', 'parent_f', 'parent_m']]
    res = df[(df['grow'] != '0') & (df['death'] == '0') & (df['gender'] != '')].reset_index(drop=True)
    und = ['Update soon!' for i in range(len(res))]
    res.insert(2, 'breed', und)
    res['Gen'] = [1 if res['parent_f'][i]=='' else find_gen(res['id'][i]) for i in range(len(res))]
    res['Spouse'] = und
    res.columns = ['ID', 'Name', 'Breed', 'Born', 'grow', 'death', 'Sex', 'Mother', 'Father', 'Gen', 'Spouse']
    return res[['ID', 'Name', 'Breed', 'Born', 'Sex', 'Mother', 'Father', 'Gen', 'Spouse']]

key = input('Enter your API Key >> ')
uid = input('Enter your ID >> ')
try:
    uid = str(uid)
    key = str(key)
except:
    print('Please check that the entered ID and API key are correct.(Do not include spaces)')
    os.system('pause')
try:
    df = ScrollListUp(uid, key)
    df.to_csv(uid + '.csv')
except:
    os.system('pause')
