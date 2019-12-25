import requests
from bs4 import BeautifulSoup

headers = "Insert Fake User agent Here"

# Job Site URLs, use requests to get html from each URL.
# Pass requests output to BeautifulSoup for parsing
monsterUrl = "https://www.monster.com/jobs/search/?q=Software-Engineer&where=NC&tm=14"
stackOverflowUrl = "https://stackoverflow.com/jobs?q=Software+Engineer&l=North+Carolina%2C+USA&d=20&u=Miles"
indeedUrl = "https://www.indeed.com/jobs?q=software+engineer&l=North+Carolina"
monsterPage = requests.get(monsterUrl)
monsterSoup = BeautifulSoup(monsterPage.content, "html.parser")
stackOverflowPage = requests.get(stackOverflowUrl)
stackOverflowSoup = BeautifulSoup(stackOverflowPage.content, "html.parser")
indeedPage = requests.get(indeedUrl)
indeedSoup = BeautifulSoup(indeedPage.content, "html.parser")

# Validate each jobsite host responds with 200 ok.
if (monsterPage.status_code != 200):
    quit
else:
    print(monsterPage.status_code)

if (indeedPage.status_code != 200):
    quit
else:
    print(indeedPage.status_code)

if (stackOverflowPage.status_code != 200):
    quit
else:
    print(stackOverflowPage.status_code)

# Loop over jobs on Monster web page
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
    jobLink = job.find("a")["href"]
    # Strip lead and trail whitespace
    jobLink = jobLink.strip()

    # Prints job title, company, location and link to job
    print(jobTitle)
    print(jobCompany)
    print(jobLocation)
    print(jobLink)
    print("\n")

# Loop over jobs on Indeed's page
for job in indeedSoup.find_all("div", class_="title"):
    # Each job title
    jobTitle = job.find("a")
    # Make object a string and strip lead and trail white space
    jobTitle = jobTitle.text.strip()

    # Print Job title, and link to job desc
    print(jobTitle)
    print("Indeed Sucks")
    print("http://indeedsucks.com")
    print("\n")

# Loop over jobs on StackOverflow jobs page
for job in stackOverflowSoup.find_all("div", class_="-job js-dismiss-overlay-container ps-relative p12 pl24 bg-yellow-050 bb bc-black-2"):
    # Each job title
    jobTitle = job.find("h2", class_="fs-body3 mb4 fc-black-800")
    # Make object a string and strip lead and trail white space
    jobTitle = jobTitle.text.strip()
    # Gets the jobs company name
    jobCompany = job.find("h3", class_="fc-black-700 fs-body1 mb4")
    jobCompany = jobCompany.find("span")
    # Make object into string and strip lead and trail whitespace
    jobCompany = jobCompany.text.strip()
    # Gets jobs location
    jobLocation = job.find("h3", class_="fc-black-700 fs-body1 mb4")
    jobLocation = jobLocation.find("span", class_="fc-black-500")
    # Turn object into string and strip lead and trail whitespace
    jobLocation = jobLocation.text.strip()
    # Link to job info
    jobLink = job.find("a")["href"]
    # Strip lead and trail whitespace
    jobLink = jobLink.strip()

    # Prints job title, company, location and link to job
    print(jobTitle)
    print(jobCompany)
    print(jobLocation)
    print("https://stackoverflow.com"+jobLink)
    print("\n")

