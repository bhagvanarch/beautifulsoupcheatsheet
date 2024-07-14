from bs4 import BeautifulSoup

import requests as reqs



url = 'https://www.google.com'

resp = reqs.get(url)

html_doc = resp.content



beautsoup = BeautifulSoup(html_doc, 'lxml')



content_headline = beautsoup.title.string

content_links = beautsoup.find_all('a')

print(content_headline)

for content_link in content_links:
    print(content_link.get('href'))