from bs4 import BeautifulSoup
import requests
import time

result = ""
print("What kind of job are you looking for?")
job_prospect = input("> ").lower()
print(f"Looking for jobs related to {job_prospect.title()}...")

for word in job_prospect.split():
    result += word + "+"
results = result[:-1]

print("Place the skill that you don't want to be included in your job")
unfamiliar_skill = input("> ")
print(f"Filtering Data Science Job without the {unfamiliar_skill} skill recquired.")
print()


def find_jobs():
    html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={results}&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text
        if 'few' in published_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace('(More Jobs)', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            job_position = job.header.h2.a.text
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    if '.' not in skills:
                        f.write(f"Required Skills: {skills.strip()} \n")
                    else:
                        f.write("This company does not have any particular skills required \n")
                    f.write(f"Job Description: {job_position.strip()} \n")
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 2
        print(f"Waiting for {time_wait} minutes")
        time.sleep(time_wait * 60)
