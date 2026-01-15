import requests
from bs4 import BeautifulSoup
import os
import csv


FilePath = '/Users/payalingale01/Projects/PythonProjects/job_scraper/savedata.csv'
#step1:Get the webpage
BASE_URL = 'https://realpython.github.io/fake-jobs/'

def fetch_page(url):
  try:
    
    print('Fetching web data')
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    response = requests.get(BASE_URL,headers=headers)
    if response.status_code == 200:
      print('Page loaded successfully')
    else:
      print(f'Faced difficulty while loading data {response.status_code}')  
    return response.text 
  except Exception as e:
    return {f'error as {str(e)}'}
  

#step2:Parse Data
def parseData():
  html = fetch_page(BASE_URL)
  soup = BeautifulSoup(html,'html.parser')
  job_cards = soup.findAll('div',class_='card-content')
  jobs=[]

  for cards in job_cards:
        try:
        # Extract job title
          jobTitle = cards.find('h2',class_='title').text.strip()
          
          # print(f'Job Title :- {jobTitle}')
        # Extract company
          jobCompany = cards.find('h3',class_='company').text.strip()
          # print(f'job Company :- {jobCompany}')
        # Extract location
          jobLocation = cards.find('p',class_='location').text.strip()
          # print(f'Extract location :- {jobLocation}')
        # Extract date posted
          jobPostedDate = cards.find('p',class_='is-small').text.strip()
          # print(f'Extract date posted :- {jobPostedDate}')
        # Create job dict
          job={
           'jobTitle':jobTitle.lower(),
           'jobCompany':jobCompany,
           'jobLocation':jobLocation,
           'jobPostedDate':jobPostedDate
            }
          jobs.append(job)
          
        except Exception as e:
           return {f'error as {str(e)}'}
  return jobs


def filterJobs(jobs):
   jobTitle = input('Enter the job title to be searched')
   filteredList = []
   for job in jobs:
          if jobTitle.lower() in job['jobTitle'].lower():
            filteredList.append(job)
   saveToCsv(filteredList)
    
         
   

def saveToCsv(jobs):
   if not jobs:
      print("❌ No jobs to save!")
      return
   elif(os.path.exists(FilePath)):
      with open(FilePath,'w',newline='',encoding='utf-8') as f:
         fieldNames = jobs[0].keys()
         writer = csv.DictWriter(f=f,fieldnames=fieldNames)
         writer.writeheader()
         writer.writerows(jobs)

   print(f"💾 Saved {len(jobs)} jobs to: {FilePath}")
   return FilePath


def display_result(jobs):
   if not  jobs:
      print('No relevant jobs found')

   for job in jobs:
      print(f'jobTitle :- {job['jobTitle']}')
      print(f'jobCompany :- {job['jobCompany']}')
      print(f'jobLocation :- {job['jobLocation']}')
      print(f'jobPostedDate :- {job['jobPostedDate']}')
   
def main():
   jobs = parseData()
   filterJobs(jobs)


if __name__ == 'main':
   main()
   
   
  

   
         
         
    