import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}&start=99999'

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div', {'class':'pagination'})
    max_page = int(pagination.find('b').text)
    return max_page

def extract_indeed_jobs(last_page):
    jobs=[]
    for page in range(last_page):
        result = requests.get(f'{URL[:-5]}{page*LIMIT}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('table', {'class':'jobCard_mainContent'})
        for result in results:
            title = result.find('h2', {'class':'jobTitle'}).text
            company = result.find('span', {'class':'companyName'})
            if company is None:
                company = ''
            else:
                company = company.text
            location = result.find('div', {'class':'companyLocation'}).text
            jobs.append({'title':title, 'company':company, 'location':location})
    return jobs