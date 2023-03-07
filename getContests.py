import requests
import datetime
import pytz
from bs4 import BeautifulSoup

url = 'https://www.acmicpc.net/contest/other/list'
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
timeformat = f"{timeformat.strftime('%Y-%m-%d')}"
dateformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
date = f"{dateformat.strftime('%Y/%m/%d, %H:%M:%S')}"

soup = BeautifulSoup(response.text, 'html.parser')
tables = soup.find_all('table')

output = ''
for table in tables:
    output += '|'.join([' Contest ID ', ' Title ', ' Start Time ', ' End Time ']) + '|\n'
    output += '|'.join(['---'] * 4) + '|\n'
    for row in table.tbody.find_all('tr'):
        cols = row.find_all('td')
        output += f"| {cols[0].text.strip()} | {cols[1].text.strip()} | {cols[2].text.strip()} | {cols[3].text.strip()} |\n"
    output += '\n'

f = open('README.md')
lines = f.readlines()
f.close()
with open('README.md', 'w') as f:
    res = ""
    for i in range(7):
        res += lines[i]
    output = res + '\n' + output + "Updated at " + date + '\n'
    f.write(output)
    f.close()

with open('./archive/'+timeformat+".md", 'w') as f:
    output += "Updated at " + date + '\n'
    f.write(output)
    f.close()
