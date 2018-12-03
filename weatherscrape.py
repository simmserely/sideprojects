import sys
import re
import urllib.request
from bs4 import BeautifulSoup as BS
import pandas as pd

def get_page(url):
    page = urllib.request.urlopen(url)
    scrape = page.read()
    return scrape

def long_parse_page(scrape):
    soup = BS(scrape, 'html.parser')
    html = list(soup.children)[2]
    body = list(html.children)[3]
    p = list(html.body)[1]
    text = p.get_text()

def parse_page(scrape):
    soup = BS(scrape, 'html.parser')
    #p = soup.findAll('p')[0].get_text()
    #p = soup.findAll(id='second')
    #p = soup.select('div p')
    week_forecast = soup.find(id='seven-day-forecast')
    #daily_forecasts = week_forecast.findAll('div', 'tombstone-container')
    #day = daily_forecasts[0]
    #day_name = day.find('p', 'period-name').get_text()
    #day_summ = day.find('p', 'short-desc').get_text()
    #day_temp = day.find('p', 'temp').get_text()
    #day_desc = day.find('img')['title']
    return week_forecast

def main():
    url1 = 'http://dataquestio.github.io/web-scraping-pages/simple.html'
    url2 = 'http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html'
    url3 = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168'
    text = get_page(url3)
    week_forecast = parse_page(text)
    day_names_taglst = week_forecast.select('.tombstone-container .period-name')
    day_name_lst = [day.get_text() for day in day_names_taglst]
    day_summ_lst = [summ.get_text() for summ in week_forecast.select('.tombstone-container .short-desc')]
    day_temp_lst = [temp.get_text() for temp in week_forecast.select('.tombstone-container .temp')]
    day_desc_lst = [desc['title'] for desc in week_forecast.select('.tombstone-container img')]
    weather = pd.DataFrame({
        'day': day_name_lst,
        'summ': day_summ_lst,
        'temp': day_temp_lst,
        'desc': day_desc_lst
    })
    weather


if __name__ == '__main__':
    main()
