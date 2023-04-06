import os
from bs4 import BeautifulSoup
import json

PARTIESCOUNT = 21
RESULTS = {}

def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [url.strip() for url in file.readlines()]
    return urls

def process_urls(urls):
    total_urls = len(urls)
    current_url = 0
    for url in urls:
        current_url += 1
        n = "./results/" + url[-16:]
        print ("Processing {}/{} URLs - {}".format(current_url, total_urls, url[-16:]))
        if os.path.exists(n) == False:
            print("File DOES NOT EXIST: ", n)
            continue
        if url[-6:] == "2.html":
            html_content = read_html_file(n)
            process_automatic_file(html_content, url[-16:-7])
        elif url[-6:] == "1.html":
            html_content = read_html_file(n)
            process_human_file(html_content, url[-16:-7])
        #if current_url > 100:
        #    break

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def process_automatic_file(html_content, sectionnum):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')

    if len(tables) >= 2:
        second_table = tables[1]
        rows = second_table.find_all('tr')
        if sectionnum not in RESULTS:
            RESULTS[sectionnum] = {}
        if "auto_machine" not in RESULTS[sectionnum]:
            RESULTS[sectionnum]["auto_machine"] = {}

        if len(rows) < PARTIESCOUNT + 1:
            print("There are less than 22 rows in the HTML file.", sectionnum)
        for i in range(1, len(rows)):
            row = rows[i]
            cells = row.find_all(['td', 'th'])
            RESULTS[sectionnum]["auto_machine"][cells[0].text] = cells[2].text
    else:
        print("There are less than 2 tables in the HTML file.", sectionnum)

def process_human_file(html_content, sectionnum):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')

    if sectionnum not in RESULTS:
        RESULTS[sectionnum] = {}
    if "auto_machine" not in RESULTS[sectionnum]:
        RESULTS[sectionnum]["human_machine"] = {}
        RESULTS[sectionnum]["human_paper"] = {}
        RESULTS[sectionnum]["human_total"] = {}

    if len(tables) >= 8:
        second_table = tables[7]
        rows = second_table.find_all('tr')

        if len(rows) < PARTIESCOUNT*3 + 1:
            print("There are less than 67 rows in the HTML file.", sectionnum)
        for i in range(1, len(rows), 3):
            row_paper = rows[i]
            row_machine = rows[i+1]
            row_total = rows[i+2]
            cells_paper = row_paper.find_all(['td', 'th'])
            cells_machine = row_machine.find_all(['td', 'th'])
            cells_total = row_total.find_all(['td', 'th'])
            RESULTS[sectionnum]["human_paper"][cells_paper[0].text] = cells_paper[2].text.replace("Хартиени (х): ", "")
            RESULTS[sectionnum]["human_machine"][cells_paper[0].text] = cells_machine[0].text.replace("Машинни (м): ", "")
            RESULTS[sectionnum]["human_total"][cells_paper[0].text] = cells_total[0].text.replace("Общо (о): ", "")
    elif len(tables) >= 5:
        second_table = tables[4]
        rows = second_table.find_all('tr')
        if len(rows) < PARTIESCOUNT + 1:
            print("There are less than 22 rows in the HTML file.", sectionnum)
        for i in range(1, len(rows)):
            row = rows[i]
            cells = row.find_all(['td', 'th'])
            RESULTS[sectionnum]["human_total"][cells[0].text] = cells[2].text
    else:
        print("There are less than 8 tables in the HTML file.", sectionnum)

if __name__ == '__main__':
    file_path = './data/urls.txt' # file with URLs
    output_path = './data/results.json' # file with results in JSON format
    urls = read_urls_from_file(file_path)
    process_urls(urls)
    with open(output_path, 'w') as file:
        json.dump(RESULTS, file)
