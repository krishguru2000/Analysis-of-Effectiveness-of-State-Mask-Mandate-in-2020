import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://worldpopulationreview.com/states"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser') #gets the html parser
table1 = soup.find('table') #find where it says table in html
headers = []

for i in table1.find_all('th'):
        title = i.text
        headers.append(title)

mydata = pd.DataFrame(columns = headers)
for j in table1.find_all('tr')[1:]: #makes a column for each header name
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row


df = mydata[['State  ', '2021 Population  ']] #makes a dataframe with the state name and 2021 population
df.rename(columns = {'State  ':'state'}, inplace = True)
df.rename(columns = {'2021 Population  ':'Population'}, inplace = True) #renames columns
us_state_abbrev = {
'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}
df['state'] = df['state'].map(us_state_abbrev).fillna(df['state']) #converst everything to abbreviations

df1 = pd.read_csv('covid2020.csv') #reads dtata from csv website
df2 = df1[['state', 'tot_cases']]

df3 = pd.merge(df, df2, on=['state']) #merges the population and cases by the state abbreviation
df3 = df3.replace(',','', regex=True)
df3['casepercent'] = df3['tot_cases'].astype(int)/df3['Population'].astype(int) #calculates how much of the population had covid
df4 = df3.sort_values(by=['casepercent'], ascending=False) #sorts by largest percenateg
print(df4)
df4.to_csv('casepercent.csv', index=False) #prints to csv

