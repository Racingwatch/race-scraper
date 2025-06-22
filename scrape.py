import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_punters():
    url = 'https://www.punters.com.au/form-guide/2025-06-29/caulfield_123456/'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = []
    for race in soup.select('.race-summary'):
        name = race.select_one('.race-name').get_text(strip=True)
        for i, runner in enumerate(race.select('.runner-name'), start=1):
            rows.append({'raceName': name, 'runnerNumber': i, 'runnerName': runner.text.strip()})
    pd.DataFrame(rows).to_csv('punters_meeting.csv', index=False)

if __name__ == '__main__':
    scrape_punters()
