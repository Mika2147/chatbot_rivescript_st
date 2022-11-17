import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

source = "Ukrainian"
context = "Civilians"

page = requests.get("https://en.wikipedia.org/wiki/Casualties_of_the_Russo-Ukrainian_War")
soup = BeautifulSoup(page.content, "html.parser")
tables = soup.find_all('table',{'class':"wikitable"})

df=pd.read_html(str(tables[2]))
# convert list to dataframe
df=pd.DataFrame(df[0])
data = df.drop(["Time period"], axis=1)
data = df.rename(columns={"Breakdown": "type", "Casualities": "deaths"})

res = ("", "", "")
for row in data.itertuples():
    if((context in str(row[1])) and (source in str(row[4]))):
        number = str(row[2])
        #number.replace(",", "")
        number = re.search(r'\d+(?:,\d+)?', number).group()
        if len(row[1]) > len(res[0]):
            res = (row[1], number, row[4])

print(str(res[0]) + "\t" + str(res[1]) + "\t" + res[2])