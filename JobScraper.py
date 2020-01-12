import requests
from bs4 import BeautifulSoup

headers = "Insert Fake User agent Here"

# Job Site URLs, use requests to get html from each URL.
# Pass requests output to BeautifulSoup for parsing
monsterUrl = "https://www.monster.com/jobs/search/?q=Software-Engineer&where=NC&tm=14"
stackOverflowUrl = "https://stackoverflow.com/jobs?q=Software+Engineer&l=North+Carolina%2C+USA&d=20&u=Miles"
indeedUrl = "https://www.indeed.com/jobs?q=software+engineer&l=Raleigh,+NC&explvl=entry_level"
# Use requests library to make get request to each websites URL
monsterPage = requests.get(monsterUrl)
stackOverflowPage = requests.get(stackOverflowUrl)
indeedPage = requests.get(indeedUrl)
# Use bs4 to parse each html page response
monsterSoup = BeautifulSoup(monsterPage.content, "html.parser")
stackOverflowSoup = BeautifulSoup(stackOverflowPage.content, "html.parser")
indeedSoup = BeautifulSoup(indeedPage.content, "html.parser")

# Validate each jobsite host responds with 200 ok.
def validateSite(sitePage):
    if (sitePage.status_code != 200):
        print("Error validating ", sitePage)
        quit
    else:
        print(sitePage.status_code)

validateSite(monsterPage)
validateSite(stackOverflowPage)
validateSite(indeedPage)

# Loop over jobs on Monster web page
for job in monsterSoup.find_all("div", class_="flex-row"):
    # Each job title
    jobTitle = job.find("a")
    # Make object a string and strip lead and trail white space
    jobTitle = jobTitle.text.strip()
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
for job in indeedSoup.find_all("div", class_="jobsearch-SerpJobCard"):
    # Each job title
    jobTitle = job.find("a", class_="jobtitle")
    # Make object a string and strip lead and trail white space
    jobTitle = jobTitle.text.strip()
    # Gets the jobs company name
    jobCompany = job.find("span", class_="company")
    # Make object into string and strip lead and trail whitespace
    jobCompany = jobCompany.text.strip()
    # Gets jobs location
    jobLocation = job.find("span", class_="location")
    # Turn object into string and strip lead and trail whitespace
    if jobLocation != None:
        jobLocation = jobLocation.text.strip()
    # Link to job info
    jobLink = job.find("a", class_="jobtitle")["href"]
    # Strip "/rc/clk" from href link on indeed
    jobLink = jobLink[7:]

    # Print Job title, and link to job desc
    print(jobTitle)
    print(jobCompany)
    print(jobLocation)
    print("https://www.indeed.com/viewjob"+jobLink)
    print("\n")

# Loop over jobs on StackOverflow jobs page
for job in stackOverflowSoup.find_all("div", class_="-job"):
    # Each job title
    jobTitle = job.find("a", class_="job-link")
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

