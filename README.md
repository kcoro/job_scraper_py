# JobScraper in Python
To run this application you will need the following libraries:
* requests
* beautifulsoup


#### How to install libraries
```python -m pip install requests```

```python -m pip install beautifulsoup4```


#### How to run JobScraper
Navigate to directory containing jobScraper.py

````python jobScraper.py````


#### This program will
* Run in the cli, and prompt user for:
  * Job Title
  * Job Location
  * Name for csv file
* Create a csv file containing scraped jobs info
* Create a txt file with json


#### Example usage
````python jobScraper.py````

Enter desired job title:

````Software Engineer````

Enter search location (eg. Raleigh, NC):

````Raleigh, NC````

Enter a name for the output csv file, include .csv extension:

````Raleigh_Jobs.csv````

Please hold, scraping jobs for Software+Engineer in Raleigh+NC

The files Raleigh_Jobs.csv and Raleigh_Jobs_as_json.txt have been created!
