import requests
from bs4 import BeautifulSoup
import csv
import json

listAllJobs = []
# Job Site default URLs, use requests to get html from each URL.
# Pass requests output to BeautifulSoup for parsing
monsterUrl = "https://www.monster.com/jobs/search/?q=Software+Engineer&where=North-Carolina"
stackOverflowUrl = "https://stackoverflow.com/jobs?q=Software+Engineer&l=North+Carolina%2C+USA&d=20&u=Miles"
indeedUrl = "https://www.indeed.com/jobs?q=software+engineer&l=Raleigh,+NC&explvl=entry_level"

# Will prompt user to enter desired title and location
# Remove spaces in users input with char's needed for search query
print("Enter desired job title:")
userJobTitle = input()
userJobTitle = userJobTitle.replace(" ","+").replace(",", "");
print("Enter search location (eg. Raleigh, NC):")
userLocation = input()
userLocation = userLocation.replace(" ","+").replace(",", "");
print("Enter a name for the output csv file, include .csv extension:")
userFileName = input()

# Update job sites default url with user input query parameters
monsterUrl = "https://www.monster.com/jobs/search/?q="+userJobTitle+"&where="+userLocation
stackOverflowUrl = "https://stackoverflow.com/jobs?q="+userJobTitle+"&l="+userLocation+"%2C+USA&d=20&u=Miles"
indeedUrl = "https://www.indeed.com/jobs?q="+userJobTitle+"&l="+userLocation+"&explvl=entry_level"

# Use requests library to make get request to each websites URL
monsterPage = requests.get(monsterUrl)
stackOverflowPage = requests.get(stackOverflowUrl)
indeedPage = requests.get(indeedUrl)
# Use bs4 to parse each html page response
monsterSoup = BeautifulSoup(monsterPage.content, "html.parser")
stackOverflowSoup = BeautifulSoup(stackOverflowPage.content, "html.parser")
indeedSoup = BeautifulSoup(indeedPage.content, "html.parser")

print(f"Please hold, scraping jobs for {userJobTitle} in {userLocation}")

# Validate each jobsite host responds with 200 ok.
def validateSite(sitePage):
    if (sitePage.status_code != 200):
        print("Error validating ", sitePage)
        quit


# Validating each jobsites http status response.
validateSite(monsterPage)
validateSite(stackOverflowPage)
validateSite(indeedPage)


# Output job site results to csv file
def outputToCSV(jobTitle, jobCompany, jobLocation, jobLink):
    with open(userFileName, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([jobTitle, jobCompany, jobLocation, jobLink])


# Loop over jobs on Monster's page
for job in monsterSoup.find_all("div", class_="flex-row"):
    # Each job title
    jobTitle = job.find("a")
    # Make object a string and strip lead and trail white space
    jobTitle = jobTitle.text.strip()
    # Gets the jobs company name
    jobCompany = job.find("div", class_="company").find("span", class_="name")
    # Make object into string and strip lead and trail whitespace
    jobCompany = jobCompany.text.strip()
    # Gets jobs location
    jobLocation = job.find("div", class_="location").find("span", class_="name")
    # Turn object into string and strip lead and trail whitespace
    if jobLocation != None:
        jobLocation = jobLocation.text.strip()
    # Link to job info
    jobLink = job.find("a")["href"]
    # Strip lead and trail whitespace
    jobLink = jobLink.strip()

    # Adds job site output to csv file
    outputToCSV(jobTitle, jobCompany, jobLocation, jobLink)
    # Appends each jobs output to a list of dictionaries
    listAllJobs.append({'jobTitle': jobTitle, 'jobCompany': jobCompany, 'jobLocation': jobLocation, 'jobLink': jobLink})


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
    jobLink = "https://www.indeed.com/viewjob"+jobLink

    # Adds job site output to csv file
    outputToCSV(jobTitle, jobCompany, jobLocation, jobLink)
    # Appends each jobs output to a list of dictionaries for conversion to json
    listAllJobs.append({'jobTitle': jobTitle, 'jobCompany': jobCompany, 'jobLocation': jobLocation, 'jobLink': jobLink})


# Loop over jobs on StackOverflow jobs page
for job in stackOverflowSoup.find_all("div", class_="-job"):
    # Each job title
    jobTitle = job.find("a", class_="s-link")
    # Make object a string and strip lead and trail white space
    jobTitle = jobTitle.text.strip()
    # Gets the jobs company name
    jobCompany = job.find("h3", class_="fc-black-700 fs-body1 mb4").find("span")
    # Make object into string and strip lead and trail whitespace
    jobCompany = jobCompany.text.strip()
    # Gets jobs location
    jobLocation = job.find("h3", class_="fc-black-700 fs-body1 mb4").find("span", class_="fc-black-500")
    # Turn object into string and strip lead and trail whitespace
    if jobLocation != None:
        jobLocation = jobLocation.text.strip()
    # Link to job info
    jobLink = job.find("a", class_="s-link")["href"]
    # Strip lead and trail whitespace
    jobLink = jobLink.strip()
    jobLink = "https://stackoverflow.com"+jobLink

    # Adds job site output to csv file
    outputToCSV(jobTitle, jobCompany, jobLocation, jobLink)
    # Appends each jobs output to a list of dictionaries
    listAllJobs.append({'jobTitle': jobTitle, 'jobCompany': jobCompany, 'jobLocation': jobLocation, 'jobLink': jobLink})


# Convert python list into json
jobsJson = json.dumps(listAllJobs, indent=4)
jsonFileName = userFileName.replace(".csv", "") + "_as_json.txt"
# Write json to output file
with open(jsonFileName, 'w') as outfile:
    outfile.write(jobsJson)

print(f"The files {userFileName} and {jsonFileName} have been created!")

# Uncomment to see json output in console for testing
# Output to console to check that json is being created, 
# and jobs are found correctly
# print(jobsJson)
