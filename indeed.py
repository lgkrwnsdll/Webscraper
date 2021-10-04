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

def extract_job(html):
    title = html.find('h2', {'class':'jobTitle'}).text
    company = html.find('span', {'class':'companyName'})
    if company is None:
        company = ''
    else:
        company = company.text
    location = html.find('div', {'class':'companyLocation'}).text
    job_id = html['data-jk']
    return {
    'title':title, 
    'company':company, 
    'location':location, 
    'link': f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50&vjk={job_id}"
    }

def extract_indeed_jobs(last_page):
    jobs=[]
    for page in range(last_page):
        print(f'Scrapping page {page+1}')
        result = requests.get(f'{URL[:-5]}{page*LIMIT}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('a', {'class':'tapItem'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs