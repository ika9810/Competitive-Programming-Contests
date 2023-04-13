import requests
import datetime
import pytz
from bs4 import BeautifulSoup

def get_contest_info(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')

    output = ''
    for table in tables:
        output += '|'.join([' Contest ID ', ' Title ', ' Start Time ', ' End Time ']) + '|\n'
        output += '|'.join(['---'] * 4) + '|\n'
        for row in table.tbody.find_all('tr'):
            cols = row.find_all('td')
            if len(cols[1].text.strip()) == 0 or cols[1].text.strip() == "대회":
                continue
            else:
                output += f"| {cols[0].text.strip()} | {cols[1].text.strip()} | {cols[2].text.strip()} | {cols[3].text.strip()} |\n"
        output += '\n'
    return output

def save_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
        f.close()

def main():
    url = 'https://www.acmicpc.net/contest/other/list'
    output = get_contest_info(url)

    timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    timeformat = f"{timeformat.strftime('%Y-%m-%d')}"
    dateformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    date = f"{dateformat.strftime('%Y/%m/%d, %H:%M:%S')}"

    f = open('README.md')
    lines = f.readlines()
    f.close()
    
    res = "".join(lines[:7])
    output = res + '\n' + output + "Updated at " + date + '\n'
    save_to_file('README.md', output)

    archive_filename = './archive/' + timeformat + ".md"
    output += "Updated at " + date + '\n'
    save_to_file(archive_filename, output)

if __name__ == "__main__":
    main()
