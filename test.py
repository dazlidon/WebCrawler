from lxml import html
import requests
import re

from bs4 import BeautifulSoup

page = requests.get('https://www.anuntul.ro/anunturi-imobiliare-vanzari/garsoniere/?search%5Bsumar%5D%5BrubricaId%5D=1&search%5Bsumar%5D%5BsubrubricaId%5D=3&search%5Bzona%5D%5B%5D=Bucure%C8%99ti&search%5Bfields%5D%5B0%5D%5Bfields%5D%5B1%5D%5Bvalue%5D%5Bmin%5D=&search%5Bfields%5D%5B0%5D%5Bfields%5D%5B1%5D%5Bvalue%5D%5Bmax%5D=&search%5Bmetrou%5D=&search%5Bschita%5D=&search%5BcautareId%5D=&search%5Bquery%5D=&search%5Bsortf%5D=valabilitate.sort&search%5Bsorts%5D=-1&search%5Bpage%5D=&search%5Bowner%5D=')
tree = html.fromstring(page.content)
html_content = page.text
soup = BeautifulSoup(html_content, "html.parser")
list1 = soup.find_all('div', attrs={"class":"i-cb"})
list_of_ids = []
for i in range (0,len(list1)):
   # print(str(list1[i]).split("\n")[0])
    #print(re.sub(r'id="adi-%"',str(list1[i])))
    splitting = str(list1[i]).split('"')[3]
    list_of_ids.append(splitting)
    #print(list_of_ids)
print(list_of_ids)
for y in list_of_ids:
    print(y)
    string_for_title = '//*[@id="placeholder"]/div[2]/div/div[1]/div[1]/a/text()'.replace("placeholder",y)
    string_for_price = '//*[@id="placeholder"]/div[2]/div/div[1]/div[2]/text()'.replace("placeholder",y)
    string_for_space = '//*[@id="placeholder"]/div[2]/div/div[1]/div[4]/ul/li[1]/text()'.replace("placeholder",y)
    string_for_year = '//*[@id="placeholder"]/div[2]/div/div[1]/div[4]/ul/li[2]/text()'.replace("placeholder",y)
    string_for_floor = '//*[@id="placeholder"]/div[2]/div/div[1]/div[4]/ul/li[4]/text()'.replace("placeholder",y)
    title = tree.xpath(string_for_title)
    price = tree.xpath(string_for_price)
    space = tree.xpath(string_for_space)
    year = tree.xpath(string_for_year)
    floor = tree.xpath(string_for_floor)

    print('Titlul Anuntului este:' + str(title))
    print('Pretul este: ' + str(price))
    print('Spatiul oferit este de :' + str(space))
    print('Anul constructiei este:' + str(year))
    print('Etajul la care se afla:' + str(floor))
print('Numarul de anunturi este de:' + str(len(list1)))


for z in range (0,len(list1)):
    modified_price= int(float(str(price).replace("€","").replace(" ","").replace("'","").replace("[","").replace("]","")))
if modified_price < int(70.000):
    print('Avem un apartament sub limita noastra' + str(title))
