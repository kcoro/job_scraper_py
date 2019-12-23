import requests
from bs4 import BeautifulSoup

url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=software+engineer&sc.keyword=software+engineer&locT=C&locId=1138960&jobType="

soup = BeautifulSoup(url)

print(soup)
