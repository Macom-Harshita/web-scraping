from bs4 import BeautifulSoup
import requests
import cloudscraper

def get_codeforces_contests():
    def formattext(s):
        s = s.strip()
        s = s.strip('\n')
        return s
    scraper = cloudscraper.create_scraper()
    url = "https://codeforces.com/contests"

    page = scraper.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    """print(soup.prettify())"""
    datatable = soup.find('div', class_ = "datatable")
    table = datatable.find('table')
    contests = table.find_all('tr')[1:]
    contest_details = []
    for contest in contests:
        details = {}
        dets = contest.find_all('td')
        details['name'] = formattext(dets[0].text)
        details['date and time'] = formattext(dets[2].find('span', class_ = 'format-time').text)
        details['duration'] = formattext(dets[3].text)
        if dets[5].find('a'):
            details['register_link'] = 'https://codeforces.com' + dets[5].find('a')['href']
        else:
            details['register_link'] = 0
        contest_details.append(details)

    return contest_details 
