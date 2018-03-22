'''
Created on 22 Mar 2018

@author: olaska
'''
import pandas as pd
import csv
import json
import requests

#DataFrame is created from file get from url
df=pd.read_json('url.someaddress')
#this allow to change name columns from original file
df.columns=['col_1','col_2','col_3','etc']
#DataFrame transformed into csv file
csv=df.to_csv()


#retrieve data(can be as json/csv file - depends on available API
r = requests.get('url.someadress').json()
#pandas retrieve json file from url
json = pd.read_json('http://someadress')
#creates csv file as a string
csv = str(json.to_csv())
#splits string into numerous line representing rows
csv = csv.split('\n')
#loop
for row in csv:
    
                print(type(row))
                #row = row.split(',')
                #row = row[1:]
                #row = ','.join(row)
                #print(row)
#csv = csv[1:]
#glues again
#csv = '\n'.join(csv)
#it creates /writes into and close a csv file

with open('someFile.csv', 'w') as f:
 f.write(csv)
  