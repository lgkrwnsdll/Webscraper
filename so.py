import requests
from bs4 import BeautifulSoup

URL = f'https://stackoverflow.com/jobs?q=python'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

def extract_pages():
    result = requests.get(URL, headers=headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find('div', {'class':'s-pagination'}).find_all('a')
    max_page = pages[-2].get_text(strip=True)
    return int(max_page)

def extract_job(html):
    title = html.find('h2', {'class':'mb4 fc-black-800 fs-body3'}).get_text(strip=True)
    company, location = html.find('h3', {'class':'fc-black-700 fs-body1 mb4'}).find_all('span', recursive=False)
    job_id = html['data-jobid']
    return {
    'title':title, 
    'company':company.get_text(strip=True), 
    'location':location.get_text(strip=True), 
    'link': f"https://stackoverflow.com/jobs?id={job_id}&q=python"
    }

def extract_jobs(last_page):
    jobs=[]
    for page in range(last_page):
        print(f'Scrapping SO page {page+1}')
        result = requests.get(f'{URL}&pg={page+1}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class':'-job'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    max_pages = extract_pages()
    jobs = extract_jobs(max_pages)
    return jobs