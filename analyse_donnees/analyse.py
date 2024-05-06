import requests

from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)

page = reponse.content
soup = BeautifulSoup(page, "html.parser")

class_name = "gem-c-document-list__item-description"

description = soup.find_all("p", class_=class_name)

print(description)