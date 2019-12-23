import requests
from bs4 import BeautifulSoup

monsterUrl = "https://www.monster.com/jobs/search/?q=Software-Engineer&where=Raleigh__2C-NC&intcid=skr_navigation_nhpso_searchMain"
indeedUrl = "https://www.indeed.com/jobs?q=Software+Engineer&l=Raleigh%2C+NC#"
monsterPage = requests.get(monsterUrl)
monsterSoup = BeautifulSoup(monsterPage.content, "html.parser")
indeedPage = requests.get(indeedUrl)
indeedSoup = BeautifulSoup(indeedPage.content, "html.parser")

# Validate host responds with 200 ok.
if (monsterPage.status_code != 200):
    quit
else:
    print(monsterPage.status_code)

print(monsterSoup.prettify())

