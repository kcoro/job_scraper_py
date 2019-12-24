import requests
from bs4 import BeautifulSoup

headers = "Insert Fake User agent Here"

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

# Validate host responds with 200 ok.
if (indeedPage.status_code != 200):
    quit
else:
    print(indeedPage.status_code)

# Loop over each product container on webpage
for job in monsterSoup.find_all("div", class_="flex-row"):
    # Each job title
    jobTitle = job.find("a")
    # Make object a string and strip lead and trail white space
    jobTitle = jobTitle.text.strip()
    # Strip trailing whitespace from job title
    # Gets the jobs company name
    jobCompany = job.find("div", class_="company")
    jobCompany = jobCompany.find("span", class_="name")
    # Make object into string and strip lead and trail whitespace
    jobCompany = jobCompany.text.strip()
    # Gets jobs location
    jobLocation = job.find("div", class_="location")
    jobLocation = jobLocation.find("span", class_="name")
    # Turn object into string and strip lead and trail whitespace
    jobLocation = jobLocation.text.strip()
    # Link to job info
    jobLink = job.find('a')['href']
    # Strip lead and trail whitespace
    jobLink = jobLink.strip()
    # Prints job title, location and link to job
    print(jobTitle)
    print(jobCompany)
    print(jobLocation)
    print(jobLink)
    print("\n")

