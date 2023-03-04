import requests
from bs4 import BeautifulSoup

url = 'https://www.acmicpc.net/contest/other/list'
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

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
    output = res + '\n' + output
    f.write(output)
    f.close()