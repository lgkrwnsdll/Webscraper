import requests
from bs4 import BeautifulSoup

indeed_result = requests.get('https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50&start=99999')

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find('div', {'class':'pagination'})

max_page = int(pagination.find('b').text)