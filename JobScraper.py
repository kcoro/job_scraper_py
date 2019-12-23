import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.com/jobs?q=Software+Engineer&l=Raleigh%2C+NC#"
indeedPage = requests.get(url)
indeedSoup = BeautifulSoup(indeedPage.content, "html.parser")

print(indeedSoup)
