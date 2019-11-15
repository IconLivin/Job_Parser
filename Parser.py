import requests
from bs4 import BeautifulSoup as bs
from prettytable import PrettyTable as pt


headers={'accept':'*/*','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
Job=[]

def hh_parser(base_url,headers):
    urls=[]
    urls.append(base_url)
    session = requests.Session()
    request = session.get(base_url,headers=headers)
    if request.status_code==200:
        soup = bs(request.content,'html.parser')
        try:
            count = int((((soup.find_all('a',attrs={'data-qa':'pager-page'}))[-1]).text))
            for i in range(count):
                url=f'https://nn.hh.ru/search/vacancy?area=66&text=It+intern&page={i}'
                if url not in urls:
                    urls.append(url)
        except:
           pass
        for i in range(len(urls)):
            divs = soup.find_all('div',attrs={'class':'vacancy-serp-item'})
            for div in divs:
                position= div.find('a',attrs={'data-qa':'vacancy-serp__vacancy-title'}).text
                company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
                href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
                Job.append(company)
                Job.append(position)
                Job.append(href)
    else:
        print('ERROR')


base_url='https://nn.hh.ru/search/vacancy?area=66&text=c%2B%2B+intern&page=0'
hh_parser(base_url,headers)
table=pt(['Company','Position','Link'])
while Job:
    table.add_row(Job[:3])
    Job=Job[3:]
print(table)

